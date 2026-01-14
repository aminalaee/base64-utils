use pyo3::prelude::*;

mod decoder;
mod encoder;

#[pymodule]
fn _base64_utils(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add("__version__", env!("CARGO_PKG_VERSION"))?;
    m.add_function(wrap_pyfunction!(decoder::b64decode, m)?)?;
    m.add_function(wrap_pyfunction!(decoder::standard_b64decode, m)?)?;
    m.add_function(wrap_pyfunction!(decoder::urlsafe_b64decode, m)?)?;
    m.add_function(wrap_pyfunction!(encoder::b64encode, m)?)?;
    m.add_function(wrap_pyfunction!(encoder::standard_b64encode, m)?)?;
    m.add_function(wrap_pyfunction!(encoder::urlsafe_b64encode, m)?)?;
    Ok(())
}
