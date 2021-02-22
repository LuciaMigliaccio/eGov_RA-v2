
def convertTo(context):
    for item in context:
        if item["priority"]== "Alta":
            item["priority"]=3
        if item["priority"] == "Media":
            item["priority"]=2
        if item["priority"] == "Bassa":
            item["priority"]=1
    
    for item2 in context:
        item2["maturity_level"]= item2["maturity_level"].split("\r\n")
        
        item2["maturity_level"] = [item.replace('Insufficiente', '0') for item in item2["maturity_level"]]
        item2["maturity_level"] = [item.replace('Minimo', '1') for item in item2["maturity_level"]]
        item2["maturity_level"] = [item.replace('Standard', '2') for item in item2["maturity_level"]]
        item2["maturity_level"] = [item.replace('Avanzato', '3') for item in item2["maturity_level"]]
    return context

def convertFrom(context):
    for item in context:
        if item["priority"]== 3:
            item["priority"]="Alta"
        if item["priority"] == 2:
            item["priority"]="Media"
        if item["priority"] == 1:
            item["priority"]="Bassa"
    
    for item2 in context:
        
        item2["maturity_level"] = [item.replace('0', 'Insufficiente') for item in item2["maturity_level"]]
        item2["maturity_level"] = [item.replace('1', 'Minimo') for item in item2["maturity_level"]]
        item2["maturity_level"] = [item.replace('2', 'Standard') for item in item2["maturity_level"]]
        item2["maturity_level"] = [item.replace('3', 'Avanzato') for item in item2["maturity_level"]]

        item2["maturity_level"] = "\r\n".join(item2["maturity_level"])
    return context

def checkPriority(maturity1, maturity2):
    if(maturity1[0] == 0):
        for i, item in enumerate(maturity1, start=0):
            maturity1[i] = maturity1[i+1]
        maturity1.remove()
    elif maturity2[0] == 0:
        for i,item in enumerate(maturity2, start=0):
            maturity2[i] = maturity2[i+1]
        maturity2.remove()  

def comparingmaturity(v1, v2, newelement, condizione):
    i =0
    j=0
    
    while (i< len(v1) and j< len(v2)):

        if(v1[i] < v2[j]):
            newelement.append(v1[i])
            i=i+1
        elif (v1[i] == v2[j]):
            if condizione == True:
                newelement.append(v1[i])
            i=i+1
            j=j+1
        else:
            newelement.append(v2[j])
            j=j+1

    while(i<len(v1)):
        newelement.append(v1[i])
        i=i+1

    while(j<len(v2)):
        newelement.append(v2[j])
        j=j+1

    return newelement

        



