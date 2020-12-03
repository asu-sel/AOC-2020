def traverse(data):
    w, h = len(data[0]), len(data)
    x, y = 0, 0
    count = 0
    while y < h - 1:
        x = (x + 3) % w
        y += 1
        if data[y][x] == '#': count += 1
    return count

def main():
    with open('003.in') as f:
        data = f.read().splitlines()
    print('You would encounter {} trees'.format(traverse(data)))

if __name__ == '__main__':
    main()