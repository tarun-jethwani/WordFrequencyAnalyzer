# Python Coding Assignment

## Usage

This projects supports two user interaction interfaces 
- ### ```main.py``` runs on command prompt, 
1. first it will display options for functions
2. will prompt user to enter choice, enter number from available options
3. will prompt user to enter arguments, enter arguments for the function
4. will execute function and display final result

- ### ```app.py``` a flask application 
1. after running app.py , flask application is hosted on localhost (127.0.0.1) and port number 5000
2. app supports only 3 url routes for 3 different functions, text refers to input text, 
   word refers to the group of alphabetic chars for which frequency has to be found from text, 
   n : number of most common words from text to be found, user can use url via browser or any 
   request package
    * ```127.0.0.1:5000/calculate_highest_frequency/<text>``` for getting the highest frequency from the text
      - try example ```127.0.0.1:5000/calculate_highest_frequency/The sun shines over the lake```
    * ```127.0.0.1:5000/calculate_frequency_for_word/<text>/<word>``` for getting the frequency for the word from given text
      - try example ```127.0.0.1:5000/calculate_frequency_for_word/The sun shines over the lake/lake```
    * ```127.0.0.1:5000/calculate_most_frequent_n_words/<text>/<n>``` for getting the most frequent n words
      - try example ```127.0.0.1:5000/calculate_most_frequent_n_words/The sun shines over the lake/3```
   
3. user will get appropriate string response as a result after using any of the above mentioned route

### Required Classes
IWordFrequency and IWordFrequencyAnalyzer are defined in src/iword_frequency.py

## Run Tests
Pytest is used for testing class methods, to run Pytest, please keep the code files mimicking the directory structure
mentioned below
```
# run following command in project directory 
python -m pytest 
```

## Directory Structure
```
RaboCodingAssignment
├── logs # will be created automatically 
├── src  # python package
│   ├── utils # python package to contain utility modules
│   │   ├── __init__.py   # to make directory into package
│   │   ├── config.py     # contains configuration control variables for logs
│   │   ├── log_utils.py  # defines logger for entire app
│   │   ├── main_utils.py # contains utility functions used indirectly by main.py
│   │   └── text_utils.py # contains utility functions to process text
│   │
│   ├── __init__.py        # to make directory into package
│   ├── constant.py        # holds constants
│   ├── iword_frequency.py # contains IWordFrequency and IWordFrequencyAnalyzer classes
│   └── iword_frequency_executor.py # contains Executor class to execute 
│                                   # IWordFrequencyAnalyzer functions
│    
├── tests # test directory 
│   ├── test_data  # python package
│   │   ├── __init__.py  # to make directory into package
│   │   └── inputs.py    # contains test_inputs
│   │  
│   ├── __init__.py
│   ├── conftest.py  # contains text fixtures   
│   ├── test_flask_app.py  # to test flask app
│   ├── test_iword_frequency.py  # to test IWordFrequency class
│   └── test_iword_frequency_analyzer.py # to test IWordFrequencyAnalyzer class
│
├── __init__.py 
├── app.py  # contains flask app
├── main.py # command prompt interface for user
└── README.md
```

### Logs 
- to turn on/off debug logs use control switch ```DEBUG_CONTROL = True/False ``` in src/utils/config.py 
- to turn on/off all logs use ```LOG_MODE = True/False``` in src/utils/config.py

### Use of 3rd Party Python Libraries 
- Flask 1.1.2
- pytest 6.2.3

### Note :
- Please mimic folder/files structure as given in above directory_structure
- python 3.7 and above is used for developing this project