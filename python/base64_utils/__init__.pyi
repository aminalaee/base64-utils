from _typeshed import ReadableBuffer

__version__: str

__all__ = [
    "b64encode",
]

def b64encode(s: ReadableBuffer, altchars: ReadableBuffer | None = None) -> bytes: ...
