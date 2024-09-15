## \file ../src/suppliers/aliexpress/campaign/_experiments/prepare_new_campaign.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

"""! Эксперименты над сценарием новой рекламной камании """
...
import header

from pathlib import Path

from src.settings import gs

from src.suppliers.aliexpress.campaign import AliCampaignEditor
from src.utils import get_filenames, get_directory_names
from src.utils import pprint
from src.logger import logger

campaign_name = 'rc'
aliexpress_editor =  AliCampaignEditor(campaign_name)
aliexpress_editor.process_new_campaign(campaign_name)