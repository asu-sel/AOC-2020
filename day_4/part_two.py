import sys
from re import match

fs = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
ecl = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])

def is_valid(p):
    vrange = lambda minv, maxv, v: int(v) and minv <= int(v) <= maxv

    if not all(x in p for x in fs): return False 

    if not vrange(1920, 2002, p['byr']): return False

    if not vrange(2010, 2020, p['iyr']): return False

    if not vrange(2020, 2030, p['eyr']): return False

    if not (pat := match(r'^(\d{2,3})(cm|in)$', p['hgt'])): return False
    if pat[2] == 'in' and not vrange(59, 76, pat[1]): return False
    if pat[2] == 'cm' and not vrange(150, 193, pat[1]): return False

    if not match(r'#[\da-f]{6}$', p['hcl']): return False

    if p['ecl'] not in ecl: return False

    if not match(r'^\d{9}$', p['pid']): return False

    return True


def main():
    with open(sys.argv[1]) as f:
        passports = [p.replace(' ', '\n') for p in f.read().split('\n\n')]
        passports = [dict(f.split(':') for f in p.split('\n')) for p in passports]
    
    count = 0
    for p in passports: count += is_valid(p)
    
    print('Valid count is {}'.format(count))

if __name__ == '__main__':
    main()