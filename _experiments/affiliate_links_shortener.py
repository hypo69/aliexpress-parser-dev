## \file src/suppliers/aliexpress/_experiments/affiliate_links_shortener.py
## \file ../src/suppliers/aliexpress/_experiments/affiliate_links_shortener.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
"""! Short affiliate links """

import header
from src.suppliers.aliexpress import AffiliateLinksShortener

a = AffiliateLinksShortener()
url = 'https://aliexpress.com'
link = a.short_affiliate_link(url)
...