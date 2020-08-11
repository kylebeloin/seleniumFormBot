## Macro-enabled Excel Sheet: Python Bot that Automates Webform

## MACRO: ctr+shift+P

## This program:

-Takes input from hard-coded fields in a preconfigured, macro-enabled, Excel workbook ('myproject.xlsm').

-Matches the column names to text-fields by xpath. 

-Automates the fill and submission of each new row in the workbook.

    ***Submission line is commented out to avoid spamming SLATE database***
    
-Recognizes whether a workbook has been updated.

    ***Does not distinguish which values are NEW/OLD--only that the book has changed***

----------------------------------------------------------------------------------------------

### 1. Install python3 dependencies:

With python3 and pip installed, navigate to the project folder in terminal.

To install dependencies, run: pip install -r requirements.txt

***NOTE: If you encounter errors, you may need to use 'pip3' instead of 'pip'***


### 2. Install add-in:

To install the add-in, it’s easiest to use the command line client: xlwings addin install.

***NOTE: Excel might need to be open on a new work book for this command to run without error.***

in:     

        $ xlwings addin install


out:    

        Successfully installed the xlwings add-in! Please restart Excel.
        
        Successfully enabled RunPython!

After installing, restart Excel. You should see a new navigation tab labeled "xlwings."


### 3. Configure "myproject.xlsm":

In "myproject.xlsm," navigate to the sheet labeled "xlwings.conf," and locate the path to the python interpreter where the above dependencies in "requirements.txt" are installed. 

***NOTE: Should have python 3.8.5 and pip installed. See: https://docs.python-guide.org/starting/install3/osx/***

Default path should be: /usr/local/bin/python3

Paste the path to the cell next to the corresponding operating system.


### 4. Initialize cache files:

Because this program is intended to recognize changes in an existing workbook, you must run the macro once to establish a baseline. 

***NOTE: Check that there are no files in the folder labeled 'cache' before running for the first time.***

When you the see, Error "Exception: No new additions! Enter a new entry and then run macro.", cache has been initialized and is ready for new input. 
