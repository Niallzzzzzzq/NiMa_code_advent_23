import re, os

fp_puzzle_input="day_one_puzzle_input.txt"
fp_puzzle_input=os.path.abspath(os.path.join(os.path.dirname(__file__),fp_puzzle_input))
assert os.path.exists(fp_puzzle_input)

with open(fp_puzzle_input) as fid:
    puzzle_input=fid.read()

print(puzzle_input)