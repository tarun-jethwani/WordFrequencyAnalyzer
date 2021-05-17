"""
This module contains class which defines parameterized methods to
test methods of IWordFrequency class

"""
import pytest

# TEST_DATA_2 is a dictionary of test data constants
# needed for this module
from tests.test_data.inputs import TEST_DATA_2


# sends arguments to 'result_tester' fixture
# defined in conftest.py
@pytest.mark.parametrize(
    "result_tester",
    TEST_DATA_2["WORD_FREQUENCY_PAIR"],
    indirect=["result_tester"],
)
def test_word_frequency(result_tester):
    """
    compares result of the method caluclate_highest_frequency
    with the actual result

    Parameters
    ----------
    result_tester : value obtained through text fixture
                    defined in conftest.py

    """
    assert result_tester[0] == TEST_DATA_2["WORD_3"]
    assert result_tester[1] == TEST_DATA_2["FREQUENCY_1"]


@pytest.mark.parametrize(
    "result_tester",
    TEST_DATA_2["NON_STR_WORD_PAIRS"],
    indirect=["result_tester"],
)
def test_word_is_str(result_tester):
    """
    if word is not of type <str> assert exception message
    with actual value

    Parameters
    ----------
    result_tester : value obtained through text fixture
                    defined in conftest.py

    """
    assert result_tester == TEST_DATA_2["WORD_TYPE_ERROR"]


@pytest.mark.parametrize(
    "result_tester",
    TEST_DATA_2["NON_ALPHA_NON_LOWER_CASE_PAIRS"],
    indirect=["result_tester"],
)
def test_word_is_lower_case_alphabetic(result_tester):
    """
    if word is not all lower case, assert exception
    message with actual value

    Parameters
    ----------
    result_tester : value obtained through text fixture
                    defined in conftest.py

    """
    assert result_tester == TEST_DATA_2["LOWER_CASE_CONDITION"]


@pytest.mark.parametrize(
    "result_tester",
    TEST_DATA_2["NON_INT_FREQUENCY_PAIRS"],
    indirect=["result_tester"],
)
def test_frequency_is_integer(result_tester):
    """
    if frequency is not of type <int>, assert
    exception message with actual value

    Parameters
    ----------
    result_tester : value obtained through text fixture
                    defined in conftest.py

    """
    assert result_tester == TEST_DATA_2["FREQUENCY_TYPE_ERROR"]


@pytest.mark.parametrize(
    "result_tester",
    TEST_DATA_2["INVALID_FREQUENCY_PAIRS"],
    indirect=["result_tester"],
)
def test_frequency_is_valid(result_tester):
    """
    if value of frequency is invalid i.e 0, assert
    exception message with actual value

    Parameters
    ----------
    result_tester : value obtained through text fixture
                    defined in conftest.py

    """
    assert result_tester == TEST_DATA_2["INVALID_FREQUENCY"]
