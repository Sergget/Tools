import os
from pptx import Presentation

if __name__ =="__main__":
    files=os.listdir(".")

    for file in files:
        if file[0:2]!="~$" and file.endswith(".pptx"):
            prs = Presentation(file)
            print(prs)