"""! Проверка создания affiliate для рекламной кампании  
Если текой рекламной кампании не существует - будет создана новая"""
## \file ../src/suppliers/aliexpress/campaign/_experiments/prepare_campaign.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
...
import header
from src.suppliers.aliexpress.campaign import 

locales = {'EN': 'USD', 'HE': 'ILS', 'RU': 'ILS'}
campaign_name:str = 'rc'
language: str = 'EN'
currency: str = 'USD'
campaign_file:str = None
# Если текой рекламной кампании не существует - будет создана новая

#process_campaign(campaign_name = campaign_name, language = language, currency = currency, campaign_file = campaign_file)
process_campaign(campaign_name = campaign_name, language = language, currency = currency, campaign_file = campaign_file)

    