# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 2018081 (IIT) W1790830 (UoW)
# Date: 29/02/2020


pass_mark=0 # Pass Mark variable
defer = 0 # Defer Mark variable
fail=0 # Fail Mark variable
retry=0  # This variable for contine or quit the program part


credit_range = [0,20,40,60,80,100,120] # Credits limitation values list

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

    if pass_mark not in credit_range or defer not in credit_range or fail not in credit_range: # Figure it out the all input data in correct range by credit range list
        print("Sorry, Range Error.")

    elif total != 120: # Figure it out total == 120 or not
        print("Sorry, Total incorrect.")

    elif pass_mark == 120:
        print("\n")
        print("This candidate's progression outcome : Progress.")

    elif pass_mark == 100:
        print("\n")
        print("This candidate's progression outcome : Progress - module trailer.")

    elif fail >=80:
        print("\n")
        print("This candidate's progression outcome : Exclude.")

    else:
        print("\n")
        print("This candidate's progression outcome : Do not Progress – module retriever")


# User choice of continue or quit the program.
while True:
    try:
        retry = str(input("Enter 'C' to Continue and Enter 'Q' to Quit. Your Choice : "))
        retry=retry.upper()
        if retry=='Q' or retry=='C':
            if retry=='C':
                print("\n")
                main()
                print("\n")
            elif retry=='Q':
                exit()
        else:
            print("You entered wrong option. Try Again!\n")
            
    except:
        print()
    
