'''PROGRAM : Separate Comma
   WRITER  : NAT KANJANASIRI
   DATE    : JAN 30, 2023
   PURPOSE : '''
number = int(input())
answer = ''
while number > 0:
    remainder = number % 1000
    number = number // 1000
    if number > 0 and remainder == 0:
        answer = ',' + '000' + answer
    elif number > 0 and remainder != 0:
        answer = ',' + str(remainder) + answer
    else:
        answer = str(remainder) + answer
print(answer)