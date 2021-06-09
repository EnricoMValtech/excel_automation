import pandas as pd
from colorama import Fore, Style
from openpyxl import load_workbook


def aggregate_csv_files(file_name, all_filenames):
    if file_name and all_filenames:
        writer = pd.ExcelWriter(file_name)
    # each csv file has to go in a different sheet inside an xlsx file.
    # the name of the sheet is based on the the filename
        for f in all_filenames:
            tmp = pd.read_csv(f)
            # Excel workseet name must be <= 31 characters
            if len(f[:-4]) > 31:
                tmp.to_excel(writer, sheet_name=f[0:30], index=False)
                continue
            tmp.to_excel(writer, sheet_name=f[:-4], index=False)
        writer.save()
        print(Fore.GREEN + f'Success, file {file_name} has been created')
    else:
        print(
            Fore.RED + "Error, no file_name specified or no file found with that extension")
    print(Style.RESET_ALL)


# based on https://gist.github.com/Trambadiya26Nensi/a31d186f1aba549b3fef0f7b55945e20#file-appenddata-py


def merge_excel_files(main_file, file_to_merge):
    book = load_workbook(main_file)
    writer = pd.ExcelWriter(main_file, engine='openpyxl', mode='a')

    df_to_merge = pd.read_excel(
        file_to_merge, index_col=0, sheet_name=None,)

    # try to open an existing workbook
    writer.book = book
    # copy existing sheets
    writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
    # read existing file
    reader = pd.read_excel(main_file)

    for k in df_to_merge.keys():
        df = pd.DataFrame(data=df_to_merge[k])
        # write out the new sheet
        df.to_excel(writer, sheet_name=k, header=False,
                    startrow=len(reader)+1)
    writer.close()
    print(Fore.GREEN + f'Success, file {main_file} has been updated')
    print(Style.RESET_ALL)
