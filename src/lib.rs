use base64_simd::{Out, STANDARD, URL_SAFE};
use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;
use pyo3::types::PyBytes;

const STANDARD_CHARSET: &[u8] =
    b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";

#[derive(FromPyObject)]
pub enum StringOrBytes {
    #[pyo3(transparent, annotation = "str")]
    String(String),
    #[pyo3(transparent, annotation = "bytes")]
    Bytes(Vec<u8>),
}

impl StringOrBytes {
    fn into_bytes(self) -> Vec<u8> {
        match self {
            StringOrBytes::String(s) => s.into_bytes(),
            StringOrBytes::Bytes(b) => b,
        }
    }
}

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

#[pyfunction]
#[pyo3(signature = (s, altchars=None, validate=false))]
pub fn b64decode(
    py: Python<'_>,
    s: StringOrBytes,
    altchars: Option<StringOrBytes>,
    validate: bool,
) -> PyResult<Py<PyBytes>> {
    let mut input: Vec<u8> = s.into_bytes();

    if let Some(alt) = altchars {
        let bytes = alt.into_bytes();
        if bytes.len() != 2 {
            return Err(PyValueError::new_err(
                "altchars must be a bytes-like object of length 2",
            ));
        }

        for byte in input.iter_mut() {
            if *byte == bytes[0] {
                *byte = b'+';
            } else if *byte == bytes[1] {
                *byte = b'/';
            }
        }
    }

    if validate {
        for &b in &input {
            if !STANDARD_CHARSET.contains(&b) {
                return Err(PyValueError::new_err("Only base64 data is allowed"));
            }
        }
    } else {
        input.retain(|&b| STANDARD_CHARSET.contains(&b));
    }

    let output_len = STANDARD
        .decoded_length(&input)
        .map_err(|_| PyValueError::new_err("Invalid base64-encoded string"))?;
    let output: Bound<'_, PyBytes> = PyBytes::new_with(py, output_len, |buf| {
        let _ = STANDARD.decode(&input, Out::from_slice(buf));
        Ok(())
    })?;
    Ok(output.into())
}

#[pyfunction]
pub fn standard_b64encode(py: Python<'_>, s: &[u8]) -> PyResult<Py<PyBytes>> {
    let output_len = STANDARD.encoded_length(s.len());
    let output = PyBytes::new_with(py, output_len, |buf| {
        let _ = STANDARD.encode(s, Out::from_slice(buf));
        Ok(())
    })?;
    Ok(output.into())
}

#[pyfunction]
pub fn urlsafe_b64encode(py: Python<'_>, s: &[u8]) -> PyResult<Py<PyBytes>> {
    let output_len = URL_SAFE.encoded_length(s.len());
    let output = PyBytes::new_with(py, output_len, |buf| {
        let _ = URL_SAFE.encode(s, Out::from_slice(buf));
        Ok(())
    })?;
    Ok(output.into())
}

#[pymodule]
fn _base64_utils(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add("__version__", env!("CARGO_PKG_VERSION"))?;
    m.add_function(wrap_pyfunction!(b64encode, m)?)?;
    m.add_function(wrap_pyfunction!(b64decode, m)?)?;
    m.add_function(wrap_pyfunction!(standard_b64encode, m)?)?;
    m.add_function(wrap_pyfunction!(urlsafe_b64encode, m)?)?;
    Ok(())
}
