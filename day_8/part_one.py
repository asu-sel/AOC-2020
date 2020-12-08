import sys

ACC = 'acc'
JMP = 'jmp'
NOP = 'nop'

def intcode(cmds):
    executed = set()
    a = 0
    i = 0

    while i < len(cmds):
        if i in executed:
            break
        executed.add(i)

        cmd, n = cmds[i]
        if cmd == ACC:
            a += n
            i += 1
        if cmd == JMP:
            i += n
        if cmd == NOP:
            i += 1
    
    return a

def main():
    with open(sys.argv[1]) as f:
        cmd = [l.split(' ') for l in f.read().splitlines()]
        cmd = [(c, int(n)) for c, n in cmd]
    
    print(f'Accumulator value is {intcode(cmd)}')

if __name__ == '__main__':
    main()