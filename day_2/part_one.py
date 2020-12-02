def validate(cmin, cmax, char, pword):
    count = pword.count(char)
    return count >= cmin and count <= cmax

def main():
    valid = 0
    
    with open('002_input.txt') as f:
        for line in f:
            parts = line.split(' ')
            cmin, cmax = map(int, parts[0].split('-'))
            letter = parts[1][0]
            pword  = parts[2]
            
            if validate(cmin, cmax, letter, pword):
                valid += 1
    
    print('Valid passwords count: {}'.format(valid))

if __name__ == '__main__':
    main()