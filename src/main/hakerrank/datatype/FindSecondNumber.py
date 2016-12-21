# 1. N값을 받아 숫자를 몇개 받을지
# 1-2. N값의 숫자만큼의 수의 숫자를 A List 에 입력
# 1-3. A List 에는 각 숫자사이가 한칸씩 덜어져서 들어가야한다.
# 3. A List 값에서 2번째로 큰 값을 찾는다
# 4. 2번째로 큰 값을 출력한다.

def get_number_by_size(size, numbers):
    return numbers[:size]


def get_second_number(numbers):
    # max = None
    # second_max = None
    # if numbers[0] > numbers[1]:
    #     max = numbers[0]
    #     second_max = numbers[1]
    # elif numbers[0] == numbers[1]:
    #     max = numbers[0]
    # elif numbers[0] < numbers[1]:
    #     max = numbers[1]

    max = numbers[0] if numbers[0] >= numbers[1] else numbers[1]
    second_max = numbers[1] if numbers[0] > numbers[1] else None

    for number in numbers:
        if number > max:
            second_max = max
            max = number
        elif (second_max == None) and (number < max):
            second_max = number
        elif (second_max != None) and (second_max < number < max):
            second_max = number

    return second_max

def string_convert_list(str):
    return [int(c) for c in str.split()]


