#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

from colored import stylize, fg

# decoration
print(stylize("\n---- | Check if lines are parallel | ----\n", fg("red")))

# user interaction
print("Lines are represented as [a, b, c].")
first_line = input("Determine first line: ").split(", ")
second_line = input("Determine second line: ").split(", ")

# main program
def check(l1, l2):
    if l1 == l2:
        return "\nThe lines are parallel to themselves.\n"
    elif l1[0] == l2[0] and l1[1] == l2[1]:
        return "\nThe lines are parallel.\n"
    else:
        return "\nThe lines are not parallel.\n"

output = stylize(check(first_line, second_line), fg("red"))
print(f"\nFirst line: {first_line[0]}x + {first_line[1]}y = {first_line[2]}")
print(f"First line: {second_line[0]}x + {second_line[1]}y = {second_line[2]}")
print(output)
