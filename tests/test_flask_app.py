""" this module contains test functions to test flask app client url routes """
# load url constants
from tests.test_data.inputs import (
    URL_ERROR_FREQUENCY_FOR_WORD,
    URL_ERROR_HIGHEST_FREQUENCY,
    URL_ERROR_MOST_FREQUENT_WORDS,
    URL_FREQUENCY_FOR_WORD,
    URL_HIGHEST_FREQUENCY,
    URL_MOST_FREQUENT_N_WORDS,
)


# client argument is received from text fixture
def test_highest_frequency(client):
    """
    invokes get request from
    url route /calculate_highest_frequency/<text>/

    Parameters
    ----------
    client : instance of flask client

    """
    response = client.get(URL_HIGHEST_FREQUENCY)
    # decode bytes data before asserting
    assert int(response.data.decode("utf-8")[-1]) == 2


def test_frequency_for_word(client):
    """
    invokes get request from
    url route /calculate_frequency_for_word/<text>/<word>

    Parameters
    ----------
    client : instance of flask client

    """
    response = client.get(URL_FREQUENCY_FOR_WORD)
    # decode bytes data before asserting
    assert int(response.data.decode("utf-8")[-1]) == 1


def test_most_frequent_n_words(client):
    """
    invokes get request from
    url route /calculate_most_frequent_n_words/<text>/<n>

    Parameters
    ----------
    client : instance of flask client

    """
    response = client.get(URL_MOST_FREQUENT_N_WORDS)
    output = response.data.decode("utf-8").split("are ")
    assert str([("the", 2), ("lake", 1)]) == output[1]


def test_error_in_highest_frequency(client):
    """
    negative test, tests invalid url route
     /calculate_highest_frequency/<number>/

    Parameters
    ----------
    client : instance of flask client

    """
    response = client.get(URL_ERROR_HIGHEST_FREQUENCY)
    # decode bytes data before asserting
    error_type = response.data.decode("utf-8").split(" :")[0]
    assert error_type == "ValueError"


def test_error_in_frequency_for_word(client):
    """
    negative test, tests invalid url route
     /calculate_frequency_for_word/<number>/<word>

    Parameters
    ----------
    client : instance of flask client

    """
    response = client.get(URL_ERROR_FREQUENCY_FOR_WORD)
    # decode bytes data before asserting
    error_type = response.data.decode("utf-8").split(" :")[0]
    assert error_type == "ValueError"


def test_error_in_most_frequent_words(client):
    """
    negative test, tests invalid url route
     /calculate_most_frequent_n_words/<text>/<word>

    Parameters
    ----------
    client : instance of flask client

    """
    response = client.get(URL_ERROR_MOST_FREQUENT_WORDS)
    # decode bytes data before asserting
    error_type = response.data.decode("utf-8").split(" :")[0]
    assert error_type == "ValueError"
