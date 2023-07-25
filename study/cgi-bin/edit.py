import cgi
import os.path

from zmodule.sqlcommandsnew import sqlcommands
from zmodule.CommonDoc import MyDoc

test = sqlcommands()
dum_val = "..."
skin = "cgi-bin/forms/t_update.html"
options = "<select type='text' name='zNumber' value='%address%'><br/>"

def MakeForm(data, msg):
    
    global skin, dum_val
    meta = None
    form = ""
    match = ['...','...','...','...']
    bala = ['...','...','...','...']
    with open(skin) as f:
        lines = f.readlines()
        meta = eval(lines[0])
        form = form.join(lines[1:])
    if len(data) is 2 or len(data) is 4:
        try:
            full = PopDrop(data['edit'])
            match = test.GetOne(data['edit'])
        except:
            full = PopDrop(data['zNumber'])
            match = test.GetOne(data['zNumber'])
        for a in match:
            bala = a  
    elif len(data) is 0:
        full = PopDrop()
    else:
        full = PopDrop(data[2])
    form = form.replace(options, full)
    for ss, key in enumerate(meta):
        actual = dum_val
        
        if len(data) is not 3:
            actual = bala[ss + 1]
            form = form.replace(meta[key], actual)
        else:
            actual = data[ss]
            form = form.replace(meta[key], actual)
            if ss == 0:
                form = form.replace("Update", msg)
    print(form)

def LoadData():
    test.Open()
    test.NewTable()

def PopDrop(i=1):
    filler = test.GetPrimary()
    totes = options + '\n'
    for ss, a in enumerate(filler):
        if int(a[0]) == int(i):
            totes += '<option value="%s" selected>%s</option>\n' % (a[0],a[0])
        else:
            totes += '<option value="%s">%s</option>\n' % (a[0],a[0])
    return totes
    
def ReadCGI(dat):
    
    ret = ["0","0","0"]
    for key in dat:
        if key == "zNumber":
            ret[2] = dat[key]
        elif key == "zName":
            ret[0] = dat[key]
        elif key == "zEmail":
            ret[1] = dat[key]
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
        if key != 'delete':
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
    if len(dat) is not 3:
        MakeForm(dat,"Enter Data")
    else:
        test.UpdateOne(ret)
        MakeForm(ret,"Successful Submition")

except Exception as ex:
    MakeForm(ret, "InputError - " + str(ex))
    
test.End()
MyDoc.Do_End()
