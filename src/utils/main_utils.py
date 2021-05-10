"""

This module provides execution functions which works as a wrapper over
IWordFrequencyAnalyzer functions, they receive dictionary parameters and
check for the existence of specific parameter before executing the final
function of IWordFrequencyAnalyzer class

"""
from src.iword_frequency import IWordFrequencyAnalyzer


# initialise instance of the IWordFrequencyAnalyzer class
analyzer = IWordFrequencyAnalyzer()


# function to create exception message
def get_exception_message(e):
    """

    Parameters
    ----------
    e : Exception object

    Returns
    -------
      : str
      Exception message
    """
    error_type = str(type(e)).split("'")[1]
    message = f"{error_type} : {e}"
    return message


def execute_highest_frequency(params: dict) -> str:
    """
    executes calculate_highest_frequency() of
    IWordFrequencyAnalyzer class

    Parameters
    ----------
    params : dict
        Parameters received from user

    Returns
    -------
        : str
     final message for user

    """

    if "text" in params:
        result = analyzer.calculate_highest_frequency(params['text'])
        return f"Highest Frequency in the given text is {result}"
    else:
        return "parameter insufficient"


def execute_frequency_for_word(params: dict) -> str:
    """
        executes calculate_frequency_for_word() of
        IWordFrequencyAnalyzer class

        Parameters
        ----------
        params : dict
            Parameters received from user

        Returns
        -------
            : str
         final message for user

        """

    if "text" in params and "word" in params:
        result = analyzer.calculate_frequency_for_word(params['text'],
                                                       params['word'])
        return f"Frequency for the {params['word']} in the " \
               f"given text is {result}"
    else:
        return "parameter insufficient"


def execute_most_frequent_n_words(params: dict) -> str:
    """
        executes calculate_most_frequent_n_words() of
        IWordFrequencyAnalyzer class

        Parameters
        ----------
        params : dict
            Parameters received from user

        Returns
        -------
            : str
         final message for user

    """

    if "text" in params and "n" in params:
        try:
            n = int(params["n"])
            result = analyzer.calculate_most_frequent_n_words(params['text'],
                                                              n)
            return f"Most frequent {params['n']} words are {result}"

        except (ValueError, TypeError) as e:
            return get_exception_message(e)
    else:
        return "parameter insufficient"


# function to create exception message

def get_exception_message(e):
    """

    Parameters
    ----------
    e : Exception object

    Returns
    -------
      : str
      Exception message
    """
    error_type = str(type(e)).split("'")[1]
    message = f"{error_type} : {e}"
    return message
