class MachineCodeError(Exception):
    pass

def binary(x):
    return bin(x)[2:]

def chunk(seq, size):
    return (seq[pos:pos + size] for pos in xrange(0, len(seq), size))

def execute(code, regs=[]):

    if not regs:
        i=0
        while i<65535:
            regs.append(0)
            i+=1

    instructions=[]

    if len(code)%5 != 0:
        raise MachineCodeError('code is malformed (len%5 != 0')

    for x in chunk(raw, 5):
        prim = []
        for y in x:
            prim.append(ord(y))#
        instructions.append((prim[0], int(binary(prim[1])+binary(prim[2]), 2), int(binary(prim[3])+binary(prim[4]), 2)))#Generate Tuple and add it to list

    for x in instructions:
        c=x[0]
        a1=x[1]
        a2=x[2]
        
        if c == 0: #NIL instruction: Does nothing
            pass
        
        elif c == 1: #SET instruction: Sets a registry to a value
            regs[a1] = a2
            
        elif c == 2: #COP instruction: copy one registry to another
            regs[a1] = regs[a2]
            
        elif c == 3: #ADD instruction: Add one registry to another
            regs[a1] = (regs[a1]+regs[a2])%65536

        elif c == 4: #SUB instruction: Subtract one registry from another
            regs[a1] = (regs[a1]-regs[a2])%65536

        elif c == 5: #MUL instruction: Multiply one resistry by another
            regs[a1] = (regs[a1]*regs[a2])%65536

        elif c == 6: #DIV instruction: Floor divide one registry by another
            regs[a1] = (regs[a1]//regs[a2])%65536
            
        elif c == 7: #GRE instruction: reg1 to 1 if reg1>reg2, else 0
            regs[a1] = int(regs[a1]>regs[a2])
            
        elif c == 8: #LES instruction: reg1 to 1 if reg1<reg2, else 0
            regs[a1] = int(regs[a1]<regs[a2])
            
        elif c == 9: #EQU instruction: reg1 to 1 if reg1=reg2, else 0
            regs[a1] = int(regs[a1]==regs[a2])
            
        elif c == 10: #LSH instruction: bitwise left shift reg1 by reg2
            regs[a1] = regs[a1]<<regs[a2]
            
        elif c == 11: #RSH instruction: bitwise right shift reg1 by reg2
            regs[a1] = regs[a1]>>regs[a2]
            
        elif c == 12: #AND instruction: bitwise and reg1 by reg2
            regs[a1] = regs[a1]&regs[a2]
            
        elif c == 13: #ORR instruction: bitwise or reg1 by reg2
            regs[a1] = regs[a1]|regs[a2]
            
        elif c == 14: #XOR instruction: bitwise xor reg1 by reg2
            regs[a1] = regs[a1]^regs[a2]

        elif c == 15: #NND instruction: bitwise nand reg1 by reg2
            regs[a1] = ~(regs[a1]&regs[a2])

        elif c == 16: #NOR instruction: bitwise nor reg1 by reg2
            regs[a1] = ~(regs[a1]|regs[a2])

        elif c == 17: #XNR instruction: bitwise xnor reg1 by reg2
            regs[a1] = ~(regs[a1]^regs[a2])
        elif c == 18: #NEG instruction: bitwise negate reg1
            regs[a1] = ~regs[a1]
