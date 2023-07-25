import cgi
import os.path
import pickle

from zmodule.sqlcommandsnew import sqlcommands
from zmodule.CommonDoc import MyDoc

test = sqlcommands()

dum_val = "..."
skin = "cgi-bin/forms/t_input.html"

def MakeForm(data, msg):
    
    global skin, dum_val
    meta = None
    form = ""
    with open(skin) as f:
        lines = f.readlines()
        meta = eval(lines[0])
        form = form.join(lines[1:])
    
    for ss, key in enumerate(meta):
        actual = dum_val
        if len(data) is 0:
            form = form.replace(meta[key], actual)
        else:
            actual = data[ss]
            form = form.replace(meta[key], actual)
            if ss == 0:
                form = form.replace("Submit", msg)
    print(form)

def LoadData():
    test.Open()
    test.NewTable()

def ReadCGI(dat):
    
    ret = ["0","0","0"]
    for key in dat:
        if key == "zNumber":
            ret[0] = dat[key]
        elif key == "zName":
            ret[1] = dat[key]
        elif key == "zEmail":
            ret[2] = dat[key]
        else:
            ret.append(dat[key])
    return ret

def decode(dat):
    
    if isinstance(dat, dict):
        return dat
    zsave = dict()
    if dat is None:
        return zsave
    for key in dat:
        ukey = key
        uval = dat[key].value
        zsave[ukey] = uval
    return zsave

try:
    LoadData()
    MyDoc.Do_Start()
    dat = cgi.FieldStorage()
    dat = decode(dat)
    ret = ReadCGI(dat)
        
    if len(dat) is 0:
        MakeForm(dat,"Enter Data")
    else:
        test.FillTable(ret)
        MakeForm(ret,"Successful Submition")
    

except Exception as ex:
    MakeForm(ret,"Input Error - " + str(ex))

test.End()  
MyDoc.Do_End()
