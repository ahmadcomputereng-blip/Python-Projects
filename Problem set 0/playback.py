#In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... 
#Run your program with python playback.py. Type This is CS50 and press Enter. Your program should output:
#This...is...CS50  
name = input().replace(" ", "...")
print(name)