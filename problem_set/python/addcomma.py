'''PROGRAM : Separate Comma
   WRITER  : NAT KANJANASIRI
   DATE    : JUN 21, 2021
   PURPOSE : '''
number = input()
output = ''
n = len(number)
for i in range(-1, -(n + 1), -1):
    output = number[i] + output
    if i % 3 == 0 and i != -n:
        output = ',' + output
print(output)
