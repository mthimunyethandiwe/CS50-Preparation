#implement a program that prompts the user for the name of a file and then outputs that file’s 
# media type if the file’s name ends, case-insensitively, in any of these suffixes:.gif, .png, .jpeg, .jpg, .pdf, .txt, .zip
name = input("File Name: ")
name_converted = name.strip().lower()

if name_converted.endswith(".jpg") or name_converted.endswith(".jpeg"):
        print("image/jpeg")


elif name_converted.endswith(".png"):
        print("image/png")

elif name_converted.endswith(".pdf"):
        print("application/pdf")

elif name_converted.endswith(".txt"):
        print("text/plain")

elif name_converted.endswith(".zip"):
        print("application/zip")

elif name_converted.endswith(".gif"):
        print("image/gif")

else:
    print("application/octet-stream")