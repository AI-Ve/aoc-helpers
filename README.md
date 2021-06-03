# AOC-download-inputs
Short script that downloads the input file for a given day.

The script runs in the command line as such: `python3 get_input.py 2018 10`.<p>
The script creates its own directory for each year and in the year folder, creates separate directories for each day. This will happen in the directory the script is located.
Only requirement is to have requests and bs4 installed.<p>
In case those are missing, use: `pip3 install bs4 requests`.
