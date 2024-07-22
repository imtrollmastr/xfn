import os

def loadCommandPrompt():
    print('Select a option:')
    print("1) Show an XFN file")
    print("2) Convert a file to XFN")
    cmdprompt = input(">")
    if cmdprompt == "1":
        print("Enter the filename:")
        cmdprompt = input(">")
        os.system("python3 xfn_images/render.py " + cmdprompt)
        exit()
    elif cmdprompt == "2":
        print("Enter the file you would like to convert:") 
        cmdprompt = input(">")
        print("Enter the output name of the XFN file:")
        cmdprompt2 = input(">")
        os.system("python3 xfn_images/convert.py " + cmdprompt + " " + cmdprompt2)
        exit()
    else:
        loadCommandPrompt()

loadCommandPrompt()