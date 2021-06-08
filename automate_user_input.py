from module.osModule import get_most_updated_subfolder, get_all_files_name
from module.excelFileModule import aggregate_csv_files, merge_excel_files
from module.installer import check_packages
import datetime as dt
import tkinter as tk
from tkinter import filedialog

from tkinter.filedialog import askopenfilename
print('checking packages')
check_packages()

# returns the todays date as 06-07-2021 (month-day-year)
today = dt.date.today().strftime("%m-%d-%Y")
# define main directory

root = tk.Tk()
root.withdraw()

all_files = []
file_directory = ""
ex = input('1 or 2')
if ex == '1':
    while not all_files and not file_directory:
        file_directory = filedialog.askdirectory()

        # file_directory = "D:\crawls\Test1"

        # get working directory
        if not file_directory:
            answer = input(
                'are you sure you want to exit? please type Y or N\n')
            print()
            if answer == 'N':
                continue
            else:
                exit()
        print(f'you selected {file_directory}')
        working_directory = get_most_updated_subfolder(today, file_directory)

        # get all the files in a directory given an extension
        all_files = get_all_files_name(working_directory, "csv")

        if not all_files:
            print(
                f'folder {working_directory} does not contain files with that extension')

        else:
            # combine each csv file in a sheet of an xlsx file

            output_file = input("Enter output file:")

            if output_file[:-4] == ".xlsx":
                aggregate_csv_files(output_file, all_files)
            else:
                aggregate_csv_files(output_file+".xlsx", all_files)


else:
    print('select a file where to append the data')
    main_file = askopenfilename()
    print('select a file that contains the data to be appended')
    file_to_merge = askopenfilename()
    merge_excel_files(main_file, file_to_merge)
