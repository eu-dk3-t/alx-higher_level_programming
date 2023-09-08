#!/usr/bin/python3
""" Defines a text-indentation function """


def text_indentation(text):
    """
    Function name:
        text_indentation
    Description:
        Print text with two new lines after each '.', '?', and ':'.
    Args:
        text (string): The text to print.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    no_space = True
    new_text = ''
    for char in text.strip():
        if char == ' ' and no_space:
            pass
        elif char in ':?.':
            new_text += char + "\n\n"
            no_space = True
        else:
            new_text += char
            no_space = False

    print(new_text, end='')
