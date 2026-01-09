# Python base64 utils


<div align="center">

<a href="https://pypi.org/project/base64-utils/" target="_blank">>
    <img src="https://badge.fury.io/py/base64-utils.svg" alt="Package version">
</a>
<a href="https://pypi.org/project/base64-utils" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/base64-utils.svg?color=%2334D058" alt="Supported Python versions">
</a>
<a href="https://codspeed.io/aminalaee/base64-utils?utm_source=badge" target="_blank">
    <img src="https://img.shields.io/endpoint?url=https://codspeed.io/badge.json" alt="Codspeed">
</a>

</div>

---

Fast, drop-in replacement for Python's base64 module, powered by Rust.

## Installation
Using `pip`:
```shell
$ pip install base64-utils
```

## Example

```shell
>>> import base64_utils as base64

>>> encoded = base64.b64encode(b'data to be encoded')
>>> encoded
b'ZGF0YSB0byBiZSBlbmNvZGVk'

>>> data = base64.b64decode(encoded)
>>> data
b'data to be encoded'
```

## Benchmarks

| Benchmark                          | Min   | Max   | Mean  | Min (+)      | Max (+)      | Mean (+)     |
| ---------------------------------- | ----- | ----- | ----- | ------------ | ------------ | ------------ |
| b64encode (1 KB data)              | 0.003 | 0.004 | 0.003 | 0.001 (3.6x) | 0.001 (3.8x) | 0.001 (3.7x) |
| b64encode (100 KB data)            | 0.301 | 0.330 | 0.309 | 0.046 (6.5x) | 0.061 (5.4x) | 0.050 (6.2x) |
| b64encode (1 MB data)              | 3.270 | 3.388 | 3.345 | 0.448 (7.3x) | 0.492 (6.9x) | 0.468 (7.1x) |
| b64encode (altchars + 100 KB data) | 0.464 | 0.490 | 0.477 | 0.322 (1.4x) | 0.340 (1.4x) | 0.332 (1.4x) |

## How to develop locally

```shell
$ make build
$ make test
```
