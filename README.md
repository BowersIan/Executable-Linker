# Executable-Linker
Recursively searches through a directory and links all executable files to your binaries directory

## Usage
Download the Executable-Linker.py file and run it with python3. See the printout of the help command below:

    usage: executable-linker [-h] [-i INPUT] [-o OUTPUT] [-f] [-l] [-g]

    optional arguments:
    -h, --help            show this help message and exit
    -i INPUT, --input INPUT
                            Folder to search through, defaults to current working
                            directory
    -o OUTPUT, --output OUTPUT
                            Folder to place links, defaults to ~/.local/bin
    -f, --follow-links    Follow links in directory structure, may lead to
                            infinite looping or other issues
    -l, --lower           Sets link names to lowercase
    -e, --extension       Leaves file extension on link
    -g, --git             Stops ignoring .git folders. Recommended to leave off
