#String Slicing
note="Hei! Olen suomalainen sopiskelija. Entä sinulle?"
testStr="Mika, Kasonen, Atte, Saranen, Zaman"
commaStr=testStr.index(",")
print(testStr[0:commaStr])
print(note[0:2])
print(note[2:9:2])
print(note[-7:-2])
print(note[::-1])
