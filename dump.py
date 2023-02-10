import sys,inspect

def getFuncs():
    functionFile = open("dump.txt","a")
    members = inspect.getmembers(sys.modules[__name__])
    for member in members:
        print(member)
        functionFile.write(str(member) + "\n")
    functionFile.close()

getFuncs()