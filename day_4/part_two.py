import sys
from re import match

ecl = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])

vs = {
    'byr': lambda v: 1920 <= int(v) <= 2002,
    'iyr': lambda v: 2010 <= int(v) <= 2020,
    'eyr': lambda v: 2020 <= int(v) <= 2030,
    'hcl': lambda v: match(r'^#[\da-f]{6}$', v),
    'ecl': lambda v: v in ecl,
    'pid': lambda v: match(r'^\d{9}$', v),
    'hgt': lambda v: (v[-2:] == 'in' and 59 <= int(v[:-2]) <= 76) or (v[-2:] == 'cm' and 150 <= int(v[:-2]) <= 193)
}

def is_valid(p):
    return set(vs).issubset(p) and all(vs[f](p[f]) for f in vs)


def main():
    with open(sys.argv[1]) as f:
        passports = [p.replace(' ', '\n') for p in f.read().split('\n\n')]
        passports = [dict(f.split(':') for f in p.split('\n')) for p in passports]

    print('Valid count is {}'.format(sum(is_valid(p) for p in passports)))

if __name__ == '__main__':
    main()