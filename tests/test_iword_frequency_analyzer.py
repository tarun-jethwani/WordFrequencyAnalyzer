"""
This module contains parameterized test functions to test methods
of class IWordFrequencyAnalyzer

"""
import pytest

# importing dictionary of test data constants
from tests.test_data.inputs import TEST_DATA_1


# sends arguments to 'params_highest_frequency' fixture
# defined in conftest.py
# test_case_1
@pytest.mark.parametrize(
    "params_highest_frequency",
    TEST_DATA_1["test_case_1"][0],
    indirect=["params_highest_frequency"],
)
def test_highest_frequency(params_highest_frequency):
    """
    asserts actual value with the result obtained from
    calculate_highest_frequency method of IWordFrequencyAnalyzer class

    Parameters
    ----------
    params_highest_frequency : value obtained through text fixture
                               defined in conftest.py

    """
    # assert calculated_result == actual_result
    assert params_highest_frequency[0] == params_highest_frequency[1]


# sends arguments to 'params_word_frequency' fixture
# defined in conftest.py
# test_case_2
@pytest.mark.parametrize(
    "params_word_frequency",
    TEST_DATA_1["test_case_2"][0],
    indirect=["params_word_frequency"],
)
def test_word_frequency(params_word_frequency):
    """
    asserts actual value with the result obtained from
    calculate_frequency_for_word method of IWordFrequencyAnalyzer class

    Parameters
    ----------
    params_word_frequency : value obtained through text fixture
                            defined in conftest.py

    """
    # assert calculated_result == actual_result
    assert params_word_frequency[0] == params_word_frequency[1]


# sends arguments to 'params_most_common' fixture
# defined in conftest.py
# test_case_3
@pytest.mark.parametrize(
    "params_most_common",
    TEST_DATA_1["test_case_3"][0],
    indirect=["params_most_common"],
)
def test_most_frequent_n_words(params_most_common):
    """
    asserts actual value with the result obtained from
    calculate_most_frequent_n_words method of IWordFrequencyAnalyzer class

    Parameters
    ----------
    params_most_common : value obtained through text fixture
                         defined in conftest.py

    """
    # assert calculated_result == actual_result
    assert params_most_common[0] == params_most_common[1]


# test_case_4
@pytest.mark.parametrize(
    "params_highest_frequency",
    TEST_DATA_1["test_case_4"][0],
    indirect=["params_highest_frequency"],
)
def test_type_error_highest_frequency(params_highest_frequency):
    """
    if input text in calculate_highest_frequency method
    is not of type <str>, asserts exception message string
    from fixture, with the actual exception message string

    Parameters
    ----------
    params_highest_frequency : value obtained through text fixture
                                defined in conftest.py

    """
    # assert calculated_result == actual_result
    assert params_highest_frequency[0] == params_highest_frequency[1]


# test_case_5
@pytest.mark.parametrize(
    "params_highest_frequency",
    TEST_DATA_1["test_case_5"][0],
    indirect=["params_highest_frequency"],
)
def test_value_error_highest_frequency(params_highest_frequency):
    """
    if input text value is invalid, or if empty in
    calculate_highest_frequency method, asserts exception message string
    from fixture, with the actual exception message string

    Parameters
    ----------
    params_highest_frequency : value obtained through text fixture
                                defined in conftest.py

    """
    # assert calculated_result == actual_result
    assert params_highest_frequency[0] == params_highest_frequency[1]


# test_case_6
@pytest.mark.parametrize(
    "params_word_frequency",
    TEST_DATA_1["test_case_6"][0],
    indirect=["params_word_frequency"],
)
def test_typeerror_for_text_in_word_frequency(params_word_frequency):
    """
    if input text in calculate_frequency_for_word method is
    not of type <str>, asserts exception message string
    from fixture, with the actual exception message string

    Parameters
    ----------
    params_word_frequency : value obtained through text fixture
                            defined in conftest.py

    """
    # assert calculated_result == actual_result
    assert params_word_frequency[0] == params_word_frequency[1]


# test_case_7
@pytest.mark.parametrize(
    "params_word_frequency",
    TEST_DATA_1["test_case_7"][0],
    indirect=["params_word_frequency"],
)
def test_typeerror_for_word_in_word_frequency(params_word_frequency):
    """
    if word passed to calculate_frequency_for_word method is
    not of type <str>, asserts exception message string
    from fixture, with the actual exception message string

    Parameters
    ----------
    params_word_frequency : value obtained through text fixture
                            defined in conftest.py

    """
    # assert calculated_result == actual_result
    assert params_word_frequency[0] == params_word_frequency[1]


# test_case_8
@pytest.mark.parametrize(
    "params_word_frequency",
    TEST_DATA_1["test_case_8"][0],
    indirect=["params_word_frequency"],
)
def test_value_error_for_text_in_word_frequency(params_word_frequency):
    """
    if value of input text in calculate_frequency_for_word method
    is invalid, asserts exception message string from fixture,
    with the actual exception message string

    Parameters
    ----------
    params_word_frequency : value obtained through text fixture
                            defined in conftest.py

    """
    # assert calculated_result == actual_result
    assert params_word_frequency[0] == params_word_frequency[1]


# test_case_9
@pytest.mark.parametrize(
    "params_word_frequency",
    TEST_DATA_1["test_case_9"][0],
    indirect=["params_word_frequency"],
)
def test_value_error_for_word_in_word_frequency(params_word_frequency):
    """
    if value of word passed to calculate_frequency_for_word method
    is invalid, asserts exception message string from fixture,
    with the actual exception message string

    Parameters
    ----------
    params_word_frequency : value obtained through text fixture
                            defined in conftest.py

    """
    # assert calculated_result == actual_result
    assert params_word_frequency[0] == params_word_frequency[1]


# test_case_10
@pytest.mark.parametrize(
    "params_most_common",
    TEST_DATA_1["test_case_10"][0],
    indirect=["params_most_common"],
)
def test_type_error_for_n_most_frequent_n_words(params_most_common):
    """
    if argument 'n' passed to calculate_most_frequent_n_words method
    is not of type <int>, asserts exception message string from fixture,
    with the actual exception message string

    Parameters
    ----------
    params_most_common : value obtained through text fixture
                         defined in conftest.py

    """
    # assert calculated_result == actual_result
    assert params_most_common[0] == params_most_common[1]


# test_case_11
@pytest.mark.parametrize(
    "params_most_common",
    TEST_DATA_1["test_case_11"][0],
    indirect=["params_most_common"],
)
def test_value_error_for_text_most_frequent_n_words(params_most_common):
    """
    if value of input text in calculate_most_frequent_n_words method
    is invalid, asserts exception message string from fixture,
    with the actual exception message string

    Parameters
    ----------
    params_most_common : value obtained through text fixture
                         defined in conftest.py

    """
    # assert calculated_result == actual_result
    assert params_most_common[0] == params_most_common[1]


# test_case_12
@pytest.mark.parametrize(
    "params_most_common",
    TEST_DATA_1["test_case_12"][0],
    indirect=["params_most_common"],
)
def test_type_error_for_text_most_frequent_n_words(params_most_common):
    """
    if input text in calculate_most_frequent_n_words method
    is not of type <str>, asserts exception message string from fixture,
    with the actual exception message string

    Parameters
    ----------
    params_most_common : value obtained through text fixture
                         defined in conftest.py

    """
    # assert calculated_result == actual_result
    assert params_most_common[0] == params_most_common[1]


# test_case_13
@pytest.mark.parametrize(
    "params_most_common",
    TEST_DATA_1["test_case_13"][0],
    indirect=["params_most_common"],
)
def test_value_error_most_frequent_n_words(params_most_common):
    """
    if value of argument 'n' passed to calculate_most_frequent_n_words
    method is invalid, asserts exception message string from fixture,
    with the actual exception message string

    Parameters
    ----------
    params_most_common : value obtained through text fixture
                         defined in conftest.py

    """
    # assert calculated_result == actual_result
    assert params_most_common[0] == params_most_common[1]


# test_case_14
@pytest.mark.parametrize(
    "params_most_common",
    TEST_DATA_1["test_case_14"][0],
    indirect=["params_most_common"],
)
def test_n_greater_than_total_words(params_most_common):
    """
    if value of argument 'n' passed to calculate_most_frequent_n_words
    method exceeds total number of words in input text,
    asserts exception message string from fixture,
    with the actual exception message string

    Parameters
    ----------
    params_most_common : value obtained through text fixture
                         defined in conftest.py

    """
    # assert calculated_result == actual_result
    assert params_most_common[0] == params_most_common[1]
