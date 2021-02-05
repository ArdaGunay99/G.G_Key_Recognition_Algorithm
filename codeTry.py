assoArray=dict()

assoArray["burak"]="ezgi"
assoArray["faruk"]="asli"
assoArray["fatma"]="hayriye"

elementsToDelete=[]
for elem in assoArray:
    if(elem=="burak"):
        elementsToDelete.append(elem)
        
for elem in assoArray:
    print(elem)
    
for elem in elementsToDelete:
    del assoArray[elem]

for elem in assoArray:
    print(elem)
    
assoArrayDup=dict(assoArray)

print("Printing dup array")

for elem in assoArrayDup:
    print(elem)
    if(elem=="faruk"):
        assoArray["deneme"]="denedim"
        del assoArray["faruk"]
        
for elem in assoArray:
    print(elem)

checker=bool(True)

print(checker)

print("S".lower()=="stm".lower())
    