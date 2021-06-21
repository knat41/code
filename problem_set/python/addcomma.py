'''PROGRAM : Separate Comma
   WRITER  : NAT KANJANASIRI
   DATE    : OCT 16, 2020
   PURPOSE : '''
number = input()
output = ''
n = len(number)
for i in range(-1, -(n + 1), -1):
    output = number[i] + output
    if i % 3 == 0 and i != -n:
        output = ',' + output
print(output)
