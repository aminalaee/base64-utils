use base64_simd::{Out, STANDARD, URL_SAFE, forgiving_decode_inplace};
use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;
use pyo3::types::PyBytes;

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
        STANDARD
            .check(&input)
            .map_err(|_| PyValueError::new_err("Invalid base64-encoded string"))?;

        let output_len = STANDARD
            .decoded_length(&input)
            .map_err(|_| PyValueError::new_err("Invalid base64-encoded string"))?;

        let output: Bound<'_, PyBytes> = PyBytes::new_with(py, output_len, |buf| {
            STANDARD
                .decode(&input, Out::from_slice(buf))
                .map_err(|_| PyValueError::new_err("Invalid base64-encoded string"))?;
            Ok(())
        })?;
        Ok(output.into())
    } else {
        let output = forgiving_decode_inplace(&mut input)
            .map_err(|_| PyValueError::new_err("Invalid base64-encoded string"))?;
        Ok(PyBytes::new(py, output).into())
    }
}

#[pyfunction]
pub fn standard_b64decode(py: Python<'_>, s: StringOrBytes) -> PyResult<Py<PyBytes>> {
    let input: Vec<u8> = s.into_bytes();
    let output_len = STANDARD
        .decoded_length(&input)
        .map_err(|_| PyValueError::new_err("Invalid base64-encoded string"))?;
    let output = PyBytes::new_with(py, output_len, |buf| {
        let _ = STANDARD.decode(&input, Out::from_slice(buf));
        Ok(())
    })?;
    Ok(output.into())
}

#[pyfunction]
pub fn urlsafe_b64decode(py: Python<'_>, s: StringOrBytes) -> PyResult<Py<PyBytes>> {
    let input: Vec<u8> = s.into_bytes();
    let output_len = URL_SAFE
        .decoded_length(&input)
        .map_err(|_| PyValueError::new_err("Invalid base64-encoded string"))?;
    let output = PyBytes::new_with(py, output_len, |buf| {
        let _ = URL_SAFE.decode(&input, Out::from_slice(buf));
        Ok(())
    })?;
    Ok(output.into())
}
