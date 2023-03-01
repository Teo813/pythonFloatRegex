# This is a sample Python script.
import re
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def check_Regex(text):
    pattern = "([0-9]*.[0-9]|[0-9]+.)([eE][+-]?[0-9]+)?[LlFf]?|[+-]?[0-9]+[eE][+-]?[0-9]+[LlFf]?"
    match = re.match(pattern, text)
    if match:
        print("Match found:", match.group())
    else:
        print("No match")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    text = input("Enter some text: ")
    check_Regex(text)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
