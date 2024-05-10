monthnumbers = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,1:'jan',2:'feb',3:'mar',4:'apr',5:'may'}
keys=[]
for e in monthnumbers:
    keys.append(str(e))
    print(keys)
    keys.sort()
    print(keys)