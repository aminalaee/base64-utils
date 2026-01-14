import base64

import base64_utils
import pytest


def test_b64decode() -> None:
    data = b"dGVzdA=="
    decoded = base64_utils.b64decode(data)
    expected = base64.b64decode(data)

    assert isinstance(decoded, bytes)
    assert expected == decoded


def test_b64decode_str() -> None:
    data = "dGVzdA=="
    decoded = base64_utils.b64decode(data)
    expected = base64.b64decode(data)

    assert isinstance(decoded, bytes)
    assert expected == decoded


def test_b64decode_altchars() -> None:
    data = b"dGVzdA+/"
    altchars = b"-_"
    decoded = base64_utils.b64decode(data, altchars=altchars)
    expected = base64.b64decode(data, altchars=altchars)

    assert isinstance(decoded, bytes)
    assert expected == decoded


def test_b64decode_altchars_invalid() -> None:
    with pytest.raises(ValueError):
        base64_utils.b64decode(b"dGVzdA+/", altchars=b"-")


def test_b64decode_validate() -> None:
    data_with_spaces = b"dGVz dA=="  # "test" with a space in the middle
    decoded = base64_utils.b64decode(data_with_spaces, validate=False)
    expected = base64.b64decode(data_with_spaces, validate=False)
    assert decoded == expected
    assert decoded == b"test"

    with pytest.raises(ValueError):
        base64_utils.b64decode(data_with_spaces, validate=True)
    with pytest.raises(ValueError):
        base64.b64decode(data_with_spaces, validate=True)


def test_b64decode_invalid_data() -> None:
    data = b"invalid_base64!!"
    with pytest.raises(ValueError):
        base64_utils.b64decode(data)


def test_standard_b64decode() -> None:
    data = base64.standard_b64encode(b"some data")

    decoded = base64_utils.standard_b64decode(data)
    expected = base64.standard_b64decode(data)

    assert isinstance(decoded, bytes)
    assert expected == decoded


def test_urlsafe_b64decode() -> None:
    data = base64.urlsafe_b64encode(b"some data")

    decoded = base64_utils.urlsafe_b64decode(data)
    expected = base64.urlsafe_b64decode(data)

    assert isinstance(decoded, bytes)
    assert expected == decoded
