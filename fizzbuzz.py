def fb(x):
    result = ""
    if x % 3 == 0:
        result += "Fizz"
    if x % 5 == 0:
        result += "Buzz"
    if result != "":
        return result
    return str(x)


def fblist(nums):
    result = ""
    for num in nums:
        result += fb(num) + ","

    index = len(result)-1
    result = result[:index]

    return result
