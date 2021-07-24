# -*- coding: utf-8 -*-

def input_celsius_value():
    print("변환하고 싶은 섭씨 온도를 입력해 주세요: ")
    return float(input())


def convert_celsius_fahrenheit(celsius_value):
    return ((9 / 5) * celsius_value) + 32


def print_fahrenheit_value(c, f):
    print("섭씨온도 : " + str(c))
    print("화씨온도 : " + str(f))


def main():
    print("본 프로그램은 섭씨를 화씨로로 변환해주는 프로그램입니다")
    print("============================")
    # ===Modify codes below=================
    c = input_celsius_value()
    f = convert_celsius_fahrenheit(c)
    print_fahrenheit_value(c, f)
    # ======================================
    print("===========================")
    print("프로그램이 종료 되었습니다.")


if __name__ == '__main__':
    main()
