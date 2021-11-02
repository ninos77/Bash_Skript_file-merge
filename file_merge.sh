#!/bin/bash
rm output.py
for f in *.py; do
     echo "#==============START ${f::-3}=============" >> output.py
     cat $f >> output.py
     echo " " >> output.py
     echo "#==============END ${f::-3}=============" >> output.py
     echo " " >> output.py
done
