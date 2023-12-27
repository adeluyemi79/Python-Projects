print ("welcome to python pizza Deliveries")
size = input (" what size of pizza do you want?\n S, M or L?\n")
add_pepperoni = input ("Do you want pepperoni?\n Y or N?\n" )
extra_cheese = input ("Do you want extra cheese?\n Y or N?\n")
bill = 0
if size == "s":
    bill +=15
elif size == "M":
    bill +=20
else:
    bill +=25
if add_pepperoni == "Y":
    bill +=2
if extra_cheese == "Y":
    bill +=1
    print (f" your final bill is $ {bill}")


