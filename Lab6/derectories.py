import os


def listOfAllFiles():
    print("All folders in this path: ")
    for i in os.listdir(r"C:\Users\Аскар\Desktop\code\python"):
        if os.path.isdir(os.path.join(r"C:\Users\Аскар\Desktop\code\python", i)):
            print(i)
    print("\nAll files in this path: ")
    for i in os.listdir(r"C:\Users\Аскар\Desktop\code\python"):
        if os.path.isfile(os.path.join(r"C:\Users\Аскар\Desktop\code\python", i)):
            print(i)
    print("\nAll files and folders: ")
    for i in os.listdir(r"C:\Users\Аскар\Desktop\code\python"):
        print(i)
# listOfAllFiles()

def testForExistenceReadabilityWritabilityExecutability():
    path = r"C:\Users\Аскар\Desktop\code\python\Lab6"
    path1 = os.access(path, os.F_OK)
    if(path1 == True):
        print("Your file exists!!!!")
    else:
        print("Your file does not exist :(")
    path2 = os.access(path, os.R_OK)
    if(path2 == True):
        print("I can read your file :D")
    else:
        print("I can not read your file :(")
    path3 = os.access(path, os.W_OK)
    if(path3 == True):
        print("I can write something in your file! That is good :D")
    else:
        print("I can not write anything in your file :(")
    path4 = os.access(path, os.X_OK)
    if(path4 == True):
        print("I can execute your file, oh yeah :D")
    else:
        print("I can not execute your file, sad :(")
# testForExistenceReadabilityWritabilityExecutability()

def findingFilenameAndDirectory():
    path = r"C:\Users\Аскар\Desktop\code\python\Lab6\builtin.py"
    if os.access(path, os.F_OK):
        print("Your path exists :D, trying to find the directory and filename")
        x = os.path.split(path)
        print("The directory of the file:", x[0])
        print("The name of file:", x[1])
    else:
        print("Your path does not exist")
# findingFilenameAndDirectory()

def countingLines():
    path = r"C:\Users\Аскар\Desktop\code\python\Lab6\text.txt"
    f = open(path, "r")
    count = 0
    for i in f:
        if(i != "\n"):
            count += 1
    print("The amount of lines in this file is:", count)
# countingLines()

def listToFile():
    path = r"C:\Users\Аскар\Desktop\code\python\Lab6\text.txt"
    my_list = [1, "Askar", "Lenovo laptops are the best!", 4, "I hate stairs"]

    f = open(path, "w")
    f.write("Let me write this list to your file:\n")
    print(my_list)
    for i in my_list:
        f.write(str(i) + " ")
    f.close()

    f = open(path, "r")
    print(f.read())
# listToFile()

def AtxtToZtxt():
    path = r"C:\Users\Аскар\Desktop\code\python\Lab6"
    for i in range(65, 90):
        name = os.path.join(path, chr(i) +".txt")
        f = open(name, "a")
    for i in os.listdir(path):
        print(i)
# AtxtToZtxt()

def copyPaste():
    path = r"C:\Users\Аскар\Desktop\code\python\Lab6\text.txt"
    pathOfSecondfile = r"C:\Users\Аскар\Desktop\code\python\Lab6\text1.txt"
    # copying text.txt to text1.txt
    f = open(path, "r")
    f1 = open(pathOfSecondfile, "w")
    for i in f:
        f1.write(str(i))
    f1.close()
    f.close()

    f1 = open(pathOfSecondfile, "r")
    for i in f1:
        print(i)
# copyPaste()

def delitingFileInSpecificPath():
    path = r"C:\Users\Аскар\Desktop\code\python\Lab6\text2.txt"
    if(os.access(path, os.F_OK)):
        print("Your path exist!\nOkay...let me delete your file")
        os.remove(path)
        print("Deleting is succesful! :D")
    else:
        print("Your path does not exist :(")
# delitingFileInSpecificPath()
        