import re

pattern = input("Enter a regular expression pattern: ")
test_strings = input("Enter test strings (comma-separated): ").split(',')



for string in test_strings:
    if re.match(pattern, string):
        print(f"'{string}' matches the pattern '{pattern}'.")
    else:
        print(f"'{string}' does not match the pattern '{pattern}'.")
