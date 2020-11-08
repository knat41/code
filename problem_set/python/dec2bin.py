'''PROGRAM : DEC to BIN
   WRITER  : NAT KANJANASIRI
   DATE    : OCT 16, 2020
   PURPOSE : Convert base 10 to base 2'''
number = int(input("Enter number : "))
obase = ''
while(number > 0):        
        obase = str(number % 2) + obase
        number = number // 2
print(obase)
