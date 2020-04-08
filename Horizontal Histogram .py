# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 2018081 (IIT) W1790830 (UoW)
# Date: 02/03/2020



pass_mark=0 # Pass Mark variable
defer = 0 # Defer Mark variable
fail=0 # Fail Mark variable
retry=0  # This variable for contine or quit the program part


credit_range = [0,20,40,60,80,100,120] # Credits limitation values list
progress=[] # Progress Outcommers list
trailing=[] # Module Trailing List
retriver=[] # Module retrivers list
exclude=[] # Excluded student List
total_enters =[] # Total Mark Enters List

def main(): # Main Funtion

    print("Enter Student's marks here.") # Welcome note

    while True: # Input the pass mark and Check is it in integer format, Then genarate error
        try:
            pass_mark = int(input("Pass Mark : "))
            if pass_mark in credit_range: # Figure it out the all input data in correct range by credit range list
                break
            else:
                print("Sorry, Range Error.\n")
             
        except ValueError:
            print("Integers required!\n")

    while True: # Input the defer mark and Check is it in integer format, Then genarate error
        try:
            defer = int(input("Defer Mark : "))
            if defer in credit_range: # Figure it out the all input data in correct range by credit range list
                break
            else:
                print("Sorry, Range Error.\n")
        except ValueError:
            print("Integers required!\n")

    while True: # Input the fail mark and Check is it in integer format, Then genarate error
        try:
            fail = int(input("Fail Mark : "))
            if fail in credit_range: # Figure it out the all input data in correct range by credit range list
                break
            else:
                print("Sorry, Range Error.\n")
        except ValueError:
            print("Integers required!\n")

    total = pass_mark+defer+fail # Total of pass mark, defer and fail

    if total != 120: # Figure it out total == 120 or not
        print("Sorry, Total incorrect.")

    elif pass_mark == 120: # Progress outcommers
        print("\n")
        print("This candidate's progression outcome : Progress.")
        progress.append(pass_mark)
        total_enters.append(pass_mark)

    elif pass_mark == 100: # Module trailers
        print("\n")
        print("This candidate's progression outcome : Progress - module trailer.")
        trailing.append(pass_mark)
        total_enters.append(pass_mark)

    elif fail >=80: # Excluded students
        print("\n")
        print("This candidate's progression outcome : Exclude.")
        exclude.append(fail)
        total_enters.append(fail)

    else: # Module retrievers
        print("\n")
        print("This candidate's progression outcome : Do not Progress – module retriever")
        retriver.append(pass_mark)
        total_enters.append(pass_mark)

# Horizontal  H
def histogram():
    print("\n")
    print("-"*100)
    print("\n")
    print("Progress ",len(progress),":","* "*len(progress))
    print("\n")
    print("Trailing ",len(trailing),":", "* "*len(trailing))
    print("\n")
    print("Retriever ",len(retriver), ":", "* "*len(retriver))
    print("\n")
    print("Excluded ",len(exclude),":","* "*len(exclude))
    print("\n")
    print(len(total_enters), "Outcomes in Total.")
    print("\n")
    print("-"*100)

# User choice of continue or quit the program.
while True:
    try:
        retry = str(input("Enter 'C' to Continue and Enter 'Q' to Quit and histogram. Your Choice : "))
        retry=retry.upper()
        if retry=='Q' or retry=='C':
            if retry=='C':
                print("\n")
                main()
                print("\n")
            elif retry=='Q':
                histogram()
                break
        else:
            print("You entered wrong option. Try Again!\n")
            
    except:
        print()

    

