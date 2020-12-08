import sys

ACC = 'acc'
JMP = 'jmp'
NOP = 'nop'

def intcode(cmds):
    executed = set()
    a = 0
    i = 0
    r = False

    while i < len(cmds):
        if i in executed: 
            r = True
            break
        executed.add(i)

        cmd, n = cmds[i]
        if cmd == ACC:
            a += n
        if cmd == JMP:
            i += n - 1
        if cmd == NOP:
            pass
        
        i += 1
    
    return a, r

def main():
    with open(sys.argv[1]) as f:
        cmds = [l.split(' ') for l in f.read().splitlines()]
        cmds = [(c, int(n)) for c, n in cmds]

    switch = {'nop': 'jmp', 'jmp': 'nop'}
    for i, (cmd, n) in enumerate(cmds):
        if cmd in switch.keys():
            a, r = intcode(cmds[:i] + [(switch[cmd], n)] + cmds[i+1:])
            if not r:
                print(f'Accumulator value is {a}')


if __name__ == '__main__':
    main()