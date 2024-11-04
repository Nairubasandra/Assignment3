#Assignment
#Qn1
#print Patricia ,Faith,Phionah,and Anitah
studentNames=['Sandra','Patricia','Phionah','Anitah']
studentMarks=[80,56.78,90]
studentNames.insert(2,"Faith")
studentNames.remove("Sandra")
print(studentNames)


#Qn2
#Add Masha at the forth position 
studentNames.insert(3,"Masha")
print(studentNames)


#Qn3
#Update the name Phionah to Phionah Aladina
studentNames[studentNames.index("Phionah")]="Phionah Aladina"
print(studentNames)


#Qn4
#Display the length of the students list
print(f"The length of the student list is :{len(studentNames)}")

#Qn5
#Print all the student names using a for loop
for names in studentNames:
    print(names)


#Qn6    
# calculate the total marks for the student marks variable#ans304
totalMarks = sum(studentNames)
print(totalMarks)