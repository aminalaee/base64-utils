use base64_simd::{Out, STANDARD};
use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;
use pyo3::types::PyBytes;

#[pyfunction]
#[pyo3(signature = (s, altchars=None))]
pub fn b64encode(py: Python<'_>, s: &[u8], altchars: Option<&[u8]>) -> PyResult<Py<PyBytes>> {
    let output_len = STANDARD.encoded_length(s.len());

    if let Some(alt) = altchars {
        if alt.len() != 2 {
            return Err(PyValueError::new_err(
                "altchars must be a bytes-like object of length 2",
            ));
        }

        let output = PyBytes::new_with(py, output_len, |buf| {
            let _ = STANDARD.encode(s, Out::from_slice(buf));

            for byte in buf.iter_mut() {
                *byte = match *byte {
                    b'+' => alt[0],
                    b'/' => alt[1],
                    b => b,
                };
            }
            Ok(())
        })?;
        return Ok(output.into());
    }

    let output = PyBytes::new_with(py, output_len, |buf| {
        let _ = STANDARD.encode(s, Out::from_slice(buf));
        Ok(())
    })?;
    Ok(output.into())
}

#[pymodule]
fn _base64_utils(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add("__version__", env!("CARGO_PKG_VERSION"))?;
    m.add_function(wrap_pyfunction!(b64encode, m)?)?;
    Ok(())
}
