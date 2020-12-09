import sys

def find_invalid(data):
    for i in range(25, len(data)):
        nums = data[i-25:i]
        found = False
        for num in nums:
            target = data[i] - num
            if target in nums:
                found = True
                break
        if not found:
            return data[i]
    return -1

def find_sum(data):
    invalid = find_invalid(data)
    for i in range(len(data)):
        for j in range(0, i + 1):
            if sum(data[j:i]) == invalid:
                s = sorted(data[j:i])
                return s[0] + s[-1]
    return -1

def main():
    with open(sys.argv[1]) as f:
        data = list(map(int, f.read().splitlines()))
    
    print(f'Sum is {find_sum(data)}')

if __name__ == '__main__':
    main()