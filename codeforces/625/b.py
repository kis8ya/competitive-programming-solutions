import re

if __name__ == "__main__":
    name = raw_input()
    forbidden_substring = raw_input()
    # Less memory
    print sum(1 for _ in re.finditer(forbidden_substring, name))

    # Faster
    # print len([0 for _ in re.finditer(forbidden_substring, name)])
