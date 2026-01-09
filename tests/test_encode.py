import base64

import base64_utils


def test_b64encode() -> None:
    data = b"test"
    encoded = base64_utils.b64encode(data)
    expected = base64.b64encode(data)

    assert isinstance(encoded, bytes)
    assert expected == encoded


def test_b64encode_with_altchars() -> None:
    data = b"test\xff\xfe"
    encoded = base64_utils.b64encode(data, b"-_")
    expected = base64.b64encode(data, b"-_")

    assert isinstance(encoded, bytes)
    assert encoded == expected
