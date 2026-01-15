# Python base64-utils

<div align="center">

<a href="https://pypi.org/project/base64-utils/" target="_blank">
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
| b64encode (1 KB data)              | 0.004 | 0.004 | 0.004 | 0.001 (3.6x) | 0.001 (3.8x) | 0.001 (3.7x) |
| b64encode (100 KB data)            | 0.307 | 0.325 | 0.318 | 0.047 (6.6x) | 0.061 (5.3x) | 0.050 (6.4x) |
| b64encode (1 MB data)              | 3.383 | 3.456 | 3.411 | 0.447 (7.6x) | 0.487 (7.1x) | 0.467 (7.3x) |
| b64encode (altchars + 100 KB data) | 0.472 | 0.490 | 0.483 | 0.303 (1.6x) | 0.320 (1.5x) | 0.313 (1.5x) |
| b64decode (100 KB data)            | 0.512 | 0.569 | 0.538 | 0.110 (4.7x) | 0.125 (4.5x) | 0.117 (4.6x) |

## How to develop locally

```shell
$ make build
$ make test
```
