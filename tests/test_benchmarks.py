import base64_utils
import pytest

pytest.importorskip("pytest_codspeed")


@pytest.mark.benchmark
def test_b64encode() -> None:
    base64_utils.b64encode(b"test data")


@pytest.mark.benchmark
def test_b64encode_altchars() -> None:
    base64_utils.b64encode(b"test data", altchars=b"-_")


@pytest.mark.benchmark
def test_standard_b64encode() -> None:
    base64_utils.standard_b64encode(b"test data")


@pytest.mark.benchmark
def test_urlsafe_b64encode() -> None:
    base64_utils.urlsafe_b64encode(b"test data")


@pytest.mark.benchmark
def test_b64decode() -> None:
    base64_utils.b64decode(b"dGVzdA==")


@pytest.mark.benchmark
def test_b64decode_str() -> None:
    base64_utils.b64decode("dGVzdA==")
