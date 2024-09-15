## \file ../src/suppliers/aliexpress/campaign/ali_campaign_editor.py
## \file ../src/suppliers/aliexpress/campaign/ali_campaign_editor.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts/python
"""! This module provides the editor for advertising campaigns.
"""

import re
import shutil
from pathlib import Path
from types import SimpleNamespace
from typing import List, Optional

import header
from src.settings import gs
from src.suppliers.aliexpress.campaign.ali_promo_campaign import AliPromoCampaign
from src.suppliers.aliexpress.campaign.gsheet import AliCampaignGoogleSheet
from src.suppliers.aliexpress.utils import extract_prod_ids, ensure_https
from src.utils import j_loads_ns, j_loads, j_dumps
from src.utils.convertor.csv2json_csv2dict import csv2dict
from src.utils import pprint
from src.utils.file import read_text_file, save_text_file, get_filenames
from src.logger import logger

class AliCampaignEditor(AliPromoCampaign):
    """! Editor for advertising campaigns.
    """
    def __init__(self, 
                 campaign_name: str, 
                 language: Optional[str | dict] = None, 
                 currency: Optional[str] = None):
        """! Initialize the AliCampaignEditor with the given parameters.
        
        Args:
            campaign_name (Optional[str]): The name of the campaign. Defaults to `None`.
            language (Optional[str | dict]): The language of the campaign. Defaults to 'EN'.
            currency (Optional[str]): The currency for the campaign. Defaults to 'USD'.
            campaign_file (Optional[str | Path]): Optionally load a `<lang>_<currency>.json` file from the campaign root folder. Defaults to `None`.

        Raises:
            CriticalError: If neither `campaign_name` nor `campaign_file` is provided.
        
        Example:
        # 1. by campaign parameters
            >>> editor = AliCampaignEditor(campaign_name="Summer Sale", language="EN", currency="USD")
        # 2. load fom file
            >>> editor = AliCampaignEditor(campaign_name="Summer Sale", campaign_file="EN_USD.JSON")
        """
        ...
        super().__init__(campaign_name = campaign_name, language = language, currency = currency)
        #self.google_sheet = AliCampaignGoogleSheet(campaign_name = campaign_name, language = language, currency = currency, campaign_editor = self)

    def delete_product(self, product_id: str, exc_info: bool = False):
        """! Delete a product that does not have an affiliate link.
        
        Args:
            product_id (str): The ID of the product to be deleted.
            exc_info (bool): Whether to include exception information in logs. Defaults to `False`.

        Example:
            >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
            >>> editor.delete_product("12345")
        """
        ...
        _product_id = extract_prod_ids(product_id)
        
        product_path = self.category_path / 'sources.txt'
        prepared_product_path = self.category_path / '_sources.txt'
        products_list = read_text_file(product_path)
        if products_list:
            for record in products_list:
                if _product_id:
                    record_id = extract_prod_ids(record)
                    if record_id == str(product_id):
                        products_list.remove(record)
                        save_text_file((products_list, '\n'), prepared_product_path)
                        break
                else:
                    if record == str(product_id):
                        products_list.remove(record)
                        save_text_file((products_list, '\n'), product_path)
                    
        else:
            product_path = self.category_path / 'sources' / f'{product_id}.html'    
            try:
                product_path.rename(self.category_path / 'sources' / f'{product_id}_.html')
                logger.success(f"Product file {product_path=} renamed successfully.")
            except FileNotFoundError as ex:
                logger.error(f"Product file {product_path=} not found.", exc_info=exc_info)
            except Exception as ex:
                logger.critical(f"An error occurred while deleting the product file {product_path}.", ex)

    def update_product(self, category_name: str, lang: str, product: dict):
        """! Update product details within a category.

        Args:
            category_name (str): The name of the category where the product should be updated.
            lang (str): The language of the campaign.
            product (dict): A dictionary containing product details.

        Example:
            >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
            >>> editor.update_product("Electronics", "EN", {"product_id": "12345", "title": "Smartphone"})
        """
        ...
        self.dump_category_products_files(category_name, lang, product)

    def update_campaign(self):
        """! Update campaign properties such as `description`, `tags`, etc.
        
        Example:
            >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
            >>> editor.update_campaign()
        """
        ...

    def update_category(self, json_path: Path, category: SimpleNamespace) -> bool:
        """! Update the category in the JSON file.

        Args:
            json_path (Path): Path to the JSON file.
            category (SimpleNamespace): Category object to be updated.

        Returns:
            bool: True if update is successful, False otherwise.

        Example:
            >>> category = SimpleNamespace(name="New Category", description="Updated description")
            >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
            >>> result = editor.update_category(Path("category.json"), category)
            >>> print(result)  # True if successful
        """
        ...
        try:
            data = j_loads(json_path)  # Read JSON data from file
            data['category'] = category.__dict__  # Convert SimpleNamespace to dict
            j_dumps(data, json_path)  # Write updated JSON data back to file
            return True
        except Exception as ex:
            logger.error(f"Failed to update category {json_path}: {ex}")
            return False

    def get_category(self, category_name: str) -> Optional[SimpleNamespace]:
        """! Returns the SimpleNamespace object for a given category name.

        Args:
            category_name (str): The name of the category to retrieve.

        Returns:
            Optional[SimpleNamespace]: SimpleNamespace object representing the category or `None` if not found.

        Example:
            >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
            >>> category = editor.get_category("Electronics")
            >>> print(category)  # SimpleNamespace or None
        """
        ...
        try:
            if hasattr(self.campaign.category, category_name):
                return getattr(self.campaign.category, category_name)
            else:
                logger.warning(f"Category {category_name} not found in the campaign.")
                return None
        except Exception as ex:
            logger.error(f"Error retrieving category {category_name}.", ex, exc_info=True)
            return None
