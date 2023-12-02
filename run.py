#!/usr/bin/python3

import argparse
import os.path
import time
import traceback

from datetime import datetime, timedelta, timezone
from importlib import import_module

def run_solution(fn, filename):
    try:
        with open(filename) as f:
            try:
                start = time.monotonic_ns()
                print(f"out:\t{fn(f)}", end="\t")
                end = time.monotonic_ns()
                print(f"[{(end-start) / 10**6:.3f} ms]")
            except:
                traceback.print_exc()
    except FileNotFoundError:
        print("Failed to open file: '{}'".format(filename))

# Set to timezone of Advenf of Code.
now = datetime.now(timezone(timedelta(hours=-5)))
parser = argparse.ArgumentParser(description="Runs Advent of Code solutions for current day by default.")
parser.add_argument("-d", "--day", type=int, help="The day of the solution to run.", default=now.day)
parser.add_argument("-y", "--year", type=int, help="The year of the solution to run.", default=now.year)
args = parser.parse_args()

solution_fns = ["p1","p2"]
in_file_paths = [
    f"input/{args.year}/day{args.day:02}_sample.txt",
    f"input/{args.year}/day{args.day:02}.txt"
]

module = import_module(f"py.{args.year}.day{args.day:02}")
for fn in solution_fns:
    print(f"--- {fn} ---")
    for in_file_path in in_file_paths:
        print(f"in:\t{in_file_path}")
        run_solution(getattr(module, fn), in_file_path)
