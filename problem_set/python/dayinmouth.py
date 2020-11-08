'''PROGRAM : Day in Mouth
   WRITER  : NAT KANJANASIRI
   DATE    : OCT 16, 2020
   PURPOSE : '''
month, year = [int(x) for x in input().split()]
day_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
ad = year - 543
if( (ad % 4 == 0 and ad % 100 != 0) or ad % 400 == 0):
    day_in_month[2] = 29    
print("{}".format(day_in_month[month]))
