import os


def get_most_updated_subfolder(today, working_directory):
    # os.chdir(workingDirectory)
    # get all the subfolders given a project name
    list_subfolders_with_paths = [
        f.path for f in os.scandir(working_directory) if f.is_dir() and today in f.name]
    # get the most recent folder based on date
    if list_subfolders_with_paths:
        most_recent_subfolder = list_subfolders_with_paths[-1]
        return most_recent_subfolder
    return working_directory


def get_all_files_name(most_recent_subfolder, extension):
    if most_recent_subfolder:
        # # set working directory
        os.chdir(most_recent_subfolder)
        # find all csv files in the folder
        # use glob pattern matching -> extension = 'csv'
        # save result in list -> all_filenames
        return [i for i in os.listdir(
            most_recent_subfolder) if i.endswith(extension)]
