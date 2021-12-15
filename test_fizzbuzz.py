from fizzbuzz import fb, fblist


def test_given_one_return_one():
    assert fb(1) == 1


def test_given_three_return_fizz():
    assert fb(3) == "Fizz"


def test_given_five_return_buzz():
    assert fb(5) == "Buzz"


def test_given_multiple_of_three_and_five_return_fizz_buzz():
    assert fb(15) == "FizzBuzz"

def test_1_to_30():
    nums  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    assert fblist(nums) == "1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz"
