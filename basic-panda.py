import pandas as py

Student_data1={'student1':['java', 'c', 'c++', 'linux'], 'student2': ['python', 'html','javascript','linux'],
              'student3':['neo4j','perl', 'github', 'panda']}
Student_data2={'student1':['java', 'c', 'c++', 'linux'], 'student2': ['python', 'html','javascript','linux'],
              'student3':['neo4j','perl', 'github', 'panda']}

data1 =py.DataFrame(Student_data1)
data2=py.DataFrame(Student_data2)

print data1

#slicing

print data1.head(2)
print data1.tail(2)

#Merge

merge=py.merge(data1,data2,on="student1")
print merge
