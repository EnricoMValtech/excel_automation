# excel_automation
The code in this repository aims to automate the tedious task of importing screamingFrog results in excel files.

A script bat is defined that starts screamingFrog and saves the results in a folder defined by the variable "results".
The script is based on https://opensourceseo.org/automating-screaming-frog-using-batch-scripts/.

Please make sure that the script.bat file is
You can double click on the script.bat to make it run.

Then a python script
1) merge the resulting csv files from screaming frog into a xlsx file with multiple sheets (one per csv file)
2) appends the resulting xlsx file in another xlsx file
To run the script py .\automate_user_input.py

TODO:
- make the process fully automated by starting the python script from the script.bat
