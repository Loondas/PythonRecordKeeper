import cgi
import math
from zmodule.sqlcommandsnew import sqlcommands
from zmodule.CommonDoc import MyDoc

test = sqlcommands()
skin = "cgi-bin/forms/t_view.html"

def MakeForm(data, track, det):
    global skin
    form = ""
    with open(skin) as f:
        lines = f.readlines()
        form = form.join(lines)
        
        place = "'pager' value='0"
        if track is not None:
            form = form.replace(place, track)
    if len(data) is 0:
        form = form.replace("dim", "Nothing to display")
    else:
        tition = repl(data, det)
        form = form.replace('<textarea rows="4" cols="100" id="0" readonly>dim</textarea>',
                            tition)
    print(form)

def pagin(inc, ret):
    if ret == '1':
        rement = "'pager' value='0"
        inc = 0
    elif ret == '2':
        inc = int(inc) - 5
        if inc < 0:
            inc = 0
        rement = "'pager' value='" + str(inc)
    elif ret == '3':
        inc = int(inc) + 5
        rement = "'pager' value='" + str(inc)
    elif ret == '4':
        inc = test.CountEntry()
        inc = int(math.floor(inc[0]/5)*5)
        rement = "'pager' value='" + str(inc)
    elif ret is None:
        return None, 0
    else:
        inc = int(inc) + 5
        rement = "'pager' value='" + str(inc)
    return rement, inc
    
def repl(data, inc):
    tition = ""
    a = 0
    for i, dat in enumerate(data, inc + 1):
        rep = []
        tition += '<button name="edit" value="'+str(data[a][0])+'" formaction="edit.py">Edit Entry ' + str(i) + '</button>\n'
        a = a + 1
        for d in dat:
            rep.append(d)
            tition += '<textarea rows="1" cols="20" id="'+str(i)+'" readonly>'+str(d)+'</textarea>\n'
        tition +=  '<input class = "butt" type="checkbox" name="delete" value="'+str(rep[0])+'">\n'
    return tition

try:
    MyDoc.Do_Start()
    test.Open()
    dat = cgi.FieldStorage()
    numbers = dat.getlist('delete')
    test.DelEm(numbers)
    ret = dat.getvalue('Nav')
    det = dat.getvalue('pager')
    if det is None:
        det = 0
    track, inc = pagin(det,ret)
    det = inc
    data = test.GetSome(det)
    MakeForm(data, track, det)
    test.End
    
except Exception as ex:
    import traceback
    ban = "<br>" + ('*' * 5)
    nab = ('*' * 5) + "<br>"
    print(ban, ex, nab)
    tb = ex.__traceback__
    for ss, item in enumerate(traceback.format_tb(tb), 1):
        item = item.replace(" line ", "<font color='red'> line </font>") # New
        print(ss, item, "<br/>", sep="&nbsp;\t")

MyDoc.Do_End()
