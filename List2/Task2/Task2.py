import sys
import os
from datetime import datetime

args=sys.argv
try:
    if (len(args)==4):
        path=str(args[1])
        extension=str(args[2])
        suffix=str(args[3])
    elif (len(args)==3):
        path=str(args[1])
        extension=str(args[2])
        suffix=datetime.now().strftime('%Y%m%d')
    else:
        print("Wrong number of arguments. Required arguments: folder path (string), file extension (string) and optionally suffix (string).")
        sys.exit()

    path.encode('unicode_escape')
    fileList=os.listdir(path)

    for item in fileList:
        if item.endswith(extension):
            fullPath=os.path.join(path, item)
            filePath, ext = os.path.splitext(fullPath)
            fullPathSwap= filePath +"_"+suffix+ext
            os.rename(fullPath,fullPathSwap)

except ValueError:
    print("Something wrong with the arguments you gave.")
    print("Required arguments: folder path (string), file extension (string) and optionally suffix (string).")