"""! HERE SHOULD BE A DESCRIPTION OF THE MODULE OPERATION ! """
## \file ../src/suppliers/aliexpress/_experiments/alirequests.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
import header   

from src.webdriver import Driver, Chrome, Firefox

d = Driver(Firefox)
d.get_url(r"https://www.aliexpress.com")
...