# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 2018081 (IIT) W1790830 (UoW)
# Date: 10/03/2020

progress=[] # Progress Outcommers list
trailing=[] # Module Trailing List
retriver=[] # Module retrivers list
exclude=[] # Excluded student List
total_enters =[] # Total Mark Enters List

# Student 01 Dictionary
student1={
    "Pass":120
}

# Student 02 Dictionary
student2={
    "Pass": 100 ,
    "Defer": 20
}

# Student 03 Dictionary
student3={
    "Pass": 80 ,
    "Defer": 20 ,
    "Fail" : 20
}

# Student 04 Dictionary
student4={
    "Pass": 60 ,
    "Defer": 40 ,
    "Fail" : 20
}

# Student 05 Dictionary
student5={
    "Pass": 40 ,
    "Defer": 40 ,
    "Fail" : 40
}

# Student 06 Dictionary
student6={
    "Pass": 20 ,
    "Defer": 40 ,
    "Fail" : 60
}

# Student 07 Dictionary
student7={
    "Pass": 20 ,
    "Fail" : 100
}

# Student 08 Dictionary
student8={
    "Fail" : 120
}

# Progress level Checking Funtion 
def checker(student):

    if student.get("Pass")==120:
        print("This candidate's progression outcome : Progress.\n")
        progress.append(student.get("Pass"))
        total_enters.append(student.get("Pass"))

    elif student.get("Pass")==100:
        print("This candidate's progression outcome : Progress - module trailer.\n")
        trailing.append(student.get("Pass"))
        total_enters.append(student.get("Pass"))

    elif student.get("Fail") >=80:
        print("This candidate's progression outcome : Exclude.\n")
        exclude.append(student.get("Fail"))
        total_enters.append(student.get("Fail"))
    else:
        print("This candidate's progression outcome : Do not Progress – module retriever\n")
        retriver.append(student.get("Fail"))
        total_enters.append(student.get("Fail"))


# Funtion Callings
checker(student1)
checker(student2)
checker(student3)
checker(student4)
checker(student5)
checker(student6)
checker(student7)
checker(student8)

# Vertical histogram
length_progress= len(progress)
length_trailing= len(trailing)
length_retriever= len(retriver)
length_exclude= len(exclude)

max_value=max(length_progress,length_trailing,length_retriever,length_exclude)

print('-'*60)
print("Progress \t Trailing \t Retriever \t Excluded")

for i in range(max_value):
    if length_progress!=0:
        print("   *", end="\t")
        print(end='\t')
        length_progress-=1
    else:
        print(" ",end="\t")
        print(end='\t')
    
    if length_trailing!=0:
        print("    *",end="\t")
        print(end='\t')
        length_trailing-=1
    else:
        print(" ",end="\t")
        print(end='\t')

    if length_retriever!=0:
        print("    *",end="\t")
        print(end='\t')
        length_retriever-=1
    else:
        print(" ",end="\t")
        print(end='\t')
    
    if length_exclude!=0:
        print("    *",end="\t")
        print(end='\t')
        length_exclude-=1
    else:
        print(" ",end="\t")
        print(end='\t')
    print()

print("\n")
print('-'*60)




