import pytest
from hakerrank.datatype.FindSecondNumber import *

#1. 입력 받은 값 2개를 처리하고 검증
def test_input():
    assert get_number_by_size(5, [22, 33, 44, 55, 11]) == [2, 3, 4, 5, 1]
    assert get_number_by_size(3, [2, 3, 4, 5, 1]) == [2, 3, 4]

#2. 두번째로 작은 수 찾기
def test_get_second_number():
    assert get_second_number([2, 3, 4, 5, 1]) == 4
    assert get_second_number([3, 3, 3, 3, 3]) == None
    assert get_second_number([3, 3, 4, 4, 1]) == 3
    assert get_second_number([2, 3, 4, 0, -1]) == 3
    assert get_second_number([57, 57, -57, 57]) == 57


#3. 결과값을 화면에 출력
def test_string_convert_list():
    assert string_convert_list("2 4 5 1 3") == [2, 4, 5, 1, 3]
