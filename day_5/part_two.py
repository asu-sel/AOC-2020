import sys

def getID(bpass):
    row = bpass[:-3].replace('B', '1').replace('F', '0')
    col = bpass[-3:].replace('R', '1').replace('L', '0')

    return (int(row, 2) * 8) + int(col, 2)

def find(ids):
    return [mid for mid in range(ids[0], ids[-1]) if mid not in ids][0]

def main():
    with open(sys.argv[1]) as f:
        ps = f.read().splitlines()

    print('Missing ID is {}'.format(find(sorted(getID(p) for p in ps))))

if __name__ == '__main__':
    main()