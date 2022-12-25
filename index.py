# we are given table which is included 4 students and there degrees in math,science,arabic,com.
#first Q:to find the percentage of degrees for each student anf if any one was absent in any subject don't view his/her percent

dict={"ahmed":{
"math":80,
"science":65,
"Arabic":75,
"com":60
},
"ali":{
"math":65,
"science":80,
"Arabic":65,
"com":80
},
"soha":{"math":90,
"science":55,
"Arabic":88,
"com":77

},
"aya":{
"math":48,
"science":"absent",
"Arabic":60,
"com":65
}
}

for i in dict:
   sum=0
   if dict[i]["math"]=="absent" or dict[i]["science"]=="absent"or dict[i]["Arabic"]=="absent" or dict[i]["com"]=="absent":
        print("\n")
   else :
        sum=dict[i]["math"]+dict[i]["science"]+dict[i]["Arabic"]+dict[i]["com"]
        percent=(sum/4)
        print (percent)
        
        
        
#sec Q:create a function to take a subject name then retrieve the student's data in descending order by their degrees .     
        
def fun(subject):
  student_data = {
    'math': [('Ahmed', 80), ('Ali', 65), ('Soha', 90), ('Aya', 48)],
    'science': [('Ahmed', 95), ('Ali', 80), ('Soha', 55), ('Aya', 'Absent')],
    'arabic': [('Ahmed', 75), ('Ali', 65), ('Soha', 88), ('Aya', 80)],
    'com': [('Ahmed', 60), ('Ali', 80), ('Soha', 70), ('Aya', 65)]
  }
  subject_data = student_data[subject]
  sorted_data = sorted(subject_data, key=lambda x: x[1], reverse=True)
  for i in sorted_data:
     print (i)

fun('math')

#third Q: create a function to find the students who achieve the high score in a particular subject.

def highest_score(subject):
    highest_score = 0
    highest_student = ""
    if subject == "math":
        if dict["ahmed"]["math"] > highest_score:
            highest_score = dict["ahmed"]["math"]
            x="ahmed"
        if dict["ali"]["math"] > highest_score:
            highest_score = dict["ali"]["math"]
            x="ali"
        if dict["soha"]["math"] > highest_score:
            highest_score = dict["soha"]["math"]
            x=  "soha"
        if dict["aya"]["math"] > highest_score:
            highest_score = dict["aya"]["math"]
            x= "aya"
    elif subject == "science":
        if dict["ahmed"]["science"] > highest_score:
            highest_score = dict["ahmed"]["science"]
            x= "ahmed"
        if dict["ali"]["science"] > highest_score:
            highest_score = dict["ali"]["science"]
            x= "ali"
        if dict["soha"]["science"] > highest_score:
            highest_score = dict["soha"]["science"]
            x= "soha"
        if dict["aya"]["science"] > highest_score:
            highest_score = dict["aya"]["science"]
            x  = "aya"

    elif subject=="arabic":
           if dict["ahmed"]["arabic"] > highest_score:
               highest_score = dict["ahmed"]["arabic"]
               x=  "ahmed"
           if dict["ali"]["arabic"] > highest_score:
               highest_score = dict["ali"]["arabic"]
               x=  "ali"
           if dict["soha"]["arabic"] > highest_score:
               highest_score = dict["soha"]["arabic"]
               x= "soha"
           if dict["aya"]["arabic"] > highest_score:
              highest_score = dict["aya"]["arabic"]
              x="aya"
       
    elif subject =="com":
        if dict["ahmed"]["com"] > highest_score:
            highest_score = dict["ahmed"]["com"]
            x= "ahmed"
        if dict["ali"]["com"] > highest_score:
            highest_score = dict["ali"]["com"]
            x= "ali"
        if dict["soha"]["com"] > highest_score:
            highest_score = dict["soha"]["com"]
            x="soha"
        if dict["aya"]["com"] > highest_score:
            highest_score = dict["aya"]["com"]
            x=  "aya"
    return x

print (highest_score("math"))


#Apply OOP concepts to simulate the previous table.

class student:
  def init (self,name,math_score,science_score,arabic_score,com_score):
         self.name=name
         self.math_score=math_score
         self.science_score=science_score
         self.arabic_score=arabic_score
         self.com_score=com_score
  def show(self):
     return f"my name is {self.name} and i have {self.math_score} in math and i have {self.science_score} in science and i have {self.arabic_score} in Arabic and finally in com i have got {self .com_score}"
