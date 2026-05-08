use base64_simd::{Out, STANDARD, URL_SAFE};
use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;
use pyo3::types::PyBytes;

const MAXLINESIZE: usize = 76;
const MAXBINSIZE: usize = 57;

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

#[pyfunction]
pub fn encodebytes(py: Python<'_>, s: &[u8]) -> PyResult<Py<PyBytes>> {
    let encoded_len = STANDARD.encoded_length(s.len());
    let num_lines = (encoded_len + MAXLINESIZE - 1) / MAXLINESIZE;
    let total_len = encoded_len + num_lines; // one \n per line

    let output = PyBytes::new_with(py, total_len, |buf| {
        let mut pos = 0;
        for chunk in s.chunks(MAXBINSIZE) {
            let enc_len = STANDARD.encoded_length(chunk.len());
            let _ = STANDARD.encode(chunk, Out::from_slice(&mut buf[pos..pos + enc_len]));
            pos += enc_len;
            buf[pos] = b'\n';
            pos += 1;
        }
        Ok(())
    })?;
    Ok(output.into())
}
