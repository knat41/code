base = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
number = int(input("Enter number : "))
cbase = int(input("To base : "))
if number == 0:
    obase = str(number)
else:
    obase = ''
while(number > 0):        
        obase = base[number % cbase] + obase
        number = number // cbase
print(obase)