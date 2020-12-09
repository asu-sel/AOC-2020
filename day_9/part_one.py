import sys

def find(data):
    for i in range(25, len(data)):
        nums = set(data[i-25:i])
        found = False
        for num in nums:
            target = data[i] - num
            if target in nums:
                found = True
                break
        if not found:
            return data[i]
    return -1

def main():
    with open(sys.argv[1]) as f:
        data = list(map(int, f.read().splitlines()))
    
    print(f'First invalid number is {find(data)}')

if __name__ == '__main__':
    main()