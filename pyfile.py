import shlex
import os
import sys
from subprocess import call
import shutil
import re

__author__ = 'Joshua Free jfre553 2646577'

# This is a global string that represents the current directory, it is an absolute path(in terms of the program)
#It also  always has a "-" on the end
current_dir = '-'


def main():
    commands = ['pwd', 'cd', 'ls', 'rls', 'tree', 'clear', 'create', 'add', 'cat', 'delete', 'dd', 'quit']

    #Create A2dir if does not exist
    if not os.path.exists('A2dir'):
        os.makedirs('A2dir')

    #Change into A2dir
    os.chdir("A2dir")

    while True:
        redirected = not os.isatty(sys.stdin.fileno())

        if redirected:
            arg = sys.stdin.readline()
            print('ffs> ' + arg, end='')
            if not arg:
                exit()
        else:
            #Get argument/present prompt
            arg = input('ffs> ')
        #Split argument into an array of strings
        split_arg = string_to_list(arg)

        #Execute methods associated to built in commands
        if split_arg[0] == commands[0]:
            execute_pwd()  # implemented
        elif split_arg[0] == commands[1]:
            execute_cd(split_arg)  # implemented
        elif split_arg[0] == commands[2]:
            execute_ls(split_arg)
        elif split_arg[0] == commands[3]:
            execute_rls()  # implemented
        elif split_arg[0] == commands[4]:
            execute_tree()
        elif split_arg[0] == commands[5]:
            execute_clear()  # implemented
        elif split_arg[0] == commands[6]:
            execute_create(split_arg)  # implemented
        elif split_arg[0] == commands[7]:
            execute_add(split_arg)  # implemented
        elif split_arg[0] == commands[8]:
            execute_cat(split_arg)  # implemented
        elif split_arg[0] == commands[9]:
            execute_delete(split_arg)  # implemented
        elif split_arg[0] == commands[10]:
            execute_dd(split_arg)
        elif split_arg[0] == commands[11]:
            execute_quit()  # implemented
        else:
            print('Input is not a recognised command')


def execute_pwd():
    print(current_dir)


def execute_cd(args):
    #Get reference to the global variable of the current directory.
    global current_dir
    temp_dir = current_dir
    if len(args) == 1:
        #If no arguments
        temp_dir = '-'
    elif args[1] == '..':
        #If go up a directory
        if len(current_dir) == 1:
            pass
        else:
            #Find where all the dashes are in the pwd
            dashes = [i.start() for i in re.finditer('-', current_dir)]
            #Select the second to last dash
            remove_char = dashes[-2]
            #Cut the end off the string representing the current directory
            temp_dir = temp_dir[:(remove_char - len(current_dir))]
            #Reapped the end dash
            temp_dir += '-'
    elif args[1][0] == '-':
        #If an absolute path
        if args[1][-1] != '-':
            #If there is no dash on the end of the string, append it
            args[1] += '-'
        temp_dir = args[1]
    else:
        #If a relative path
        if args[1][-1] != '-':
            #If there is no dash on the end append it
            args[1] += '-'
        temp_dir = temp_dir + args[1]

    if find_folder(temp_dir):
        #If there is a folder by the name inputted then continue
        current_dir = temp_dir
    else:
        #Fail the cd command
        print('No such directory')


def execute_ls(args):
    full_folder_name = current_dir
    list_printed = []
    if len(args) == 1:
        #If only one input
        full_folder_name = current_dir
        contents = list_all_in_folder(full_folder_name)
        for thing in contents:
            thing = thing.replace(full_folder_name, '',1)
            if '-' in thing:
                thing = thing.split('-')[0]
                if thing in list_printed:
                    continue
                print("d: " + thing)
                list_printed.append(thing)
            else:
                print("f: " + thing)
                list_printed.append(thing)
    elif args[1][-1] != '-':
        #If no - at end add it.
        args[1] += '-'
    elif args[1][0] == '-':
        #If absolute path
        full_folder_name = args[1]
        if find_folder(full_folder_name):
            #If file exists then append
            contents = list_all_in_folder(full_folder_name)
            for thing in contents:
                thing = thing.replace(full_folder_name, '',1)
                if '-' in thing:
                    thing = thing.split('-')[0]
                    if thing in list_printed:
                        continue
                    print("d: " + thing)
                    list_printed.append(thing)
                else:
                    print("f: " + thing)
                    list_printed.append(thing)
        else:
            print('No such folder')
            return
    else:
        #If relative path, make absolute
        full_folder_name = current_dir + args[1]
        if find_folder(full_folder_name):
            #If file exists, append to it
            contents = list_all_in_folder(full_folder_name)
            for thing in contents:
                thing = thing.replace(full_folder_name, '',1)
                if '-' in thing:
                    thing = thing.split('-')[0]
                    if thing in list_printed:
                        continue
                    print("d: " + thing)
                    list_printed.append(thing)
                else:
                    print("f: " + thing)
                    list_printed.append(thing)
        else:
            print('No such folder')
            return


def execute_rls():
    call(['ls', '-l'])


def execute_tree():
    # TODO: execute tree
    print('tree')


def execute_clear():
    #Move up a directory
    os.chdir('..')
    #Delete the folder we were just in
    shutil.rmtree('A2dir')
    #Replace the folder
    #Create A2dir if does not exist
    if not os.path.exists('A2dir'):
        os.makedirs('A2dir')
    #Change into A2dir
    os.chdir("A2dir")


def execute_create(args):
    if len(args) == 1:
        #If only one input
        print('No file name')
        return
    elif args[1][-1] == '-':
        #If given directory rather than file
        print("Invalid file name")
        return
    elif args[1][0] == '-':
        #If absolute path
        call(['touch', './' + args[1]])
    else:
        #If relative path, then create absolute path by appending
        file_name = current_dir + args[1]
        call(['touch', './' + file_name])


def execute_add(args):
    if len(args) == 1:
        #If only one input
        print('No file name')
        return
    elif args[1][-1] == '-':
        #If given directory not file
        print("Invalid file name")
        return
    elif len(args) < 3:
        #If nothing was input to be added to file
        print("No text argument given")
        return
    elif args[1][0] == '-':
        #If absolute path
        if find_file(args[1]):
            #If file exists then append
            with open(args[1], "a") as my_file:
                my_file.write(" ".join(args[2:]))
        else:
            print('No such file')
            return
    else:
        #If relative path, make absolute
        file_name = current_dir + args[1]
        if find_file(file_name):
            #If file exists, append to it
            with open(file_name, "a") as my_file:
                my_file.write(" ".join(args[2:]))
        else:
            print('No such file')
            return


def execute_cat(args):
    if len(args) == 1:
        #Wrong number of inputs
        print('No file name')
        return
    elif args[1][-1] == '-':
        #If no - at end add it.
        args[1] += '-'
    elif args[1][0] == '-':
        #Absolute path
        if find_file(args[1]):
            with open(args[1], "r") as my_file:
                print(my_file.read())
        else:
            print('No such file')
            return
    else:
        #relative path
        file_name = current_dir + args[1]
        if find_file(file_name):
            with open(file_name, "r") as my_file:
                print(my_file.read())
        else:
            print('No such file')
            return


def execute_delete(args):
    if len(args) == 1:
        #If wrong input
        print('No file name')
        return
    elif args[1][-1] == '-':
        #If not file name
        print("Invalid file name")
        return
    elif args[1][0] == '-':
        #If absolute
        if find_file(args[1]):
            #If file exists, delete it
            os.remove(args[1])
        else:
            print('No such file')
            return
    else:
        #If relative
        file_name = current_dir + args[1]
        if find_file(file_name):
            #If file exists delete it
            os.remove(file_name)
        else:
            print('No such file')
            return


def execute_dd(args):
    # TODO : doesn't handle dd xx (for some reason the - at end isn't working) (then change for the rest)
    if len(args) == 1:
        #If wrong input
        print('No folder name')
        return
    elif args[1][-1] != '-':
        #If no - at end add it.
        print(args[1])
        args[1] += '-'
        print(args[1])
    elif args[1][0] == '-':
        #If absolute
        if find_folder(args[1]):
            #If older exists, delete it
            delete_folder(args[1])
        else:
            print('No such folder')
            return
    else:
        #If relative
        folder_name = current_dir + args[1]
        if find_folder(folder_name):
            #If folder exists delete it
            delete_folder(folder_name)
        else:
            print('No such folder')
            return


def execute_quit():
    #Go back to original directory
    os.chdir('..')
    quit()


def find_file(full_file_name):
    #Check if it is a file
    return os.path.isfile(full_file_name)


def find_folder(full_folder_name):
    #Check if string is a folder
    files = os.listdir('.')
    return any(full_folder_name in file for file in files)


def string_to_list(line):
    #Code given by lecturer for use in assignments
    lexer = shlex.shlex(line, posix=True)
    lexer.whitespace_split = False
    lexer.wordchars += '#$+-,./?@^='
    args = list(lexer)
    return args


def list_all_in_folder(full_folder_name):
    contents = os.listdir('.')
    final_list = []
    for file in contents:
        #If the folder name is longer than the file name
        if len(full_folder_name) >= len(file):
            #print(file + " less than " + full_folder_name)
            continue
        #If the folder name is not in the file name
        if full_folder_name not in file:
            #print(full_folder_name + " not in " + file)
            continue
        final_list.append(file)

    return final_list


def delete_folder(full_folder_name):
    #Get all file names
    folders = os.listdir('.')
    for folder in folders:
        #If the folder name is longer than the file name
        if len(full_folder_name) >= len(folder):
            #print(folder + " less than " + full_folder_name)
            continue
        #If the folder name is not in the file name
        if full_folder_name not in folder:
            #print(full_folder_name + " not in " + folder)
            continue
        os.remove(folder)


if __name__ == '__main__':
    main()