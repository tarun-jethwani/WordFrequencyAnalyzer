from collections import Counter
from itertools import starmap
from typing import List

from .utils.log_utils import logger
from .utils.text_utils import find_words


class IWordFrequency:
    """ Class to track occurrence of word and its frequency

    Attributes
    ----------
    word : str
        a word is a sequence of one or more
        characters between a and z
    frequency : int
        count of word occurrences
    """

    def __init__(self, word: str, frequency: int):
        """ initialises word and its frequency

        Parameters
        ----------
        word : str
            a word is a sequence of one or more
            characters between a and z
        frequency : int
            count of word occurrences
        """
        # Validation before instance variables are assigned values
        # if method validate_params() raises error,
        # instance variables are not assigned values
        self.__word, self.__frequency = self.validate_params(word, frequency)
        logger.debug("IWordFrequency initialised")

    # getters for read only attributes
    # absence of @{attribute_name}.setter
    # makes the attribute read-only

    @property
    def word(self) -> str:
        """str: word of the instance referenced by self"""
        logger.debug(f"get word attribute of IWordFrequency {self.__word}")
        return self.__word

    @property
    def frequency(self) -> int:
        """int: frequency of the word of the instance referenced by self"""
        logger.debug(f"get frequency attribute of IWordFrequency"
                     f" {self.__frequency}")
        return self.__frequency

    def validate_params(self, word: str, frequency: int) -> tuple:
        """
        performs validation for input parameters
        word and str, its necessary step before initialising
        instance variables

        Parameters
        ----------
        word : str
            a word is a sequence of one or more
            characters between a and z
        frequency : int
            count of word occurrences
        Returns
        -------
            : tuple -> (str, int) i.e (word, frequency) pair
        """
        # some initial checks
        if not isinstance(word, str):
            raise TypeError("word should be string")
        # enforcing word with all lower case chars between [a-z]
        if not word.isalpha() or not word.islower():
            raise ValueError("word should contain only chars from [a-z]")
        if not isinstance(frequency, int):
            raise TypeError("frequency should be integer")
        if frequency < 1:
            raise ValueError("Cannot create instance for "
                             "word which does not occur")

        return word, frequency


class IWordFrequencyAnalyzer:
    """ A class to perform word-frequency operations, does
    not require instance variables
    """

    def calculate_highest_frequency(self, text: str) -> int:
        """
        Calculate most number of occurrences of all the words
        present in input text, a word is group of alphabetic characters,
        all lower case[ a-z ]

        Parameters
        ----------
        text : str
            input text contains words separated by various special characters

        Returns
        -------
        int
            highest frequency in the text

        """
        logger.debug(f"received text : {text} as parameter")
        if not isinstance(text, str):
            logger.debug("TypeError : text should be string")
            raise TypeError("text should be string")
        if len(text.strip()) == 0:
            logger.debug("ValueError : text is empty")
            raise ValueError("text is empty")
        all_words = find_words(text)
        n_counter = Counter(all_words)
        # c.most_common(1) returns list of tuples [('a', 5), ('b', 4)]
        # using successive indexing to access highest frequency
        highest_frequency = n_counter.most_common(1)[0][1]
        logger.info(f"highest frequency : {highest_frequency}")
        return highest_frequency

    def calculate_frequency_for_word(self, text: str, word: str) -> int:
        """
        calculates frequency of the given word from the text

        Parameters
        ----------
        text : str
            input text contains words separated by various special characters
        word : str
            group of characters[a-z], all lower case

        Returns
        -------
        int
            frequency of the given word present in the input text
            0 if word is not present

        """
        logger.debug(f"received text : {text} and word : {word} as parameters")
        if not isinstance(text, str):
            logger.debug("TypeError : text should be string")
            raise TypeError("text should be string")
        if not isinstance(word, str):
            logger.debug("TypeError : word should be string")
            raise TypeError("word should be string")
        # if string is empty or just contains whitespaces
        if len(text.strip()) == 0:
            logger.debug("ValueError : text is empty")
            raise ValueError("text is empty")
        # if word is empty or just contains whitespaces
        if len(word.strip()) == 0:
            logger.debug("ValueError : word is empty")
            raise ValueError("word is empty")

        all_words = find_words(text)
        # word.lower() for case insensitive occurrences
        word_count = all_words.count(word.lower())
        logger.info(f"count of {word} in {text} is {word_count}")
        return word_count

    def calculate_most_frequent_n_words(self, text: str,
                                        n: int) -> List:
        """
        calculates n most frequent words out of all the word present in
        input text, by comparing all the instances of word,frequency pairs

        Parameters
        ----------
        text : str
            input text contains words separated by various special characters
        n : int
            number of most common words

        Returns
        -------
        List
            of tuples, every tuple is pair of (word, frequency) -> (str, int)
        """
        logger.debug(f"received text : {text} and n : {n} as parameters")
        if not isinstance(text, str):
            logger.debug("TypeError : text should be string")
            raise TypeError("text should be string")
        if not isinstance(n, int):
            logger.debug("TypeError : pass integer for n")
            raise TypeError("pass integer for n")
        if len(text.strip()) == 0:
            logger.debug("ValueError : text is empty")
            raise ValueError("text is empty")
        if n < 1:
            logger.debug("ValueError : most frequent words should"
                         " be at least 1")
            raise ValueError("most frequent words should be at least 1")

        all_words = find_words(text)
        n_counter = Counter(sorted(all_words))
        # check whether n is greater than total words found
        if n > len(n_counter):
            raise ValueError("n exceeds the total number of unique words")

        # creating an iterator of IWordFrequency instances
        iter_list = starmap(IWordFrequency, n_counter.most_common(n))

        # creating list of tuples of word, frequency
        # by fetching word and frequency of each item from iterator
        word_frequency_list = [(item.word, item.frequency)
                               for item in iter_list]
        logger.info(f"list of word frequencies : {word_frequency_list}")
        return word_frequency_list
