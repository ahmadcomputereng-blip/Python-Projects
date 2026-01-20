#implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
word = input("Input: ")
print("Output: " , end = "")
for c in word:
    a = c.lower()
    if (a == 'a'or a == 'e' or a == 'i' or a == 'o' or a == 'u'):
        print(end = "")
    else:
        print (c , end = "")
