import sys

def getID(bpass):
    row = bpass[:-3].replace('B', '1').replace('F', '0')
    col = bpass[-3:].replace('R', '1').replace('L', '0')

    return (int(row, 2) * 8) + int(col, 2)

def main():
    with open(sys.argv[1]) as f:
        passes = f.read().splitlines()

    print('Highest ID is {}'.format(max(getID(bpass) for bpass in passes)))

if __name__ == '__main__':
    main()