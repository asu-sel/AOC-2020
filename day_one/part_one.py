def part_one(nums):
    for num in nums:
        target = 2020 - num
        if target in nums: 
            return (num, target)
    
    # assuming this won't get hit
    raise Exception()

def data():
    

def main():
    data = []
    with open('001_input.txt') as f:
        data = list(map(int, f.read().splitlines()))
        
    x, y = part_one(data)
    print("{} * {} = {}".format(x, y, x * y))

if __name__ == '__main__':
    main()