# -*- coding: utf-8 -*-
def is_positive_number(integer_str_value):
    try:
        number = int(integer_str_value)
        if number <= 0:
            return False
        else:
            return True
    except ValueError:
        return False


def get_factorial_value(integer_value):
    if integer_value == 1:
        return 1
    else:
        return integer_value * get_factorial_value(integer_value - 1)


def main():
    while True:
        print("Input a positive number : ", end='')

        num = input()

        if num == '0':
            break

        if is_positive_number(num):
            new_num = int(num)
            print(get_factorial_value(new_num))
        else:
            print("Input again, Please")

    print("Thank you for using this program")


if __name__ == "__main__":
    main()
