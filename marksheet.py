class Marksheet:
    def __init__(self,name,no_of_subject):
        self.name=name
        self.no_of_subject=no_of_subject
        self.subjectlist=[]
    def addmarksandsubject(self,subject,mark):
        #create the dictionary from subject and marks
        #add the dictionary in the subjectlist
        for i in range(self.no_of_subject):
            dict={'subject':subject[i],'mark':mark[i]}
            self.subjectlist.append(dict)

    def calculatePercentage(self):
        #get the marks if all subject from the subject list
        #calculate the percentage
        #the total marks for the subject is 100
        result=0
        for i in range(len(self.subjectlist)):
            a=int(self.subjectlist[i]['mark'])
            #print(a)
            result=result+a
        percent=result/len(self.subjectlist)
        #print(percent)
        return percent

    #map(lambda subject: result + int(dict['mark'], self.subjectlist))


    def findDivision(self):
        #calculate division on the basis of percentage
        percentage = self.calculatePercentage()
        if(percentage>=80):
            print("Distinction")
        elif(percentage>=60 and percentage<80 ):
            print("First Division")
        elif(percentage>=40 and percentage<60):
            print("Second Division")
        else:
            print("Third Division")


name=input("enter the name of the student:")
n=int(input("enter the no of subjects:"))
subject=[]
mark=[]
studmark=Marksheet(name,n)
for i in range(1,n+1):
    sub=input("enter the subject:")
    marks=input("enter the marks:")
    subject.append(sub)
    mark.append(marks)

studmark.addmarksandsubject(subject,mark)
print('{} has got {}%'.format(name,studmark.calculatePercentage()))
studmark.findDivision()



