import sys
from re import match

fs = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
ecl = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])

def is_valid(p):
    if not all(x in p for x in fs): return False 

    if not 1920 <= p['byr']) <= 2002: return False

    if not 2010 <= p['iyr'] <= 2020: return False

    if not 2020 <= p['eyr'] <= 2030: return False

    if not (pat := match(r'^(\d{2,3})(cm|in)$', p['hgt'])): return False
    if pat[2] == 'in' and not 59 <= pat[1] <= 76: return False
    if pat[2] == 'cm' and not 150 <= pat[1] <= 193: return False

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