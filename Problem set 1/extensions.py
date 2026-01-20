#implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
file = input ("File name: ")
file = file.lower().strip()
if file.endswith(".gif") or file.endswith(".png"):
    file = file.split(".")[-1]
    file = file.replace("." , "")
    print("image/" + file)
elif file.endswith(( ".jpg" , ".jpeg" )):
    print("image/jpeg")
elif file.endswith((".pdf" , ".zip")):
    file = file.split(".")[-1]
    file = file.replace("." , "")
    print("application/" + file)
elif file.endswith(".txt"):
    print("text/plain")
else:
    print("application/octet-stream")
