import re, os

fp_puzzle_input="day_one_puzzle_input.txt"
fp_puzzle_input=os.path.abspath(os.path.join(os.path.dirname(__file__),fp_puzzle_input))
assert os.path.exists(fp_puzzle_input)

with open(fp_puzzle_input) as fid:
    puzzle_input=fid.readlines()

# print(puzzle_input)

number_pattern_dict={
        'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9
    }
number_pattern_dict={**number_pattern_dict,**{str(i):i for i in range(1,10)}}
number_pattern="(%s)"%("|".join(number_pattern_dict.keys()))

def parse_line(text_line):
    
    number_entries=re.findall(number_pattern,text_line)

    return 10*number_pattern_dict[number_entries[0]]+number_pattern_dict[number_entries[-1]]

# print(puzzle_input[3])
# print(parse_line(puzzle_input[3]))

print(sum([parse_line(i) for i in puzzle_input]))

# for i in puzzle_input:
#     try:
#         _=parse_line(i)
#     except:
#         print(i)

test_text="""two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
for i in test_text.splitlines():
    print(i,parse_line(i))

print(sum([parse_line(i) for i in test_text.splitlines()]))

print(number_pattern_dict)