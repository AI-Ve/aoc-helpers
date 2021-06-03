import os
import sys
import argparse
import re
import datetime
import bs4
import requests

PATH = os.getcwd()

def create_files(day: int, year: int) -> None:
    """
    -> Create a new directory for the year if it doesn't exist
    """

    year_dir = PATH + "/year_" + str(year)
    if not os.path.exists(year_dir):
        os.mkdir(year_dir)
        print("Created new directory <-------- {} -------->".format("year " + str(year)))
    os.chdir(year_dir)
    
    """
    -> Create a new directory for the day if it doesn't exist
    """
    day_dir = year_dir + "/day" + str(day)
    if not os.path.exists(day_dir):
        os.mkdir(day_dir)
        print("Created new directory <- {} ->".format("day" + str(day)))
    os.chdir(day_dir)
    
    """
    -> Create the input file
    """
    input_file = str(day) + '.in'

    f = open(input_file, 'w')
    f.close()


def get_puzzle(day: int, year: int) -> None:
    input_url = "https://adventofcode.com/{}/day/{}/input".format(str(year), str(day))
   
    cookie = "" # Paste here the cookie you get when inspecting the AOC page while logged in
    
    response = requests.get(input_url, cookies = {"session": cookie}, allow_redirects = False)
    if response.status_code != 200:
        print("Connection failed")
        exit(0)
    else:
        input_file = str(day) + '.in'
        counter = 0
        f = open(input_file, 'w')
        for line in response.text.split("\n"):
            f.write(line + "\n")
            counter += 1
        f.close()
    
    print("Lines Written: |   {}".format(counter))


if __name__ == "__main__":
    current_time = datetime.datetime.now()
    
    parser = argparse.ArgumentParser(description = 'Get puzzle input for AOC.')
    parser.add_argument('year',
                        type = int, 
                        nargs = 1,  
                        help = 'Years available: 2015-{}'.format(current_time.year if current_time.month == 12 else current_time.year - 1))
    parser.add_argument('day', 
                        type = int, 
                        nargs = 1, 
                        help = 'Days available: 1-25')
    args = parser.parse_args()
    
    day = args.day[0]
    year = args.year[0]
    
    if day not in range(1, 26) or year not in range(2015, current_time.year + 1 if current_time.month == 12 else current_time.year):
        print("Date no allowed!")
        exit(0)


    create_files(day, year)
    get_puzzle(day, year)
