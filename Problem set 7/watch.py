import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'^<iframe (?:.*?)src="http(?:s){0,1}://(?:www\.){0,1}youtube\.com/embed/(.*?)"(.*?)</iframe>$'
    match = re.search(pattern,s)
    if match:
        url = match.group(1)
        return f"https://youtu.be/{url}"
    return




if __name__ == "__main__":
    main()
