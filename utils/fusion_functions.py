
def convertFromDatabase(context):
    for subcategory in context:
        if subcategory["priority"]== "Alta":
            subcategory["priority"]=3
        if subcategory["priority"] == "Media":
            subcategory["priority"]=2
        if subcategory["priority"] == "Bassa":
            subcategory["priority"]=1
    
    for subcategory in context:
        subcategory["maturity_level"]= subcategory["maturity_level"].split(",")
        subcategory["maturity_level"] = [level.replace('Insufficiente', '0') for level in subcategory["maturity_level"]]
        subcategory["maturity_level"] = [level.replace('Minimo', '1') for level in subcategory["maturity_level"]]
        subcategory["maturity_level"] = [level.replace('Standard', '2') for level in subcategory["maturity_level"]]
        subcategory["maturity_level"] = [level.replace('Avanzato', '3') for level in subcategory["maturity_level"]]
    return context

def convertToDatabase(context):
    for subcategory in context:
        if subcategory["priority"]== 3:
            subcategory["priority"]="Alta"
        if subcategory["priority"] == 2:
            subcategory["priority"]="Media"
        if subcategory["priority"] == 1:
            subcategory["priority"]="Bassa"
    
    for subcategory in context:
        subcategory["maturity_level"] = [level.replace('0', 'Insufficiente') for level in subcategory["maturity_level"]]
        subcategory["maturity_level"] = [level.replace('1', 'Minimo') for level in subcategory["maturity_level"]]
        subcategory["maturity_level"] = [level.replace('2', 'Standard') for level in subcategory["maturity_level"]]
        subcategory["maturity_level"] = [level.replace('3', 'Avanzato') for level in subcategory["maturity_level"]]
        subcategory["maturity_level"] = ",".join(subcategory["maturity_level"])
    return context

def checkPriority(maturity1, maturity2):
    if(maturity1[0] == 0):
        for i, level in enumerate(maturity1, start=0):
            maturity1[i] = maturity1[i+1]
        maturity1.remove()
    elif maturity2[0] == 0:
        for i,level in enumerate(maturity2, start=0):
            maturity2[i] = maturity2[i+1]
        maturity2.remove()  

def comparingmaturity(v1, v2, newelement):
    i =0
    j=0
    
    while (i< len(v1) and j< len(v2)):
        if(v1[i] < v2[j]):
            newelement.append(v1[i])
            i=i+1
        elif (v1[i] == v2[j]):
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

    for subcategory in dictionarylist:
        if subcategory['subcategory_id'] not in newdict.keys():
            tempdict = {subcategory['subcategory_id']: [subcategory['control_id']]}
            newdict.update(tempdict)
        else:
            tempcontrols = newdict[(subcategory['subcategory_id'])]
            tempcontrols.append(subcategory['control_id'])
            newdict[(subcategory['subcategory_id'])] = tempcontrols

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


