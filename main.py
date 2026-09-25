
####################### CALCULATOR CODE ##################################
print("whats good homeboy")
print("what we doing")
def add (x,y):
    print(x+y)
def multiply (x,y):
    print (x*y)
def divide (x,y):
    print(x/y)
def subtract (x,y):
    print(x-y)
while(True):
    print("type (a)dd s(subtract) (m)ultiply (d)ivide (q)uit)")
    user_choice = input(":")
#add
    if user_choice == "a":
        x=int(input("first #"))
        y=int(input("second #"))
        add(x,y) 

#subtract
    elif user_choice == "s":
        x=int(input("first #"))
        y=int(input("second #"))
        subtract(x,y)

#multiply
    elif user_choice == "m":
        x=int(input("first #"))
        y=int(input("second #"))
        multiply(x,y)

#divide
    elif user_choice == "d":
        x=int(input("first #"))
        y=int(input("second #"))
        divide(x,y)

    elif user_choice == 'q':
        break
    else:
        print("stupid you cant do that")



