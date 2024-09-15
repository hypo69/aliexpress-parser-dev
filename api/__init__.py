"""! Aliexpress API wrapper"""
...
## \file ../src/suppliers/aliexpress/api/__init__.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
...
from packaging.version import Version
from .version import __version__, __name__, __doc__, __details__, __annotations__,  __author__  

from .api import AliexpressApi
from . import models



