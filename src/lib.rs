use base64_simd::{Out, STANDARD};
use pyo3::prelude::*;
use pyo3::types::PyBytes;

#[pyfunction]
#[pyo3(signature = (s, altchars=None))]
pub fn b64encode(py: Python<'_>, s: &[u8], altchars: Option<&[u8]>) -> PyResult<Py<PyBytes>> {
    if let Some(alt) = altchars {
        if alt.len() != 2 {
            return Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                "altchars must be a bytes object of length 2",
            ));
        }

        let output_len = STANDARD.encoded_length(s.len());
        let mut output = vec![0u8; output_len];
        let _ = STANDARD.encode(s, Out::from_slice(&mut output));

        for byte in &mut output {
            if *byte == b'+' {
                *byte = alt[0];
            } else if *byte == b'/' {
                *byte = alt[1];
            }
        }

        return Ok(PyBytes::new(py, &output).into());
    }

    let output_len = STANDARD.encoded_length(s.len());
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
