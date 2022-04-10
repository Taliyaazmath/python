#calculator using if conditions only

while True:
    n1=float(input("enter the first number:"))
    n2=float(input("enter the second number:"))


    print("here are your choices")

    a="""
    enter 1 for addition,
    enter 2 for subtraction
    enter 3 for multiplication
    enter 4 for division
    enter 5 for modulus
    enter 6 for exponential
    enter 7 for floor division.
    """
    print(a)

    con=True
    while con :
        choice= int(input("enter your choice:"))
        if choice<=7:
            if choice==1:
                print(n1+n2)
            if choice==2:
                print(n1-n2)
            if choice==3:
                print(n1*n2)
            if choice==4:
                print(n1/n2)
            if choice==5:
                print(n1%n2)
            if choice==6:
                print(n1**n2)
            if choice==7:
                print(n1//n2)
        else:
            print("please enter only the numbers from the given choice")

        con=input("enter (yes/no) if you want to use other operator:")
        if con=="yes":
            con=True
        elif con=="no":
            con=False

    num_change=input("do you wish to change the number values(yes/no):")
    if num_change=="yes":
        continue
    elif num_change=="no":
        break


