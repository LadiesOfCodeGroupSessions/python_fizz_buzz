from fizzbuzz import fb


def test_given_one_return_one():
    assert fb(1) == 1


def test_given_three_return_fizz():
    assert fb(3) == "Fizz"


def test_given_five_return_buzz():
    assert fb(5) == "Buzz"


def test_given_multiple_of_three_and_five_return_fizz_buzz():
    assert fb(15) == "FizzBuzz"

