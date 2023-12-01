import re, os

fp_puzzle_input="day_one_puzzle_input.txt"
fp_puzzle_input=os.path.abspath(os.path.join(os.path.dirname(__file__),fp_puzzle_input))
assert os.path.exists(fp_puzzle_input)

with open(fp_puzzle_input) as fid:
    puzzle_input=fid.readlines()

# print(puzzle_input)

def parse_line(text_line):
    number_entries=re.findall(r"\d",text_line)

    return int(number_entries[0]+number_entries[-1])

# print(puzzle_input[3])
# print(parse_line(puzzle_input[3]))

print(sum([parse_line(i) for i in puzzle_input]))