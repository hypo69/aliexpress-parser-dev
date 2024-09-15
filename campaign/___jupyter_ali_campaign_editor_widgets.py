
"""! Виджеты редактора рекламной кампании. Используется кроме али еще и на фб. 
После изменения раскоментируй 
%%writefile campaign_editor_jupyter.py

@code
import campaign_editor_jupyter as ce

ce.CampaignEditor().display_widgets()
@endcode
"""

## \file ../src/suppliers/aliexpress/campaign/___jupyter_ali_campaign_editor_widgets.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python

import header  

from pathlib import Path
from ipywidgets import widgets
from IPython.display import display
import webbrowser

from src.settings import gs
from src.suppliers.aliexpress.campaign.gsheet import AliCampaignGoogleSheet
from src.logger import logger

class JupyterCampaignEditorWidgets:
    def __init__(self):
        self.campaign_editor = None
        self.campaigns_directory = Path(gs.path.data, 'aliexpress', 'campaigns')
        if not self.campaigns_directory.exists():
            logger.error(f"Directory does not exist: {self.campaigns_directory=}")
            #raise FileNotFoundError(f"Directory does not exist: {self.campaigns_directory}")

        self.languages = {'EN': 'USD', 'HE': 'ILS', 'RU': 'ILS'}
        self.campaign_name_dropdown = widgets.Dropdown(
            options=self.get_directory_names(self.campaigns_directory),
            description='Campaign Name:'
        )
        self.category_name_dropdown = widgets.Dropdown(
            options=[],
            description='Category:'
        )
        self.language_dropdown = widgets.Dropdown(
            options=[(f"{lang} - {curr}", {lang: curr}) for lang, curr in self.languages.items()],
            description='Language/Currency:'
        )

        self.initialize_button = widgets.Button(
            description='Initialize Campaign Editor',
            disabled=False,
        )
        self.save_button = widgets.Button(
            description='Save campaign',
            disabled=False,
        )
        self.show_products_button = widgets.Button(
            description='Show Products',
            disabled=False,
        )
        self.open_spreadsheet_button = widgets.Button(
            description='Open Google Spreadsheet',
            disabled=False,
        )

        self.setup_callbacks()

    def get_directory_names(self, path):
        """Returns a list of directory names in the given path."""
        return [d.name for d in path.iterdir() if d.is_dir()]

    def update_category_dropdown(self, campaign_name):
        """Updates the category dropdown based on the selected campaign."""
        campaign_path = self.campaigns_directory / campaign_name / 'category'
        if not campaign_path.exists():
            logger.error(f"Path does not exist: {campaign_path}")
            self.category_name_dropdown.options = []
        else:
            campaign_categories = self.get_directory_names(campaign_path)
            self.category_name_dropdown.options = campaign_categories
            #logger.debug(f"Available categories: {campaign_categories}")

    def on_campaign_name_change(self, change):
        campaign_name = change['new']
        #logger.debug(f"Selected campaign: {campaign_name}")
        self.update_category_dropdown(campaign_name)

    def initialize_campaign_editor(self, _):
        campaign_name = self.campaign_name_dropdown.value
        category_name = self.category_name_dropdown.value or None
        locale = self.language_dropdown.value

        if campaign_name and locale:
            self.campaign_editor = AliCampaignGoogleSheet(campaign_name=campaign_name, language=locale)
            self.update_category_dropdown(campaign_name)
        else:
            print("Please select campaign name and language/currency before initializing the editor.")

    def save_campaign(self, _):
        campaign_name = self.campaign_name_dropdown.value
        category_name = self.category_name_dropdown.value
        locale = self.language_dropdown.value
        if campaign_name and locale:
            self.campaign_editor = AliCampaignGoogleSheet(campaign_name=campaign_name, category_name=category_name if category_name else None, language=locale)
            try:
                self.campaign_editor.save_categories_from_worksheet()
                #logger.info("Campaign and categories saved successfully.")
            except Exception as ex:
                logger.error("Error saving campaign.", ex)
        else:
            print("Please select campaign name and language/currency before saving the campaign.")

    def show_products(self, _):
        campaign_name = self.campaign_name_dropdown.value
        category_name = self.category_name_dropdown.value
        locale = self.language_dropdown.value

        try:
            self.campaign_editor = AliCampaignGoogleSheet(campaign_name=campaign_name, language=locale)
            self.campaign_editor.set_products_worksheet(category_name)
        except Exception as ex:
            logger.error("Error displaying products.", ex)

    def open_spreadsheet(self, _):
        """Opens the Google Spreadsheet in a browser."""
        if self.campaign_editor:
            spreadsheet_url = f"https://docs.google.com/spreadsheets/d/{self.campaign_editor.spreadsheet_id}/edit"
            webbrowser.open(spreadsheet_url)
        else:
            print("Please initialize the campaign editor first.")

    def setup_callbacks(self):
        self.campaign_name_dropdown.observe(self.on_campaign_name_change, names='value')
        self.initialize_button.on_click(self.initialize_campaign_editor)
        self.save_button.on_click(self.save_campaign)
        self.show_products_button.on_click(self.show_products)
        self.open_spreadsheet_button.on_click(self.open_spreadsheet)

    def display_widgets(self):
        display(self.campaign_name_dropdown, self.category_name_dropdown, self.language_dropdown,
                self.initialize_button, self.save_button, self.show_products_button, self.open_spreadsheet_button)

        if self.campaign_name_dropdown.value:
            self.update_category_dropdown(self.campaign_name_dropdown.value)
            

