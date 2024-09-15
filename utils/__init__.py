"""! модули управления рекламной кампанией Aliexpress:

 
"""
...
## \file ../src/suppliers/aliexpress/utils/__init__.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
...
from packaging.version import Version
from .version import __version__, __name__, __doc__, __details__, __annotations__,  __author__ 

from .extract_product_id import extract_prod_ids
from .ensure_https import ensure_https
from .locales import locales
