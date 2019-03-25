#!/usr/bin/env python3
import os
import argparse

def link(src, dst):
    os.symlink(src, dst)

parser=argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='Folder to search through, defaults to current working directory', default='./')
parser.add_argument('-o','--output', help='Folder to place links. Should not be within the input folder. Defaults to ~/.local/bin', default=os.path.expanduser('~')+'/.local/bin')
parser.add_argument('-f','--follow-links', help='Follow links in directory structure, may lead to infinite looping or other issues', action='store_true')
parser.add_argument('-l', '--lower', help='Sets link names to lowercase', action='store_true')
parser.add_argument('-e', '--extension', help='Leaves file extension on link', action='store_true')
parser.add_argument('-g', '--git', help='Stops ignoring .git folders. Recommended to leave off', action='store_true')

args=parser.parse_args()

workingDirectory=args.input
outputDirectory=os.path.join(os.getcwd(), args.output)
os.chdir(workingDirectory)

for currentDirectory, subFolders, files in os.walk(os.getcwd(), followlinks=args.follow_links):
    
    if not args.git:
        if '.git' in subFolders:
            subFolders.remove('.git')
            
    for file in files:
        if os.access(os.path.join(currentDirectory, file), os.X_OK):
            src=os.path.abspath(os.path.join(currentDirectory, file))
            print(src)
            if args.lower:
                temp=file.lower()
            else:
                temp=file

            if not args.extension:
                dst=os.path.join(outputDirectory, os.path.splitext(temp)[0])
            else:
                dst=os.path.join(outputDirectory, temp)
            try:
                link(src, dst)
            except FileExistsError as e:
                os.remove(dst)
                link(src, dst)