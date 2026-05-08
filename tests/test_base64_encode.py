import base64

import base64_utils
import pytest


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


def test_b64encode_with_invalid_altchars() -> None:
    with pytest.raises(ValueError) as excinfo:
        base64_utils.b64encode(b"test", b"-")
    assert str(excinfo.value) == "altchars must be a bytes-like object of length 2"


def test_standard_b64encode() -> None:
    data = b"example data"
    encoded = base64_utils.standard_b64encode(data)
    expected = base64.b64encode(data)

    assert isinstance(encoded, bytes)
    assert expected == encoded


def test_urlsafe_b64encode() -> None:
    data = b"example data"
    encoded = base64_utils.urlsafe_b64encode(data)
    expected = base64.urlsafe_b64encode(data)

    assert isinstance(encoded, bytes)
    assert expected == encoded


def test_encodebytes() -> None:
    data = b"Hello, World!"
    encoded = base64_utils.encodebytes(data)
    expected = base64.encodebytes(data)

    assert isinstance(encoded, bytes)
    assert expected == encoded


def test_encodebytes_multiline() -> None:
    data = b"A" * 100
    encoded = base64_utils.encodebytes(data)
    expected = base64.encodebytes(data)

    assert expected == encoded
    lines = encoded.split(b"\n")
    assert all(len(line) <= 76 for line in lines)


def test_encodebytes_empty() -> None:
    assert base64_utils.encodebytes(b"") == base64.encodebytes(b"")
