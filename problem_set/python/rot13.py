message = input()
rot = ''
for c in message:
    if ord(c) > 64 and ord(c) < 78:
        rot = rot + chr(ord(c) + 13)
    elif ord(c) > 77 and ord(c) < 91:
        rot = rot + chr(ord(c) - 13)
    elif ord(c) > 96 and ord(c) < 110:
        rot = rot + chr(ord(c) + 13)
    elif ord(c) > 109 and ord(c) < 123:
        rot = rot + chr(ord(c) - 13)
    else:
        rot = rot + c

print(rot)
