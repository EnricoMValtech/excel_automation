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


def merge_excel_files2(main_file, file_to_merge):
    if main_file and file_to_merge:
        # xl_main_sheets = pd.ExcelFile(main_file).sheet_names
        # xl_to_merge_sheets = pd.ExcelFile(file_to_merge).sheet_names
        # # open the excel writer in append mode
        # appender = pd.ExcelWriter(main_file, mode='a')
        # for s_main in xl_main_sheets:
        #     for s_to_merge in xl_to_merge_sheets:
        #         if s_main == s_to_merge:
        #             print(s_main)

        # appender.save()
        # appender.close()
        # load all the sheets from an excel file inside a dataframe {sheet_name:dataframe}
        #  for k in df_to_merge.keys():
        # for s in df_to_merge[k]:
        #     for d in df_to_merge[k][s]:
        #         # if df_to_merge[k][s].startswith('http'):
        #         if isinstance(d, str) and d.startswith('http'):
        #             print('bah')
        #             print(d)
        frames = {}
        df_main = pd.read_excel(main_file, index_col=0, sheet_name=None)
        df_to_merge = pd.read_excel(
            file_to_merge, index_col=0, sheet_name=None,)
        for k in df_to_merge.keys():
            for km in df_main.keys():
                if k == km:
                    frames[k] = df_main[k].append(df_to_merge[k])
        appender = pd.ExcelWriter(main_file, mode='a', engine="openpyxl")
        for k in frames.keys():
            print(k)
            df = pd.DataFrame(data=frames[k])
            print(df)
            df.to_excel(appender, sheet_name=k, index=False)
        appender.save()
        appender.close()

# based on https://gist.github.com/Trambadiya26Nensi/a31d186f1aba549b3fef0f7b55945e20#file-appenddata-py


def merge_excel_files(main_file, file_to_merge):
    writer = pd.ExcelWriter(main_file, engine='openpyxl')

    df_to_merge = pd.read_excel(
        file_to_merge, index_col=0, sheet_name=None,)

    # try to open an existing workbook
    writer.book = load_workbook(main_file)
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
