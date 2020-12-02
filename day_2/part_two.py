import re

def validate(cone, ctwo, char, pword):
    return (pword[cone - 1] == char) ^ (pword[ctwo - 1] == char)

def main():
    valid = 0
    
    with open('002_input.txt') as f:
        for line in f:
            pattern = re.search('(\d+)-(\d+) (\w): (\w+)', line)
            parts = line.split(' ')
            cmin = int(pattern[1])
            cmax = int(pattern[2])
            char = pattern[3]
            pword = pattern[4]
            
            if validate(cmin, cmax, char, pword):
                valid += 1
    
    print('Valid passwords count: {}'.format(valid))

if __name__ == '__main__':
    main()