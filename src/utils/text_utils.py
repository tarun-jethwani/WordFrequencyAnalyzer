""" This module contains utility functions process text """
import re
from typing import List

from .log_utils import logger


def find_words(text: str) -> List[str]:
    """
    finds all lower case words from text
    using regex pattern

    Parameters
    ----------
    text : str
        input text received from user

    Returns
    -------
    all_words : list
        list of all the words found in the input text

    """
    logger.debug(f"received text : {text} as parameter")
    # case insensitive searching
    text = text.lower()
    # find all occurrences for group of alphabetic chars
    all_words = re.findall(r"[a-z]+", text)
    if len(all_words) == 0:
        logger.debug(f"No words in input text {text}")
        raise ValueError("input text value is invalid")
    logger.info(f"all words found in text {all_words}")
    return all_words
