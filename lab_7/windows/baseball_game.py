# -*- coding: utf-8 -*-

import random


def get_random_number():
    # Helper Function - 지우지 말 것
    # 100부터 999까지 수를 램덤하게 반환함
    return random.randrange(100, 1000)


def is_digit(user_input_number):
    if user_input_number[0] == "0":
        return False

    for c in user_input_number:
        if not (ord("0") <= ord(c) <= ord("9")):
            return False

    return True


def is_between_100_and_999(user_input_number):
    # Input:
    #   - user_input_number : 문자열 값
    #                         입력된 값은 숫자형태의 문자열 값임이 보장된다.
    # Output:
    #   - user_input_number 가 정수로 변환하여 100이상 1000미만일 경우 True,
    #     그렇지 않을 경우는 False
    i = int(user_input_number)
    return True if 100 <= i <= 999 else False


def is_duplicated_number(three_digit):
    # Input:
    #   - three_digit : 문자열로 된 세자리 양의 정수 값
    #                   문자열로 된 세자리 양의 정수값의 입력이 보장된다.
    # Output:
    #   - three_digit 정수로 변환하였을 경우 중복되는 수가 있으면 True,
    #     그렇지 않을 경우는 False
    s = set(three_digit)
    return True if len(s) < 3 else False


def is_validated_number(user_input_number):
    # Input:
    #   - user_input_number : 문자열 값
    # Output:
    #   - user_input_number 값이 아래 조건이면 True, 그렇지 않으면 False 를 반환
    #        1) 숫자형 문자열이며, 2) 100이상 1000미만이며, 3) 중복되는 숫자가 없을 경우
    if not is_digit(user_input_number):
        return False
    if not is_between_100_and_999(user_input_number):
        return False
    if is_duplicated_number(user_input_number):
        return False

    return True


def get_not_duplicated_three_digit_number():
    # Input:
    #   - None : 입력값이 없음
    # Output:
    #   - 중복되는 숫자가 없는 3자리 정수값을 램덤하게 생성하여 반환함
    #     정수값으로 문자열이 아님
    while True:
        random_number = get_random_number()
        str_random_number = str(random_number)
        s = set(str_random_number)
        if len(s) == 3:
            return random_number


def get_strikes_or_ball(user_input_number, random_number):
    # Input:
    #   - user_input_number : 문자열값으로 사용자가 입력하는 세자리 정수
    #   - random_number : 문자열값으로 컴퓨터가 자동으로 생성된 숫자
    # Output:
    #   - [strikes, ball] : 규칙에 따라 정수형 값인 strikes 와 ball 이 반환됨
    #   변환 규칙은 아래와 같음
    #   - 사용자가 입력한 숫자와 컴퓨터가 생성한 숫자의
    #     한 숫자와 자릿수가 모두 일치하면 1 Strike
    #   - 자릿수는 다르나 입력한 한 숫자가 존재하면 1 Ball
    #   - 세자리 숫자를 정확히 입력하면 3 Strike
    strikes = 0
    balls = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if i == j and user_input_number[i] == random_number[j]:
                strikes += 1
            elif i != j and user_input_number[i] == random_number[j]:
                balls += 1

    return [strikes, balls]


def is_yes(one_more_input):
    # Input:
    #   - one_more_input : 문자열값으로 사용자가 입력하는 문자
    # Output:
    #   - 입력한 값이 대소문자 구분없이 "Y" 또는 "YES"일 경우 True,
    #     그렇지 않을 경우 False 를 반환함
    lower = one_more_input.lower()
    return True if lower == "y" or lower == "yes" else False


def is_no(one_more_input):
    # Input:
    #   - one_more_input : 문자열값으로 사용자가 입력하는 문자
    # Output:
    #   - 입력한 값이 대소문자 구분없이 "N" 또는 "NO"일 경우 True,
    #     그렇지 않을 경우 False 를 반환함
    lower = one_more_input.lower()
    return True if lower == "n" or lower == "no" else False


def main():
    print("Play Baseball")

    check = True

    while check:
        random_number = str(get_not_duplicated_three_digit_number())
        print("Random Number is : ", random_number)

        while True:
            user_input = input('Input guess number : ')
            if is_validated_number(user_input):
                result = get_strikes_or_ball(user_input, random_number)
                print("Strikes :", str(result[0]), ", Balls :", str(result[1]))
                if result[0] == 3:
                    break
            else:
                print("Wrong Input, Input again")

        while True:
            y_or_n = input('You win, one more(Y/N)?')
            if is_no(y_or_n):
                check = False
                break
            elif is_yes(y_or_n):
                break
            else:
                print("Wrong Input, Input again")

    print("Thank you for using this program")
    print("End of the Game")


if __name__ == "__main__":
    main()
