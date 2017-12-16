import datetime
import os
import shutil


def get_files_list(txtfile):
    """""read in a txt list of files into a python list"""

    # make an empty list to store file names to move to the destination folder
    files_list = []

    # read files into the python list
    with open(txtfile, 'r') as f:
        for line in f:
            files_list.append(line.rstrip())

    return files_list


def move_files(files_to_move, target_folder):
    """"move a list of files to the specified folder"""

    # create a blank dictionary to track whether files were successfully moved
    file_operation_results = {}

    # attempt to move each file in the list and track each success or failure in the dictionary
    for file in files_to_move:
        if os.path.exists(file):
            shutil.move(file, target_folder + os.path.split(file)[1])
            file_operation_results[file] = True
        else:
            file_operation_results[file] = False

    display_results("Move", file_operation_results)
    output_file_operations_log("Move", file_operation_results)

def display_results(file_operation_performed, file_operation_results):
    """"shows number of files successfully operated on to the user in the command line interface"""

    print("{} file operation successful for {} of {} file(s)".format(
        file_operation_performed,
        list(file_operation_results.values()).count(True),
        len(file_operation_results.keys())))


def output_file_operations_log(file_operation_performed, file_operation_results):
    """"generates a txt file to specifically show the user which files were successfully operated on and which failed"""

    # determine the date and time the log entry will be made at
    now = datetime.datetime.now()

    with open("file_ops.log", 'a') as f:
        f.write(now.strftime("%Y-%m-%d %H:%M:%S") + " " + file_operation_performed + " file operation performed.\n\n")
        f.write("Success:\n")
        for key, value in file_operation_results.items():
            if value == True: f.write(key + "\n")
        f.write("\nFailure:\n")
        for key, value in file_operation_results.items():
            if value == False: f.write(key + "\n")
        f.write("\n\n")
        f.close()


path_files_list = 'C:\\Matt\'s Files\\Python\\FileOps\\fileslist.txt'
target_folder = 'D:\\Destination\\'
files_list = get_files_list(path_files_list)
move_files(files_list, target_folder)