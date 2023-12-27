year = int (input ("which year do you want to check?\n"))
if year % 4 == 0:
    print ("leap year")
elif year % 100 == 0:
    print("leap year")
elif year % 400 == 0:
    print('leap year')
else:
    print("not leap year")
        
        
            
