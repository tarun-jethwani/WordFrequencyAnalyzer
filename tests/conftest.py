"""
This module contains fixtures to provide test data to
all the tests during pytest run

"""
import pytest

from ..app import create_app
from ..src.iword_frequency import IWordFrequency, IWordFrequencyAnalyzer


@pytest.fixture(scope="module")
def client():
    """
    provides instance of the flask app to
    module test_flask_app.py

    yields
    -------
    instance of flask client
    """
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@pytest.fixture(scope="class")
def result_tester(request):
    """
    it creates instance of IWordFrequency Class by receiving
    parameters from parameterized tests

    Parameters
    ----------
    request : contains test data passed by tests calling this fixture

    Returns
    -------
    (word, frequency) : (str, int)
        word, frequency pairs of an instance of IWordFrequency class
        if error ( ValueError, TypeError) occurs it returns error
        message in string form

    """
    try:
        word_frequency = IWordFrequency(request.param[0], request.param[1])
        return word_frequency.word, word_frequency.frequency
    except (ValueError, TypeError) as e:
        return str(e)


@pytest.fixture(scope="session")
def params_highest_frequency(request):
    """
    initialises instance of IWordFrequencyAnalyzer class
    and fetches result of calculate_highest_frequency
    method with arguments received through parameterized tests

    Parameters
    ----------
    request :  contains test data passed by tests calling this fixture

    Returns
    -------
     tuple of calculated result and
     actual result (last parameter of request.params)
        calculated result is highest_frequency obtained from
        from calculate_highest_frequency method
        if error ( ValueError, TypeError ) occurs , it returns
        error message in string form

    """
    frequency_analyzer = IWordFrequencyAnalyzer()
    try:
        output = frequency_analyzer.calculate_highest_frequency(
            request.param[0]
        )
    except (ValueError, TypeError) as e:
        output = str(e)

    return output, request.param[1]


@pytest.fixture(scope="session")
def params_word_frequency(request):
    """
    initialises instance of IWordFrequencyAnalyzer class
    and fetches result of calculate_frequency_for_word
    method with arguments received through parameterized tests

    Parameters
    ----------
    request :  contains test data passed by tests calling this fixture

    Returns
    -------
    tuple of calculated result and
    actual result (last parameter of request.params)
        calculated result is frequency obtained of word
        obtained from calculate_frequency_for_word method
        if error ( ValueError, TypeError ) occurs , it returns
        error message in string form

    """
    frequency_analyzer = IWordFrequencyAnalyzer()
    try:
        output = frequency_analyzer.calculate_frequency_for_word(
            request.param[0], request.param[1]
        )
    except (ValueError, TypeError) as e:
        output = str(e)

    return output, request.param[2]


@pytest.fixture(scope="session")
def params_most_common(request):
    """
    initialises instance of IWordFrequencyAnalyzer class
    and fetches result of calculate_most_frequent_n_words
    method with arguments received through parameterized tests

    Parameters
    ----------
    request : contains test data passed by tests calling this fixture

    Returns
    -------
    tuple of calculated result and
    actual result (last parameter of request.params)
        calculated result is List of tuples (word, frequency)
        obtained from calculate_most_frequent_n_words method
        if error ( ValueError, TypeError ) occurs , it returns
        error message in string form

    """
    frequency_analyzer = IWordFrequencyAnalyzer()
    try:
        output = frequency_analyzer.calculate_most_frequent_n_words(
            request.param[0], request.param[1]
        )
    except (ValueError, TypeError) as e:
        output = str(e)

    return output, request.param[2]
