"""
This module provides class description to
execute IWordFrequencyAnalyzer functions

"""
from .utils.log_utils import logger
from .utils.main_utils import get_exception_message


class IWordFrequencyExecutor:
    """This class is responsible to get option from user, arguments from user
     and execute, appropriate function as selected by user

     Attributes
    ----------
    options_map : dict
        dictionary of mapping integer to appropriate
        functions and its arguments

    user_option : int
        as selected by user after seeing options
        user_option is used as key to index options_map
        for corresponding function

    message : str
        contains final message received from the appropriate
        executor functions
    """

    def __init__(self, options_map):
        """
        initialises options map

        Parameters
        ----------
        options_map : dict
            dictionary of mapping integer to appropriate
            functions and its arguments
        """
        self.options_map = options_map
        # keeping instance variables None at the start
        self.user_option = None
        self.message = None
        logger.debug("IWordFrequencyExecutor initialised")

    def get_option_from_user(self):
        """
        it loops over all the keys of options_map
        and displays key and function names
        and prompts user to enter option
        choice
        """
        logger.info("displays option map to user")
        for k, v in self.options_map.items():
            print(k, v['name'])

        self.user_option = int(input("Enter your option\t"))
        logger.info(f"received user option {self.user_option}")

        if self.user_option not in self.options_map.keys():
            logger.debug("Invalid Option, select among [1,2,3]")
            raise ValueError("Invalid Option, select among [1,2,3]")

    def get_function_arguments(self):
        """
        it uses received option_choice from user as key
        to fetch arguments/parameters for the function
        at the corresponding key of the options_map
        """
        print(f"Enter Arguments for "
              f"{self.options_map[self.user_option]['name']}")
        for param in self.options_map[self.user_option]['params'].keys():
            value = input(f"Enter {param}\t")
            self.options_map[self.user_option]['params'][param] = value
            logger.info(f"received value of {param} is {value}")
        return self.options_map

    def execute_function(self):
        """
        finally after receiving option choice and function parameters
        from user its executes appropriate function at the corresponding
        key of the options_map
        """
        try:
            # exception can occur while executing these functions
            self.message = self.options_map[self.user_option]['func_name'](
                self.options_map[self.user_option]['params'])
            logger.info(self.message)

        except (ValueError, TypeError) as e:
            # if exception occurs send exception message as
            # final message back to user
            self.message = get_exception_message(e)
            logger.exception(self.message)

        # execute reset method is the last step
        # of the function
        self.reset_options_map()

    def reset_options_map(self):
        """
        make function arguments value None again
        to bring back to original form, it is easier for testing
        complete execution of one round of user interaction and
        options map has to be reset for next round
        """
        for param in self.options_map[self.user_option]['params'].keys():
            self.options_map[self.user_option]['params'][param] = None
        logger.debug("options map is reset")
