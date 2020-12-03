def traverse(data, dx, dy):
    w, h = len(data[0]), len(data)
    x, y = 0, 0
    count = 0
    while y < h - 1:
        x = (x + dx) % w
        y += dy
        if data[y][x] == '#': count += 1
    return count

def main():
    with open('003.in') as f:
        data = f.read().splitlines()
    
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    result = 1
    for slope in slopes:
        result *= traverse(data, slope[0], slope[1])
    print("Result is {}".format(result))

if __name__ == '__main__':
    main()