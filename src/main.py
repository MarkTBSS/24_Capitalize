s = "alison heck"
sResult = ''
sList = list(s)
print(sList)

for i in range(len(sList)):
    if (i == 0):
        sList[0] = sList[0].upper()
    elif (sList[i] == ' '):
        sList[i + 1] = sList[i + 1].upper()

sResult = ''.join(sList)
print(sResult)