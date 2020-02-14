Able to edit two files

File 1 (whtielist.txt):
Ability to add or remove steam id's to file.
Ignore lines that start with semicolon
File has one steam id per line

e.g.
STEAM_1:0:21438005
STEAM_0:0:20274696:

###################

File 2 (admins_simple.ini)
Interface must list all current users
Must show the username in the list given the steamid
Ability to add or remove users.
When adding users it is required to have flags such as "99:z"

eg.
"STEAM_0:0:20274696"    "99:z"

Ability to edit flags of current users
Refrence:https://wiki.alliedmods.net/Adding_Admins_(SourceMod)

-When a user is added it must be placed in both files and the same when removed.

-The user interface must look good (use bootstrap).

-Must have an options section to specify the file location for both files

https://wiki.alliedmods.net/Adding_Admins_(SourceMod)
