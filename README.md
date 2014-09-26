se360a02
========

A flat file System. Implemented so that "-" replaces "/". The program creates a real folder in the present working
directory called A2dir, which it then uses to store and create the flat file system. Storing only files and not
directories.

Commands include :



-- pwd
this displays the current ffs working directory


-- cd
change the current ffs working directory. No parameter means go back to the ffs root directory “-”. “cd ..” means
to revert to the ffs parent directory of the current directory. “cd name” means to change the ffs working directory
to name. If name starts with a “-” it is an absolute pathname. Otherwise it is relative to the working ffs directory.
The closing “-” on the directory name may be missing.


-- ls
list the files and directories in the named ffs directory. If no name is given use the current working ffs directory.
Uses the same rules for absolute and relative as cd. In the output files are indicated with “f: ” preceding their
names and directories are indicated with “d: ”.


-- rls
shows the output of the real “ls -l” command on the real A2dir directory


--tree
shows all files below this directory as an indented tree structure. Uses the same parameter rules as ls.


-- clear
removes all files in the ffs root directory. This is like “rm -rf /” in Unix (not a good idea).


-- create
creates a file with the specified name. The name must not end with a “-” otherwise it would be a directory and
we don’t create directories directly. The name can be either absolute, starting with a “-”, or relative to the
working ffs directory.


-- add
appends text to the named file. The first parameter is the filename, the next parameter is the text and consists
of the rest of the command line starting one space after the filename. The text is appended to the file. This is
 the only way to put data into a file. File names can be absolute or relative.
 
 
-- cat
 displays the contents of the named file. File names can be absolute or relative.
 
 
-- delete
deletes the named file. File names can be absolute or relative.


-- dd
deletes a directory (including all files and directories under this point). It doesn’t ask for confirmation.
The directory name can be absolute or relative.


-- quit
quits the A2com program.
