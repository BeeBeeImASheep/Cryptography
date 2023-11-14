L1 = int(input("L1 : "))
R1 = int(input("R1 : "))
K1 = int(input("K1 : "))
K2 = int(input("K2 : "))

L2 = R1
f = R1 ^ K1
R2 = L1 ^ f
L3 = R2
f = R2 ^ K2
R3 = L2 ^ f
print("L1 : " + format(L1, '04b') + " L2 : " + format(R1, '04b') + " K1 : " + format(K1, '04b') + " K2 : " + format(K2, '04b'))
print("L2 : " + format(L2, '04b') + " R2 : " + format(R2, '04b'))
print("L3 : " + format(L3, '04b') + " R3 : " + format(R3, '04b'))
print("L4 : " + format(L3, '04b') + " R4 : " + format(R3, '04b'))
R5 = L3
f = L3 ^ K2
L5 = R3 ^ f
R6 = L5
f = L5 ^ K1
L6 = R5 ^ f
print("L5 : " + format(L5, '04b') + " R5 : " + format(R5, '04b'))
print("L6 : " + format(L6, '04b') + " R6 : " + format(R6, '04b'))
