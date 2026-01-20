def main():
    word = input("Input: ")
    twt = shorten(word)
    print(f"Output: {twt}")

def shorten(word):

    for c in word:
        if c.isalpha():
            a = c.lower()
            if (a == 'a'or a == 'e' or a == 'i' or a == 'o' or a == 'u'):
                word = word.replace(c, "")
        else:
            continue
    return(word)

if __name__ == "__main__":
    main()
