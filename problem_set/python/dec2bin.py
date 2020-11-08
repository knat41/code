'''FILE    : Hex Oct Bin to Dec
   WRITER  : NAT KANJANASIRI
   DATE    : OCT 16, 2020
   PURPOSE : Convert base 2, 8, 16 to base 10'''
number = int(input("Enter number : "))
obase = ''
while(number > 0):        
        obase = str(number % 2) + obase
        number = number // 2
print(obase)
