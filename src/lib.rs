use base64_simd::STANDARD;
use pyo3::prelude::*;

#[pyfunction]
pub fn b64encode(s: &[u8]) -> PyResult<String> {
    Ok(STANDARD.encode_to_string(s))
}

#[pymodule]
fn _base64_utils(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add("__version__", env!("CARGO_PKG_VERSION"))?;
    m.add_function(wrap_pyfunction!(b64encode, m)?)?;
    Ok(())
}
