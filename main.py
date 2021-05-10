"""
This is main module provides interface for a user to interact with
rest of the application via command line prompts, seeking inputs from user

"""

# options map is mapping of function, function_name
# and its arguments with option value
from src.constants import OPTIONS_MAP
from src.iword_frequency_executor import IWordFrequencyExecutor
from src.utils.log_utils import logger
from src.utils.main_utils import get_exception_message

executor = IWordFrequencyExecutor(OPTIONS_MAP)

if __name__ == "__main__":

    logger.info("Command Prompt Interface")

    # loop to hold option interface for user
    while True:

        # displays options map to user
        # gets option choice from user
        try:
            # user might give invalid option
            executor.get_option_from_user()
        except ValueError as e:
            # print exception message, and continue
            user_message = get_exception_message(e)
            logger.exception(user_message)
            print(user_message, end="\n\n")
            continue

        # fetch functions arguments according
        # to the option choice selected by user
        executor.get_function_arguments()

        # execute appropriate function as selected
        # by user through option choice
        executor.execute_function()

        # Final Message for user
        print(executor.message, end="\n\n")
