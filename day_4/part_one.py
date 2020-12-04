import sys

fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

def is_valid(p):
    return fields.issubset(p)


def main():
    with open(sys.argv[1]) as f:
        passports = [p.replace(' ', '\n') for p in f.read().split('\n\n')]
        passports = [dict(f.split(':') for f in p.split('\n')) for p in passports]
    
    print('Valid count is {}'.format(sum(is_valid(p) for p in passports)))

if __name__ == '__main__':
    main()