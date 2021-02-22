
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

def createdict(dictionarylist,newdict):


    for item in dictionarylist:
        if item['subcategory_id'] not in newdict.keys():
            tempdict = {item['subcategory_id']: [item['control_id']]}
            newdict.update(tempdict)
        else:
            tempcontrols = newdict[(item['subcategory_id'])]
            tempcontrols.append(item['control_id'])
            newdict[(item['subcategory_id'])] = tempcontrols

    lista= []
    for key,value in newdict.items():
        lista.append({'subcategory_id': key, 'control_id':value})

    return lista

def profileupgrade(list1,list2):

    i =0
    j=0
    result = []

    while(i< len(list1) and j< len(list2)):

        if list1[i]['subcategory_id'] == list2[j]['subcategory_id']:
            newelement=[]
            newelement = list1[i]
            temp= []

            newelement['control_id']= comparingcontrols(list1[i]['control_id'], list2[j]['control_id'], temp)

            result.append(newelement)
            i=i+1
            j=j+1
        elif list1[i]['subcategory_id'] < list2[j]['subcategory_id']:
            newelement = list1[i]
            result.append(newelement)
            i=i+1
        else:
            newelement = list2[j]
            result.append(newelement)
            j=j+1

    while (i < len(list1)):
        newelement = list1[i]
        result.append(newelement)
        i = i + 1

    while (j < len(list2)):
        newelement = list2[j]
        result.append(newelement)
        j = j + 1

    return result

def comparingcontrols(v1,v2,newelement):
    i = 0
    j = 0

    while (i < len(v1) and j < len(v2)):
        if (v1[i] != v2[j]):
            newelement.append(v2[j])
            newelement.append(v1[i])

        i=i+1
        j=j+1

    while (i < len(v1)):
        newelement.append(v1[i])
        i = i + 1

    while (j < len(v2)):
        newelement.append(v2[j])
        j = j + 1

    return newelement



