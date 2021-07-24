# -*- coding: utf-8 -*-


def sum_of_list(list_data):
    result = 0
    for i in list_data:
        result += i
    return result


def merge_and_sort(list_data_a, list_data_b):
    result = list_data_a + list_data_b
    result.sort()
    return result


def delete_a_list_element(list_data, element_value):
    if element_value in list_data:
        list_data.remove(element_value)
        result = list_data
    else:
        result = 0
    return result


def comparison_list_size(list_data_a, list_data_b):
    len_a = len(list_data_a)
    len_b = len(list_data_b)
    if len_a >= len_b:
        result = list_data_a
    else:
        result = list_data_b
    return result


def odd_even_check(a, b):
    check = (a + b) % 2
    if check == 0:
        result = 'Even'
    else:
        result = 'Odd'
    return result


def discount_price(price):
    if price < 100000:
        result = price * 0.9
    else:
        result = price * 0.8
    return result


def find_smallest_value(list_data):
    list_data.sort()
    result = list_data[0]
    return result


def binary_converter(decimal_number):
    result = ''
    while decimal_number > 0:
        remainder = decimal_number % 2
        decimal_number = decimal_number // 2
        result = str(remainder) + result
    return result.strip()


def number_of_cases(list_data):
    result = []
    for i in range(len(list_data)):
        for j in range(len(list_data)):
            a = str(list_data[i])
            b = str(list_data[j])
            compose = a + b
            if compose not in result:
                result.append(compose)
    result.sort()
    return result


def main():
    a = sum_of_list([1, 2, 3, 4])
    print(a)

    b = merge_and_sort([2, 1, 3, 0], [8, 6, 9, 5])
    print(b)

    c = delete_a_list_element(list_data=[1, 2, 3, 4], element_value=1)
    print(c)

    d = comparison_list_size(list_data_a=[1, 2, 3], list_data_b=[1, 2, 3, 4])
    print(d)

    e = discount_price(100000)
    print(e)

    f = find_smallest_value(list_data=[8, 6, 9, 5])
    print(f)

    print(binary_converter(10))
    print(number_of_cases(list_data=[1, 2, 3, 'a']))


if __name__ == "__main__":
    main()
