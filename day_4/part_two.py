import sys
from re import match

fs = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

def is_valid(p):
    if not all(x in p for x in fs): return False 
    
    if not 1920 <= int(p['byr']) <= 2002: return False

    if not 2010 <= int(p['iyr']) <= 2020: return False

    if not 2020 <= int(p['eyr']) <= 2030: return False

    pat = match('^(\d{2,3})(cm|in)$', p['hgt'])
    if not pat: return False
    if pat[2] == 'in' and not 59 <= int(pat[1]) <= 76: return False
    if pat[2] == 'cm' and not 150 <= int(pat[1]) <= 193: return False

    if not match('^#[a-z0-9]{6}$', p['hcl']): return False

    if p['ecl'] not in set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']): return False

    if not match('^\d{9}$', p['pid']): return False

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