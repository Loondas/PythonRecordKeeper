import cgi
import os.path
import pickle

from zmodule.CommonDoc import MyDoc

skin = "cgi-bin/forms/t_front.html"
DEF_FILE = "cgi-bin/data/lab_default.pcl"

##if __name__ == "__main__":
##    skin = "forms/t_front.html"
def MakeForm():
    global skin
    form = ""
    with open(skin) as f:
        lines = f.readlines()
        form = form.join(lines[0:])
    print(form)


MyDoc.Do_Start()
MakeForm()
MyDoc.Do_End()

    
