""" contains constants to be used by other modules and functions """
from .utils.main_utils import (execute_frequency_for_word,
                               execute_highest_frequency,
                               execute_most_frequent_n_words)

# options map is mapping of function, function_name
# and its arguments with option value

OPTIONS_MAP = {
    1: {"name": "Calculate Highest Frequency",
        "func_name": execute_highest_frequency,
        "params": {"text": None}},
    2: {"name": "Calculate Frequency for Word",
        "func_name": execute_frequency_for_word,
        "params": {"text": None, "word": None}},
    3: {"name": "Calculate Most Frequent N Words",
        "func_name": execute_most_frequent_n_words,
        "params": {"text": None, "n": None}}
}
