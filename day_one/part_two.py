def part_two(nums):
    for i in range(len(nums)):
        val = 2020 - nums[i]
        for j in range(i, len(nums)):
            target = val - nums[j]
            if target in nums:
                return (nums[j], nums[i], target)
    
    # assuming this won't get hit
    raise Exception()

def main():
    data = []
    with open('001_input.txt') as f:
        data = list(map(int, f.read().splitlines()))
        
    x, y, z = part_two(data)
    print("{} * {} * {} = {}".format(x, y, z, x * y * z))

if __name__ == '__main__':
    main()
