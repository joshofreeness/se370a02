import shlex
import os
from subprocess import call
import shutil
import re

__author__ = 'Joshua Free'

current_dir = '-'


def main():
    commands = ['pwd', 'cd', 'ls', 'rls', 'tree', 'clear', 'create', 'add', 'cat', 'delete', 'dd', 'quit']

    #Create A2dir if does not exist
    if not os.path.exists('A2dir'):
        os.makedirs('A2dir')

    #Change into A2dir
    os.chdir("A2dir")

    while True:
        arg = input('ffs> ')
        split_arg = string_to_list(arg)

        if split_arg[0] == commands[0]:
            execute_pwd()
        elif split_arg[0] == commands[1]:
            execute_cd(split_arg)
        elif split_arg[0] == commands[2]:
            execute_ls()
        elif split_arg[0] == commands[3]:
            execute_rls()
        elif split_arg[0] == commands[4]:
            execute_tree()
        elif split_arg[0] == commands[5]:
            execute_clear()
        elif split_arg[0] == commands[6]:
            execute_create(split_arg)
        elif split_arg[0] == commands[7]:
            execute_add()
        elif split_arg[0] == commands[8]:
            execute_cat()
        elif split_arg[0] == commands[9]:
            execute_delete(split_arg)
        elif split_arg[0] == commands[10]:
            execute_dd()
        elif split_arg[0] == commands[11]:
            execute_quit()
        else:
            print('Input is not a recognised command')


def execute_pwd():
    print(current_dir)


def execute_cd(args):
    temp_dir = current_dir
    global current_dir
    if len(args) == 1:
        temp_dir = '-'
    elif args[1] == '..':
        if len(current_dir) == 1:
            pass
        else:
            dashes = [i.start() for i in re.finditer('-', current_dir)]
            remove_char = dashes[-2]
            temp_dir = temp_dir[:(remove_char - len(current_dir))]
            temp_dir += '-'
    elif args[1][0] == '-':
        if args[1][-1] != '-':
            args[1] += '-'
        temp_dir = args[1]
    else:
        if args[1][-1] != '-':
            args[1] += '-'
        temp_dir = temp_dir + args[1]

    if find_folder(temp_dir):
        current_dir = temp_dir
    else:
        print('No such directory')


def execute_ls():
    # TODO: execute LS
    print('ls')


def execute_rls():
    call(['ls','-l'])


def execute_tree():
    # TODO: execute tree
    print('tree')


def execute_clear():
    # TODO: execute clear
    os.chdir('..')
    shutil.rmtree('A2dir')
    #Create A2dir if does not exist
    if not os.path.exists('A2dir'):
        os.makedirs('A2dir')
    #Change into A2dir
    os.chdir("A2dir")


def execute_create(args):
    if len(args) == 1:
        print('No file name')
        return
    elif args[1][-1] == '-':
        print("Invalid file name")
        return
    elif args[1][0] == '-':
        call(['touch', './'+args[1]])
    else:
        file_name = current_dir + args[1]
        call(['touch', './'+file_name])


def execute_add():
    # TODO: execute add
    print('add')


def execute_cat():
    # TODO: execute cat
    print('cat')


def execute_delete(args):
    if len(args) == 1:
        print('No file name')
        return
    elif args[1][-1] == '-':
        print("Invalid file name")
        return
    elif args[1][0] == '-':
        if find_file(args[1]):
            os.remove(args[1])
        else:
            print('No such file')
            return
    else:
        file_name = current_dir + args[1]
        if find_file(file_name):
            os.remove(file_name)
        else:
            print('No such file')
            return



def execute_dd():
    # TODO: execute dd
    print('dd')


def execute_quit():
    os.chdir('..')
    quit()


def find_file(full_file_name):
    return os.path.isfile(full_file_name)


def find_folder(full_folder_name):
    files = os.listdir('.')
    return any(full_folder_name in file for file in files)


def string_to_list(line):
    lexer = shlex.shlex(line, posix=True)
    lexer.whitespace_split = False
    lexer.wordchars += '#$+-,./?@^='
    args = list(lexer)
    return args


if __name__ == '__main__':
    main()