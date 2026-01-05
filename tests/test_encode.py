import base64_utils


def test_b64encode() -> None:
    encoded = base64_utils.b64encode(b"test")

    assert encoded == "dGVzdA=="
