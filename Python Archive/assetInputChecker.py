checklist = []
for i in "30934":
    if i.upper() in '1234567890':
        checklist.append('GREEN')
    else:
        checklist.append('RED')
if 'RED' in checklist:
    print('ABORT')
else:
    print('GREEN across the board')