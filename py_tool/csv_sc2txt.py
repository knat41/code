# -*- coding: cp874 -*-
"""
PROGRAM : convert csv file to utm
DATE : first version 2015/02/17 20:00:00
     : current version 2018/09/24 22:44:00
PROGRAMER : NAT KANJANASIRI
   
subjectcode_UM01_1.txt
subjectcode_UM02_1.txt
subjectcode_UM03_1.txt
subjectcode_UM04_1.txt
subjectcode_UM05_1.txt
subjectcode_UM06_1.txt
subjectcode_midtermmark_1.txt
subjectcode_finalmark_1.txt

Command line usage:
$ python csv2utm.py noun
nouns
"""

__author__ = "Nat Kanjanasiri (kanjanasiri@gmail.com)"
__version__ = "$Revision: 0.2 $"
__date__ = "$Date: 2015/02/17 20:00:00 $"
__copyright__ = "Copyright (c) 2015 Nat Kanjanasiri"
__license__ = "Python"

#
import csv
import os

#define variable
# ans use for answer key and scoretxt for list of score
# ans 10 point
# '00000' that mean answer sheet
ans_unit1 = {}
ans_unit2 = {}
ans_unit3 = {}
ans_unit4 = {}
ans_unit5 = {}
ans_unit6 = {}

scoretxt = {'0':'2222222222', '1':'1222222222', '2':'1122222222',
            '3':'1112222222', '4':'1111222222', '5':'1111122222',
            '6':'1111112222', '7':'1111111222', '8':'1111111122',
            '9':'1111111112', '10':'1111111111'}

# answer 20 point
ans_mid   = {}
ans_final = {}
scores20 = {'0':'22222222222222222222', '1':'12222222222222222222',
            '2':'11222222222222222222', '3':'11122222222222222222',
            '4':'11112222222222222222', '5':'11111222222222222222',
            '6':'11111122222222222222', '7':'11111112222222222222',
            '8':'11111111222222222222', '9':'11111111122222222222',
            '10':'11111111112222222222', '11':'11111111111222222222',
            '12':'11111111111122222222', '13':'11111111111112222222',
            '14':'11111111111111222222', '15':'11111111111111122222',
            '16':'11111111111111112222', '17':'11111111111111111222',
            '18':'11111111111111111122', '19':'11111111111111111112',
            '20':'11111111111111111111'}

#control variable
input_file  ='m4.csv'
output_file_u1 = '_UM01_1.txt'
output_file_u2 = '_UM02_1.txt'
output_file_u3 = '_UM03_1.txt'
output_file_u4 = '_UM04_1.txt'
output_file_u5 = '_UM05_1.txt'
output_file_u6 = '_UM06_1.txt'
output_file_mid = '_MIDTERMMARK_1.txt'
output_file_fin = '_FINALMARK_1.txt'

answer = 10

if(answer == 10):
    with open(input_file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ans_unit1[row['id']] = scoretxt[row['s1']]
            ans_unit2[row['id']] = scoretxt[row['s2']]
            ans_unit3[row['id']] = scoretxt[row['s3']]
            ans_unit4[row['id']] = scoretxt[row['s4']]
            ans_unit5[row['id']] = scoretxt[row['s5']]
            ans_unit6[row['id']] = scoretxt[row['s6']]
            ans_mid[row['id']] = scores20[row['mid']]
            ans_final[row['id']] = scores20[row['fin']]

    print 'Done for read file, And preparing to write file'
    print 'Please wait!!!'

"""==================== Unit 1 ===================="""
if os.path.exists(output_file_u1):
    f = open(output_file_u1, 'r+')
    f.write('00000' + ' ' + '1111111111'+'\n')
    for k, v in ans_unit1.iteritems():
        f.write(k + ' ' + v +'\n')
        
    f.close()
    print 'Write file' + output_file_u1 + ' Done'
else:
    f = open(output_file_u1, 'w')
    f.write('00000' + ' ' + '1111111111'+'\n')
    for k, v in ans_unit1.iteritems():
        f.write(k + ' ' + v +'\n')

    f.close()
    print 'Create file ' + output_file_u1 + ' Done'

"""==================== Unit 2 ===================="""
if os.path.exists(output_file_u2):
    f = open(output_file_u2, 'r+')
    f.write('00000' + ' ' + '1111111111'+'\n')
    for k, v in ans_unit2.iteritems():
        f.write(k + ' ' + v +'\n')

    f.close()
    print 'Write file' + output_file_u2 + ' Done'
else:
    f = open(output_file_u2, 'w')
    f.write('00000' + ' ' + '1111111111'+'\n')
    for k, v in ans_unit2.iteritems():
        f.write(k + ' ' + v +'\n')

    f.close()
    print 'Create file ' + output_file_u2 + ' Done'

"""==================== Unit 3 ===================="""
if os.path.exists(output_file_u3):
    f = open(output_file_u3, 'r+')
    f.write('00000' + ' ' + '1111111111'+'\n')
    for k, v in ans_unit3.iteritems():
        f.write(k + ' ' + v +'\n')

    f.close()
    print 'Write file' + output_file_u3 + ' Done'
else:
    f = open(output_file_u3, 'w')
    f.write('00000' + ' ' + '1111111111'+'\n')
    for k, v in ans_unit3.iteritems():
        f.write(k + ' ' + v +'\n')

    f.close()
    print 'Create file ' + output_file_u3 + ' Done'

"""==================== Unit 4 ===================="""
if os.path.exists(output_file_u4):
    f = open(output_file_u4, 'r+')
    f.write('00000' + ' ' + '1111111111'+'\n')
    for k, v in ans_unit4.iteritems():
        f.write(k + ' ' + v +'\n')

    f.close()
    print 'Write file' + output_file_u4 + ' Done'
else:
    f = open(output_file_u4, 'w')
    f.write('00000' + ' ' + '1111111111'+'\n')
    for k, v in ans_unit4.iteritems():
        f.write(k + ' ' + v +'\n')

    f.close()
    print 'Create file ' + output_file_u4 + ' Done'

"""==================== Unit 5 ===================="""
if os.path.exists(output_file_u5):
    f = open(output_file_u5, 'r+')
    f.write('00000' + ' ' + '1111111111'+'\n')
    for k, v in ans_unit5.iteritems():
        f.write(k + ' ' + v +'\n')

    f.close()
    print 'Write file' + output_file_u5 + ' Done'
else:
    f = open(output_file_u5, 'w')
    f.write('00000' + ' ' + '1111111111'+'\n')
    for k, v in ans_unit5.iteritems():
        f.write(k + ' ' + v +'\n')

    f.close()
    print 'Create file ' + output_file_u5 + ' Done'

"""==================== Unit 6 ===================="""
if os.path.exists(output_file_u6):
    f = open(output_file_u6, 'r+')
    f.write('00000' + ' ' + '1111111111'+'\n')
    for k, v in ans_unit6.iteritems():
        f.write(k + ' ' + v +'\n')

    f.close()
    print 'Write file' + output_file_u6 + ' Done'
else:
    f = open(output_file_u6, 'w')
    f.write('00000' + ' ' + '1111111111'+'\n')
    for k, v in ans_unit6.iteritems():
        f.write(k + ' ' + v +'\n')

    f.close()
    print 'Create file ' + output_file_u6 + ' Done'


"""==================== MidTerm EXAM ===================="""
if os.path.exists(output_file_mid):
    f = open(output_file_mid, 'r+')
    f.write('00000' + ' ' + '11111111111111111111'+'\n')
    for k, v in ans_mid.iteritems():
        f.write(k + ' ' + v +'\n')

    f.close()
    print 'Write file' + output_file_mid + ' Done'
else:
    f = open(output_file_mid, 'w')
    f.write('00000' + ' ' + '11111111111111111111'+'\n')
    for k, v in ans_mid.iteritems():
        f.write(k + ' ' + v +'\n')

    f.close()
    print 'Create file ' + output_file_mid + ' Done'

"""==================== Fianl EXAM ===================="""
if os.path.exists(output_file_fin):
    f = open(output_file_fin, 'r+')
    f.write('00000' + ' ' + '11111111111111111111'+'\n')
    for k, v in ans_final.iteritems():
        f.write(k + ' ' + v +'\n')

    f.close()
    print 'Write file' + output_file_fin + ' Done'
else:
    f = open(output_file_fin, 'w')
    f.write('00000' + ' ' + '11111111111111111111'+'\n')
    for k, v in ans_final.iteritems():
        f.write(k + ' ' + v +'\n')

    f.close()
    print 'Create file ' + output_file_fin + ' Done'

