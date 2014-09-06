import shlex

__author__ = 'Joshua Free'


def main():
    commands = ['pwd', 'cd', 'ls', 'rls', 'tree', 'clear', 'create', 'add', 'cat', 'delete', 'dd', 'quit']

    while True:
        arg = input('ffs> ')
        split_arg = string_to_list(arg)

        if split_arg[0] == commands[0]:
            execute_pwd()
        elif split_arg[0] == commands[1]:
            execute_cd()
        elif split_arg[0] == commands[2]:
            execute_ls()
        elif split_arg[0] == commands[3]:
            execute_rls()
        elif split_arg[0] == commands[4]:
            execute_tree()
        elif split_arg[0] == commands[5]:
            execute_clear()
        elif split_arg[0] == commands[6]:
            execute_create()
        elif split_arg[0] == commands[7]:
            execute_add()
        elif split_arg[0] == commands[8]:
            execute_cat()
        elif split_arg[0] == commands[9]:
            execute_delete()
        elif split_arg[0] == commands[10]:
            execute_dd()
        elif split_arg[0] == commands[11]:
            execute_quit()
        else:
            print('Input is not a recognised command')


def execute_pwd():
    # TODO: execute PWD
    print('pwd')


def execute_cd():
    # TODO: execute CD
    print('cd')


def execute_ls():
    # TODO: execute LS
    print('ls')


def execute_rls():
    # TODO: execute RLS
    print('rls')


def execute_tree():
    # TODO: execute tree
    print('tree')


def execute_clear():
    # TODO: execute clear
    print('clear')


def execute_create():
    # TODO: execute create
    print('create')


def execute_add():
    # TODO: execute add
    print('add')


def execute_cat():
    # TODO: execute cat
    print('cat')


def execute_delete():
    # TODO: execute delete
    print('delete')


def execute_dd():
    # TODO: execute dd
    print('dd')


def execute_quit():
    quit()


def string_to_list(line):
    lexer = shlex.shlex(line, posix=True)
    lexer.whitespace_split = False
    lexer.wordchars += '#$+-,./?@^='
    args = list(lexer)
    return args


if __name__ == '__main__':
    main()