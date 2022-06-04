#!/usr/bin/env python3

# Created By: Alex De Meo
# Date: 03/25/2022
# Description: Gets a sentence and displays each word on a new line

# takes the sentence and puts each word into a list
def parse_string(sentence):
    # split at " "
    words = sentence.split()

    return words


def main():
    # get sentence
    u_sentence = input("Enter a sentence to be parsed: ")
    # call the function that will put the strin into list
    parsed = parse_string(u_sentence)

    for word in parsed:
        print(word)


if __name__ == "__main__":
    main()
