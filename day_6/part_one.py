import sys

def main():
    with open(sys.argv[1]) as f:
        answers = f.read().split('\n\n')

    res = sum(len(set.union(*[set(g) for g in a.splitlines()])) for a in answers)
    print('Count is {}'.format(res))

if __name__ == '__main__':
    main()