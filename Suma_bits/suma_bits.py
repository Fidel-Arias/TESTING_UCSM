# SPECIFICATION:
#
# add8 emulates an 8-bit hardware adder.
# it takes 17 bits, representing two 8-bit
# numbers and a carry bit.
#
# TASK:
#
# Write test() such that it achieves 100%
# statement coverage of the add8 function.
def add8(a0,a1,a2,a3,a4,a5,a6,a7,b0,b1,b2,b3,b4,b5,b6,b7,c0):
    # Bit 0
    xor0 = a0 != b0
    s1 = xor0 != c0
    c1 = (a0 and b0) or (c0 and xor0)
    
    # Bit 1
    xor1 = a1 != b1
    s2 = xor1 != c1
    c2 = (a1 and b1) or (c1 and xor1)
    
    # Bit 2
    xor2 = a2 != b2
    s3 = xor2 != c2
    c3 = (a2 and b2) or (c2 and xor2)
    
    # Bit 3
    xor3 = a3 != b3
    s4 = xor3 != c3
    c4 = (a3 and b3) or (c3 and xor3)
    
    # Bit 4
    xor4 = a4 != b4
    s5 = xor4 != c4
    c5 = (a4 and b4) or (c4 and xor4)
    
    # Bit 5
    xor5 = a5 != b5
    s6 = xor5 != c5
    c6 = (a5 and b5) or (c5 and xor5)
    
    # Bit 6
    xor6 = a6 != b6
    s7 = xor6 != c6
    c7 = (a6 and b6) or (c6 and xor6)
    
    # Bit 7 (MSB)
    xor7 = a7 != b7
    s8 = xor7 != c7
    c8 = (a7 and b7) or (c7 and xor7)
    
    return (s1, s2, s3, s4, s5, s6, s7, s8, c8)