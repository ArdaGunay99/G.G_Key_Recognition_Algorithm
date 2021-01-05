import re
import xlsxwriter
print("AE"=="ae")

deneme1="japanaeduration"
deneme2="japanAEduration"

print("AE" in deneme1)
print("AE" in deneme2)

deneme3="barbieAEpresence"
#gets all uppercases returns list
r=re.findall('[A-Z]',deneme3)
#joins list to a str
joinR=''.join([str(elem) for elem in r])
print(r)
print(type(r))
print(joinR)
print(type(joinR))
#word after certain characters
wordAfterKeyProfile=deneme3.split(joinR,1)[1]

print(wordAfterKeyProfile)

deneme4=["ayşe","fatma","hayriye","pembe"]

for index in range(len(deneme4)):
    print("This is the value {}".format(deneme4[index]))
    print("This is the index {}".format(index))
    
class excelWriter():
    #the actual excel file
    __excelFile=""
    #the worksheet we write
    __workSheet=""
    #column Headers should be ordered when given,it should be list
    __columnHeaders=""
    #row counter
    __row=0
    
    def __init__(self,fileName,columnHeaders):
        print("Creating the object")
        self.__excelFile=xlsxwriter.Workbook(fileName+".xlsx")
        self.__workSheet=self.__excelFile.add_worksheet()
        self.__columnHeaders=columnHeaders
        
    def getExcelFile(self):
        if(self.__excelFile != ""):
            return self.__excelFile
        else:
            print("File not created")
    def setColumnHeaders(self,colHeaderNames):
        #col headers should be ordered
        self.__columnHeaders=colHeaderNames
    def writeColumnHeaders(self):
        #check if the file is created
        if(self.__workSheet == ""):
            print("Document not created")
        else:
            for index in range(len(self.__columnHeaders)):
                print("Writing the value {}".format(self.__columnHeaders[index]))
                self.__workSheet.write(0,index,self.__columnHeaders[index])
        self.__row+=1
    def writeToFile(self,data):
        #check if the file is created
        if(self.__workSheet==""):
            print("Document not created")
        else:
            #check the data and column header is same
            if(len(self.__columnHeaders)==len(data)):
                if(self.__row==0):
                        self.writeColumnHeaders()
                for index in range(len(data)):                    
                    print("Writing the value {}".format(data[index]))
                    self.__workSheet.write(self.__row,index,data[index])
                    
        self.__row+=1
    def closeFile(self):
        print("Closing the file")
        self.__excelFile.close()
            
                    
headers=["ayşe","fatma","hayriye","pembe"]

values1=[1,2,3,4]
values2=[5,6,7,8]

fileWriter=excelWriter("denemeExcel",headers)
fileWriter.writeToFile(values1)
fileWriter.writeToFile(values2)
fileWriter.closeFile()
