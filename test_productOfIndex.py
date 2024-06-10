from product_Of_Index import *

def test_even_function_return_even_list():
    nums = list(range(1, 11))
    assert even_number_list(nums) == [2, 4, 6, 8, 10]

