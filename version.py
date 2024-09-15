﻿"""! aliexpress special vars
- `__version__`: This variable holds the version of the module or package.
- `__name__`: Contains the name of the module. If the script is being run directly, the value will be `"__main__"`.
- `__doc__`: The module's documentation string.
- `__details__`: This variable likely contains additional details about the module, but the exact purpose depends on the specific module or package.
- `__annotations__`: Contains type annotations for variables and functions in the module.
- `__author__`: The name(s) of the author(s) of the module.
"""

## \file ../src/suppliers/aliexpress/version.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
__name__:str
__version__="3.12.0.0.0.5"
__doc__:str="Supplier `aliexpress` classes, methods and attributes"
__details__:str="Добавлена логика работы через requests"
__annotations__
__examples__ =f"""
@code
from src.suppliers.aliexpress import Aliexpress, AliApi, AliRequests 
@endcode
"""
__author__='hypotez '

