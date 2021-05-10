"""
this module provides web interface using flask app to execute
IWordFrequencyAnalyzer class functions via url routes

"""
from flask import Flask
from src.iword_frequency import IWordFrequencyAnalyzer
from src.utils.main_utils import get_exception_message
from src.utils.log_utils import logger


def create_app():
    """
    creates flask app defines functions to handle different url routes
    each function is responsible for executing different function of
    IWordFrequencyAnalyzer class

    Returns
    -------
    instance of flask app
    """

    flask_app = Flask(__name__)
    logger.debug("Flask app is initialized")
    word_frequency_analyzer = IWordFrequencyAnalyzer()
    logger.debug("IWordFrequencyAnalyzer instance is created")

    # handle non-existent/invalid url routes
    @flask_app.errorhandler(404)
    def page_not_found(e):
        logger.debug(get_exception_message(e))
        return "given url route does not exist, or is invalid"

    # to calculate highest frequency
    @flask_app.route("/calculate_highest_frequency/<text>/",
                     methods=['GET', 'POST'])
    def highest_frequency(text):
        """
        receives text from url request and executes
        calculate_highest_frequency() function of
        IWordFrequencyAnalyzer class

        Parameters
        ----------
        text : str
            input text received from user

        Returns
        -------
            : str
            final message for the user

        """
        try:
            # ValueError can occur
            result = word_frequency_analyzer.calculate_highest_frequency(text)
            logger.info(result)
            return f"Highest Frequency in the given text is {result}"
        except ValueError as e:
            message = get_exception_message(e)
            logger.exception(message)
            return message

    # to calculate frequency for word
    @flask_app.route("/calculate_frequency_for_word/<text>/<word>",
                     methods=['GET', 'POST'])
    def calculate_frequency_for_word(text, word):
        """
        receives text and word from url request and executes
        calculate_frequency_for_word() function of
        IWordFrequencyAnalyzer class

        Parameters
        ----------
        text : str
            input text received from user
        word : str
            word for which frequency has to be found

        Returns
        -------
            : str
            final message for user

        """
        try:
            # ValueError can occur
            result = word_frequency_analyzer. \
                calculate_frequency_for_word(text, word)
            logger.info("result")
            return f"Frequency for the {word} in the given text is {result}"
        except ValueError as e:
            message = get_exception_message(e)
            logger.exception(message)
            return message

    @flask_app.route("/calculate_most_frequent_n_words/<text>/<n>",
                     methods=['GET', 'POST'])
    def calculate_most_frequent_n_words(text, n):
        """
        receives text and n(number in form of string) from url request
        and executes calculate_most_frequent_n_words() function of
        IWordFrequencyAnalyzer class

        Parameters
        ----------
        text : str
            input text received from user
        n : str
            number of words to be found which are most common

        Returns
        -------
            : str
            final message for the user

        """
        # convert from str to int
        try:
            # ValueError can occur
            n = int(n)
            result = word_frequency_analyzer. \
                calculate_most_frequent_n_words(text, n)
            logger.info(result)
            return f"Most frequent {n} words are {result}"
        except ValueError as e:
            message = get_exception_message(e)
            logger.exception(message)
            return message

    return flask_app


if __name__ == "__main__":
    app = create_app()
    app.run()
    logger.info("Flask app running on localhost - port 5000")
