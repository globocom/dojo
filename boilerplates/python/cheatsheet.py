############################################################################
# Language idiosyncratics
############################################################################
x = """
- no strong typing - variables can be any type (at least by default)
- Indentation matters (a lot)
- <tabs> and <spaces> are VERY different - use only 4xSpaces
- When <tabs> are mixed with <spaces> erros WILL occur
- snake_case_is_recommended
"""

############################################################################
# Types
############################################################################
t_bool = True
t_str = "abc"
t_int = 42
t_float = 1234.56  # or 1.23456e3
# t_struct # python does not have structs. Use classes/objects (or list/dicts)
# pointers: objects and lists are always passed as pointers
t_null = None

t_list = [1, "2", True]  # there are no arrays. Elements can be anything
t_dict = {  # newline for readability
    "key": "value",
    42: True,
}  # hashmaps (key: value). values can be anything. keys must be hashable


############################################################################
# Maths & Basics
############################################################################
import math

t_int += 1  # Increment by one. there is no i++ syntax
powered = 2 ** 8  # 256
mod_division = 13 % 5  # 3
floored = 8 // 3  # Like floor: 2 (2.666...)
floored = math.floor(42.8)  # 42
ceiled = math.ceil(41.2)  # 42
rounded = round(2.255, 2)  # 2.26


############################################################################
# Functions (with indentation only, no curly braces {} )
############################################################################
def f_function(arg1, arg2, arg3="Default value"):
    return (arg3, arg2, arg1)


all_args = f_function(2, True)  # all_args = (arg3, arg2, arg1)
arg3, arg2, arg1 = f_function(2, True, "hello?")
f_function(arg1=1, arg2=True, arg3="hello?")


############################################################################
# String manipulation
############################################################################
c = "concatenate" + " a number: " + str(10)
formatted_string = f"interpolate variables like {c} or {t_int+10}"
formatted_string2 = "var {}, 001 {:03d}, 2.89 {:.2f}".format("var", 1, 2.8888)
all_lowercase = c.lower()
all_uppercase = c.upper()
trimmed_string = "  no spaces before or after   \n".strip()
split_list = "split, a, string".split(", ")
join_list = ", ".join(split_list)  # elements MUST be strings
length_of_string = len("abç")  # 3
replaced_string = t_str.replace("bc", "eiou")  # "abc" -> "aeiou"


############################################################################
# Conditionals
############################################################################
if True:
    print("always true")
elif ("condition 1" or 10 or ["a"]) and ("" or False or None or 0 or []):
    print("Left conditions are true. Right conditions are False")
elif t_null is not None and t_int == 42 and t_str == abc and 1 in t_list:
    print("operators: ==, !=, >, >=, <, <=")
else:
    print("text without newline", end="")
    print()  # empty line (just \n)


############################################################################
# Loops (break/continue apply) (python does not have classic loops)
############################################################################
while True:
    print("Infinite loops are like this (until break or return)")
    break

for i in range(0, 5):
    print(f"last printed digit is 4: {i}")

for char in t_str:
    print(f"iterate all characters from a string: {char}")

for element in t_list:
    print(f"iterate all elements from a list: {element}")

for key, value in t_dict.items():
    print(f"iterate all elements from a dict: {key}:{value}")


############################################################################
# Lists/Dicts manipulation
############################################################################
first_element = t_list[0]
last_element = t_list[-1]  # negative index counts from the end
first_and_second = t_list[0:2]  # sub-list syntax: from:to(exclusive)
element_index = t_list.index("2")  # Exception if not found

t_list.append("new element to the end of the list")
popped_string = t_list.pop()  # "remove and get last element"
length_of_list = len([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])  # 10

t_dict["new key"] = "new value"  # insert new keys
remove_a_key = t_dict.pop("new key")

is_true = "2" in t_list  # check if element exists in list
is_false = "value" in t_dict  # this checks keys only
is_true = "value" in t_dict.values()  # this checks keys only


############################################################################
# Regex usage
############################################################################
import re
match_list = re.findall("[a-z]+", "ab3 c22 dd5")  # ['ab', 'c', 'dd']
is_true = bool(re.search("\+1[0-9]{7}", "+12345678"))
group_match = re.search(">([a-z]+)<", "<123>abcd</123>").group(1)
