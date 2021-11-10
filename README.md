# How to merge the contents of many files into one by Bash Scripting?

* #### We have many files that have been created using python. Those files contain codes and functions.
* #### We want to merge all the content from those files into a file called (output.py) so that all functions can be run from this file.
* #### We have a file named (yourCoice.py) this file is as template. It collects all the function plus a function called start_app that is already in this file (yourCoice.py).

## How To Merge?
1. Run fil-merge.sh to create output.py
2. Run execute.sh to start output.py which contains all functions from other files. or you can run it with this command (python3 output.py).