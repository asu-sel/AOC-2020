import sys

fs = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

def is_valid(p):
    return all(x in p for x in fs)


def main():
    with open(sys.argv[1]) as f:
        passports = [p.replace(' ', '\n') for p in f.read().split('\n\n')]
        passports = [dict(f.split(':') for f in p.split('\n')) for p in passports]
    
    count = 0
    for passport in passports:
        count += is_valid(passport)
    
    print('Valid count is {}'.format(count))

if __name__ == '__main__':
    main()