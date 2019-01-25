# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text, 1):
        if next in "([{":
            opening_brackets_stack.append(Bracket(char = next, position = i))
            pass
        if next in ")]}":
            if are_matching(opening_brackets_stack[-1].char, next):
                opening_brackets_stack.pop()
            else:
                return i
            pass
         
    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    else:
        return "Success"

def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)

if __name__ == "__main__":
    main()
