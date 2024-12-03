import os
import argparse
import requests
from datetime import date
from pyprojroot import here


SESSION_COOKIE = os.getenv("AOC_SESSION_COOKIE")

today = date.today()
this_year = today.year
this_day = today.day

parser = argparse.ArgumentParser(
    description="Get puzzle input for a particular day and write it to a text file."
)
parser.add_argument(
    "--year",
    help="Year to fetch data for. Defaults to current year.",
    default=this_year,
)
parser.add_argument(
    "--day", help="Day to fetch data for. Defaults to current day.", default=this_day
)
args = parser.parse_args()

year = args.year
day = args.day

url = f"https://adventofcode.com/{year}/day/{day}/input"

headers = {
    "Cookie": f"session={SESSION_COOKIE}",
}

response = requests.get(url, headers=headers)

puzzle_input = response.text

print(puzzle_input)

path_to_file = os.path.abspath(here(f"{year}/data/day{str(day).zfill(2)}.txt"))
dirname = os.path.dirname(path_to_file)

if not os.path.exists(dirname):
    os.makedirs(dirname)

with open(path_to_file, "w") as f:
    f.write(puzzle_input)

print(f"Puzzle input has been written to {path_to_file}")
