"""! Aliexpress Проверки логин, кукис итп. """
## \file ../src/suppliers/aliexpress/_experiments/web_login.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python


import header
from pathlib import Path
import pickle
import requests

from src.settings import gs
from src.suppliers import Supplier
from src.utils import pprint

a = Supplier('aliexpress')

d = a.driver
d.get_url('https://aliexpress.com')