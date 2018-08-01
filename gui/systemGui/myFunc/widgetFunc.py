def setEditReadOnly(nameList,Boolean=True):
    for i in nameList:
        i.setReadOnly(Boolean)

def getEditText(name):
    return name.text()

def setEditText(nameList,query,method = "first"):
    if method == "first":
        if query.first():
            for i,name in enumerate(nameList):
                name.setText(str(query.value(i)))




