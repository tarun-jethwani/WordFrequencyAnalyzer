"""
This module contains test constants used as inputs to test functions

"""
TEXT1 = "##@Apple&^*_Mango08%$Orange#$%Mango;guava::Guava$Banana#Mango" \
        "?/Orange*apple(Banana:"
TEXT2 = "##@Rose&^*_Tulip08%$sunflower#*&tulip$%lily;tulip::Rose$#>" \
        "SunFlower?Lotus?jasmin*lily(tulip:"
TEXT3 = "The sun shines over the lake"

FREQUENCY_1 = 3
FREQUENCY_2 = 4

WORD_1 = "guava"
WORD_2 = "jasmin"
WORD_3 = "elephant"
WORD_4 = "_the"

FREQUENCY_GUAVA = 2
FREQUENCY_JASMIN = 1

FRUITS_ORDER = [("mango", 3), ("apple", 2)]
FLOWER_ORDER = [("tulip", 4), ("lily", 2), ("rose", 2)]

N_VALUE1 = 2
N_VALUE2 = 3

DUMMY_FLOAT = 45.6
DUMMY_INT = 4

EMPTY_TEXT_1 = ""
EMPTY_TEXT_2 = "  "

WORD_FREQUENCY_PAIR = [("elephant", 3)]
NON_STR_WORD_PAIRS = [(45, 5), (33.40, 10)]
NON_ALPHA_NON_LOWER_CASE_PAIRS = [("oRAnge", 8), ("Guava", 6),
                                  ("&%rose", 4), ("%$#lily*", 2)]
NON_INT_FREQUENCY_PAIRS = [("tulip", 32.1), ("lily", "rose")]
INVALID_FREQUENCY_PAIRS = [("rose", 0), ("apple", -1)]

# flask demo url routes
URL_HIGHEST_FREQUENCY = "/calculate_highest_frequency/The%20sun%20shines" \
                        "%20over%20the%20lake/"
URL_FREQUENCY_FOR_WORD = "/calculate_frequency_for_word/The%20sun%20shines" \
                         "%20over%20the%20lake/over"
URL_MOST_FREQUENT_N_WORDS = "/calculate_most_frequent_n_words/The%20sun" \
                            "%20shines%20over%20the%20lake/2"

URL_ERROR_HIGHEST_FREQUENCY = "/calculate_highest_frequency/9/"
URL_ERROR_FREQUENCY_FOR_WORD = "/calculate_frequency_for_word/9/over"
URL_ERROR_MOST_FREQUENT_WORDS = "/calculate_most_frequent_n_words/" \
                                "The sun shines over the lake/the"


# error / exception messages
TEXT_TYPE_ERROR = "text should be string"
TEXT_VALUE_ERROR = "text is empty"
WORD_TYPE_ERROR = "word should be string"
WORD_VALUE_ERROR = "word is empty"
N_TYPE_ERROR = "pass integer for n"
N_VALUE_ERROR = "most frequent words should be at least 1"
MAX_N_ERROR = "n exceeds the total number of unique words"
LOWER_CASE_CONDITION = "word should contain only chars from [a-z]"
FREQUENCY_TYPE_ERROR = "frequency should be integer"
INVALID_FREQUENCY = "Cannot create instance for word which does not occur"

NUM_STRING = '3'
INVALID_NUM_STRING = 'yk'
PARAMS = ['The sun shines over the lake', '3']

# creating dictionary of test data for test cases
TEST_DATA_1 = {
    "test_case_1": ([(TEXT1, FREQUENCY_1), (TEXT2, FREQUENCY_2)],
                    "test_highest_frequency"),
    "test_case_2": ([(TEXT1, WORD_1, FREQUENCY_GUAVA),
                     (TEXT2, WORD_2, FREQUENCY_JASMIN)],
                    "test_word_frequency"),
    "test_case_3": ([(TEXT1, N_VALUE1, FRUITS_ORDER),
                     (TEXT2, N_VALUE2, FLOWER_ORDER)],
                    "test_most_frequent_n_words"),
    "test_case_4": ([(DUMMY_FLOAT, TEXT_TYPE_ERROR),
                     (DUMMY_INT, TEXT_TYPE_ERROR)],
                    "test_type_error_highest_frequency"),
    "test_case_5": ([(EMPTY_TEXT_1, TEXT_VALUE_ERROR),
                     (EMPTY_TEXT_2, TEXT_VALUE_ERROR)],
                    "test_value_error_highest_frequency"),
    "test_case_6": ([(DUMMY_FLOAT, WORD_1, TEXT_TYPE_ERROR),
                     (DUMMY_INT, WORD_2, TEXT_TYPE_ERROR)],
                    "test_typeerror_for_text_in_word_frequency"),
    "test_case_7": ([(TEXT1, DUMMY_FLOAT, WORD_TYPE_ERROR),
                     (TEXT2, DUMMY_INT, WORD_TYPE_ERROR)],
                    "test_typeerror_for_word_in_word_frequency"),
    "test_case_8": ([(EMPTY_TEXT_1, WORD_1, TEXT_VALUE_ERROR),
                     (EMPTY_TEXT_2, WORD_2, TEXT_VALUE_ERROR)],
                    "test_value_error_for_text_in_word_frequency"),
    "test_case_9": ([(TEXT1, EMPTY_TEXT_1, WORD_VALUE_ERROR),
                     (TEXT2, EMPTY_TEXT_2, WORD_VALUE_ERROR)],
                    "test_value_error_for_word_in_word_frequency"),
    "test_case_10": ([(TEXT1, DUMMY_FLOAT, N_TYPE_ERROR),
                      (TEXT2, WORD_2, N_TYPE_ERROR)],
                     "test_type_error_for_n_most_frequent_n_words"),
    "test_case_11": ([(EMPTY_TEXT_1, 2, TEXT_VALUE_ERROR),
                      (EMPTY_TEXT_2, 1, TEXT_VALUE_ERROR)],
                     "test_value_error_for_text_most_frequent_n_words"),
    "test_case_12": ([(DUMMY_FLOAT, 2, TEXT_TYPE_ERROR),
                      (DUMMY_INT, 1, TEXT_TYPE_ERROR)],
                     "test_type_error_for_text_most_frequent_n_words"),
    "test_case_13": ([(TEXT1, 0, N_VALUE_ERROR), (TEXT2, -1, N_VALUE_ERROR)],
                     "test_value_error_most_frequent_n_words"),

    "test_case_14": ([(TEXT1, 20, MAX_N_ERROR), (TEXT2, 30, MAX_N_ERROR)],
                     "test_n_greater_than_total_words")
}

TEST_DATA_2 = {
    "FREQUENCY_1": FREQUENCY_1,
    "FREQUENCY_TYPE_ERROR": FREQUENCY_TYPE_ERROR,
    "INVALID_FREQUENCY": INVALID_FREQUENCY,
    "INVALID_FREQUENCY_PAIRS": INVALID_FREQUENCY_PAIRS,
    "LOWER_CASE_CONDITION": LOWER_CASE_CONDITION,
    "NON_ALPHA_NON_LOWER_CASE_PAIRS": NON_ALPHA_NON_LOWER_CASE_PAIRS,
    "NON_INT_FREQUENCY_PAIRS": NON_INT_FREQUENCY_PAIRS,
    "NON_STR_WORD_PAIRS": NON_STR_WORD_PAIRS,
    "WORD_3": WORD_3,
    "WORD_FREQUENCY_PAIR": WORD_FREQUENCY_PAIR,
    "WORD_TYPE_ERROR": WORD_TYPE_ERROR,
}
