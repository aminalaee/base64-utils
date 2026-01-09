import base64_utils
import pytest

pytest.importorskip("pytest_codspeed")


@pytest.mark.benchmark
def test_b64encode() -> None:
    base64_utils.b64encode(b"test data")


@pytest.mark.benchmark
def test_b64encode_altchars() -> None:
    base64_utils.b64encode(b"test data", altchars=b"-_")
