# -*- coding: utf8 -*-

def get_file_contents(filename):
    # Input:
    #   - filename : 문자열값으로 처리할 파일의 이름
    # Output:
    #   - 파일에 나오는 모든 Text 데이터를 문자열로 반환
    with open(filename, "rt", encoding="UTF8") as file:
        contents = file.read()
        return contents


def get_number_of_characters_with_blank(filename):
    # Input:
    #   - filename : 문자열값으로 처리할 파일의 이름
    # Output:
    #   - 빈칸을 포함하여 해당 파일에 나오는 글자 수의 총합
    with open(filename, "rt", encoding="UTF8") as file:
        content = file.read()
        length = len(content)
        return length


def get_number_of_characters_without_blank(filename):
    # Input:
    #   - filename : 문자열값으로 처리할 파일의 이름
    # Output:
    #   - 빈칸을 포함하지 않는 해당 파일에 나오는 글자 수의 총합
    #     여기서 빈칸이라고 함은 " ", "\t", "\n" 을 모두 포함함
    with open(filename, "rt", encoding="UTF8") as file:
        content = file.read()
        count_space = content.count(" ")
        count_tab = content.count("\t")
        count_enter = content.count("\n")
        print(count_space)
        print(count_tab)
        print(count_enter)

        length = len(content) - count_space - count_tab - count_enter
        return length


def get_number_of_lines(filename):
    # Input:
    #   - filename : 문자열값으로 처리할 파일의 이름
    # Output:
    #   - 해당 파일의 모든 라인수의 총합
    #     단 마지막 줄 수는 제외함
    with open(filename, "rt", encoding="UTF8") as file:
        lines = file.readlines()
        length = len(lines)

        return length


def get_number_of_target_words(filename, target_words):
    # Input:
    #   - filename : 문자열값으로 처리할 파일의 이름
    #   - target_words : 문자열값으로 처리할 파일의 이름
    # Output:
    #   - 대소문자 구분없이 해당 파일에  target_words가 포함된 횟수
    with open(filename, "rt", encoding="UTF8") as file:
        content = file.read()
        content = content.lower()
        target_words = target_words.lower()
        count = content.count(target_words)

        return count


if __name__ == '__main__':
    print(get_number_of_target_words("1984.txt", "Hi"))
    print(get_number_of_target_words("1984.txt", "had"))
    print(get_number_of_target_words("1984.txt", "and"))
