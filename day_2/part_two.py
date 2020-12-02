def validate(cone, ctwo, char, pword):
    return (pword[cone - 1] == char) ^ (pword[ctwo - 1] == char)

def main():
    valid = 0
    
    with open('002_input.txt') as f:
        for line in f:
            parts = line.split(' ')
            cmin, cmax = map(int, parts[0].split('-'))
            char = parts[1][0]
            pword  = parts[2]
            
            if validate(cmin, cmax, char, pword):
                valid += 1
    
    print('Valid passwords count: {}'.format(valid))

if __name__ == '__main__':
    main()