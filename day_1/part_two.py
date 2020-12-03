import sys

def part_two(nums):
    snums = set(nums)
    for i in range(len(nums)):
        val = 2020 - nums[i]
        for j in range(i + 1, len(nums)):
            target = val - nums[j]
            if target in snums:
                return (nums[i], nums[j], target)
    
    # assuming this won't get hit
    raise Exception()

def main():
    with open(sys.argv[1]) as f:
        data = sorted(map(int, f.read().splitlines()))
        
    x, y, z = part_two(data)
    print("{} * {} * {} = {}".format(x, y, z, x * y * z))

if __name__ == '__main__':
    main()
