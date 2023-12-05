import re, os

fp_puzzle_input="day_one_puzzle_input.txt"
fp_puzzle_input=os.path.abspath(os.path.join(os.path.dirname(__file__),fp_puzzle_input))
assert os.path.exists(fp_puzzle_input)

with open(fp_puzzle_input) as fid:
    puzzle_input=fid.readlines()

# print(puzzle_input)

def parse_line(text_line):
    number_pattern_dict={
            'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9
        }
    number_pattern_dict={**number_pattern_dict,**{str(i):i for i in range(1,10)}}
    # number_pattern="((?=%s))"%(")|(?=".join(number_pattern_dict.keys()))
    number_pattern="(%s)"%("|".join(number_pattern_dict.keys()))
    number_entries=re.findall(number_pattern,text_line)
    
    first_digit=''
    first_digit_pos=None
    last_digit=''
    last_digit_pos=None

    for dig in number_pattern_dict.keys():
        dig_pattern="(?=%s)"%dig
        matches= re.finditer(dig_pattern,text_line)
        # if (matches)

    # logic:
    # loop over possible digits
    #   find all matches to possible digits using lookahead
    #   assign earliest matching digit to first digit
    #   assign last matching digit to last digit
    # return (10 * first digit) + last digit

        
    assert len(number_entries)>0
    return 10*number_pattern_dict[number_entries[0]]+number_pattern_dict[number_entries[-1]]

# for i in range(10,25):
#     print(puzzle_input[i].strip(),parse_line(puzzle_input[i]))

def parse_line_better(text_line):
    number_pattern_dict={
            'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9
        }
    number_pattern_dict={**number_pattern_dict,**{str(i):i for i in range(1,10)}}
    number_pattern_dict
    number_pattern="((?=%s))"%(")|(?=".join(number_pattern_dict.keys()))
    matches=[i for i in re.finditer(number_pattern,text_line)]

    number_pattern_consuming="(%s)"%("|".join(number_pattern_dict.keys()))
    last_digit_index=matches[0].span()[0]
    first_digit=re.match(number_pattern_consuming,text_line[last_digit_index:]).group()
    last_digit_index=matches[-1].span()[0]
    last_digit=re.match(number_pattern_consuming,text_line[last_digit_index:]).group()

    return 10*number_pattern_dict[first_digit]+number_pattern_dict[last_digit]



print(sum([parse_line(i) for i in puzzle_input]))
print(sum([parse_line_better(i) for i in puzzle_input]))

# for i in puzzle_input:
#     try:
#         _=parse_line(i)
#     except:
#         print(i)

test_text_1="""1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
test_text_2="""two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
# for i in test_text.splitlines():
#     print(i,parse_line(i))

assert sum([parse_line(i) for i in test_text_1.splitlines()])==142
assert sum([parse_line(i) for i in test_text_2.splitlines()])==281
# print( sum([parse_line_better(i) for i in test_text_1.splitlines()]))
# print( sum([parse_line_better(i) for i in test_text_2.splitlines()]))
assert sum([parse_line_better(i) for i in test_text_1.splitlines()])==142
assert sum([parse_line_better(i) for i in test_text_2.splitlines()])==281


# print(parse_line("eighthree"))
# print(
#     re.findall("(one|two|three|four|five|six|seven|eight|nine)","eighthree")
# )

number_pattern_dict={
            'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9
        }
number_pattern_dict={**number_pattern_dict,**{str(i):i for i in range(1,10)}}
number_pattern="((?=%s))"%(")|(?=".join(number_pattern_dict.keys()))
# print(number_pattern)

s="eighthree"
# print(re.match(number_pattern,s))
# matches = re.finditer(number_pattern, s)
# for match in matches:
#     print(match)