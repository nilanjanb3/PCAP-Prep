nums = [_ for _ in range(10)]

print(nums)

squareList = [_**2 for _ in range(10)]

print(squareList)

oddList = [_ for _ in range(10) if _ % 2 == 1]

print(oddList)

oddList = list(filter(lambda x: x % 2 == 1, nums))

print(oddList)

cubeList = list(map(lambda x : x**3, nums))

print(cubeList)