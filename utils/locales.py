## \file ../src/suppliers/aliexpress/utils/locales.py
# -*- coding: utf-8 -*-
#! /usr/bin/python3
"""! Module for loading locales data from JSON file.

This module contains functions for loading and processing locales data from a JSON file.

Functions:
    load_locales_data(path: Path) -> list[dict[str, str]]:
        Load locales data from a JSON file.

Examples:
    >>> from src.suppliers.aliexpress.utils.locales import load_locales_data
    >>> locales = load_locales_data(Path('/path/to/locales.json'))
    >>> print(locales)
    [{'EN': 'USD'}, {'HE': 'ILS'}, {'RU': 'ILS'}, {'EN': 'EUR'}, {'EN': 'GBR'}, {'RU': 'EUR'}]
"""
...
from pathlib import Path

from src.settings import gs
from src.utils import j_loads

def get_locales(locales_path: Path | str) -> list[dict[str, str]]:
    """Load locales data from a JSON file.

    Args:
        path (Path): Path to the JSON file containing locales data.

    Returns:
        list[dict[str, str]]: List of dictionaries with locale and currency pairs.

    Examples:
        >>> from src.suppliers.aliexpress.utils.locales import load_locales_data
        >>> locales = load_locales_data(Path('/path/to/locales.json'))
        >>> print(locales)
        [{'EN': 'USD'}, {'HE': 'ILS'}, {'RU': 'ILS'}, {'EN': 'EUR'}, {'EN': 'GBR'}, {'RU': 'EUR'}]
    """
    return j_loads(locales_path).get('locales', [])


locales:list[dict[str, str]] = get_locales (gs.path.src / 'suppliers' / 'aliexpress' / 'utils' / 'locales.json') # defined locales for campaigns
