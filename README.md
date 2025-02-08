# Advanced Python Concepts

This repository contains various Python scripts demonstrating advanced Python concepts such as decorators, generators, concurrency, and more.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Modules](#modules)

## Overview

The repository covers various advanced Python topics with practical implementations, including:

- **Functional programming** (e.g., `functools.partial`, `singledispatch`)
- **Concurrency** using `asyncio`
- **Data classes** for structured objects
- **Generators** for efficient data handling
- **Cached properties** for optimized attribute access
- **HTTP requests** (both synchronous and asynchronous)

## Installation

### Clone the Repository

```bash
git clone https://github.com/matin-ghorbani/advanced-python.git
cd advanced-python
```

## Modules

`advanced_functions.py`
Demonstrates the use of `functools.partial` and functional programming techniques.

`cached_property.py`
Shows how to use `functools.cached_property` to cache computed values in a class.

`concurrency.py`
Compares synchronous and asynchronous HTTP requests using `asyncio` and `requests`.

`data_classes.py`
Implements Python data classes with custom `__post_init__` and `field` default values.

`dock_typing.py`
Demonstrates how to use Python's type hints for better code clarity and static analysis.

`generators.py`
Explains Python generators with examples of `yield` and coroutine-style data processing.

`requests_utils.py`
Contains helper functions for synchronous and asynchronous HTTP requests using `requests`.

`setter_getter.py`
Illustrates the use of Python's `@property` and `@property.setter` decorators for encapsulation.

`single_dispatch.py`
Uses `functools.singledispatch` for function overloading based on argument type.
