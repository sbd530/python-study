# -*- coding: utf8 -*-


# Help Function - 수정하지 말 것
def get_morse_code_dict():
    morse_code = {
        "A": ".-", "N": "-.", "B": "-...", "O": "---", "C": "-.-.", "P": ".--.", "D": "-..", "Q": "--.-", "E": ".",
        "R": ".-.", "F": "..-.", "S": "...", "G": "--.", "T": "-", "H": "....", "U": "..-", "I": "..", "V": "...-",
        "K": "-.-", "X": "-..-", "J": ".---", "W": ".--", "L": ".-..", "Y": "-.--", "M": "--", "Z": "--.."
    }
    return morse_code


# Help Function - 수정하지 말 것
def get_help_message():
    message = "HELP - International Morse Code List\n"
    morse_code = get_morse_code_dict()

    counter = 0

    for key in sorted(morse_code):
        counter += 1
        message += "%s: %s\t" % (key, morse_code[key])
        if counter % 5 == 0:
            message += "\n"

    return message


def is_help_command(user_input):
    # Input:
    #     - user_input : 문자열값으로 사용자가 입력하는 문자
    # Output:
    #     - 입력한 값이 대소문자 구분없이 "H" 또는 "HELP"일 경우 True,
    #       그렇지 않을 경우 False를 반환함
    lower = user_input.lower()
    return True if lower == "h" or lower == "help" else False


def is_validated_english_sentence(user_input):
    # Input:
    #     - user_input : 문자열값으로 사용자가 입력하는 문자
    # Output:
    #     - 입력한 값이 아래에 해당될 경우 False, 그렇지 않으면 True
    #       1) 숫자가 포함되어 있거나,
    #       2) _@#$%^&*()-+=[]{}"';:\|`~ 와 같은 특수문자가 포함되어 있거나
    #       3) 영어와 문장부호(.,!?)를 제외하면 입력값이 없거나 빈칸만 입력했을 경우
    characters = ".,!?"
    forbidden = """_@#$%^&*()-+=[]{}"';:|`~\\"""
    numbers = [str(i) for i in range(10)]

    string = "".join(x for x in user_input if x not in characters)
    string = string.strip()

    if len(string) == 0:
        return False

    for s in string:
        if (s in forbidden) or (s in numbers):
            return False

    return True


def is_validated_morse_code(user_input):
    # Input:
    #     - user_input : 문자열값으로 사용자가 입력하는 문자
    # Output:
    #     - 입력한 값이 아래에 해당될 경우 False, 그렇지 않으면 True
    #       1) "-","."," "외 다른 글자가 포함되어 있는 경우
    #       2) get_morse_code_dict 함수에 정의된 Morse Code 부호외 다른 코드가 입력된 경우 ex)......

    allowed_list = [".", "-", " "]

    for c in user_input:
        if c not in allowed_list:
            return False

    morse_code = get_morse_code_dict()
    morse_list = user_input.split()

    for morse in morse_list:
        if morse not in morse_code.values():
            return False

    return True


def get_cleaned_english_sentence(raw_english_sentence):
    # Input:
    #     - raw_english_sentence : 문자열값으로 Morse Code로 변환 가능한 영어 문장
    # Output:
    #     - 입력된 영어문장에수 4개의 문장부호를 ".,!?" 삭제하고, 양쪽끝 여백을 제거한 문자열 값 반환
    # Examples:
    #     >>> import morsecode as mc
    #     >>> mc.get_cleaned_english_sentence("This is Gachon!!")
    #     'This is Gachon'
    #     >>> mc.get_cleaned_english_sentence("Is this Gachon?")
    #     'Is this Gachon'
    #     >>> mc.get_cleaned_english_sentence("How are you?")
    #     'How are you'
    #     >>> mc.get_cleaned_english_sentence("Fine, Thank you. and you?")
    #     'Fine Thank you and you'
    characters = ".,!?"

    result = "".join(x for x in raw_english_sentence if x not in characters)
    result = result.strip()

    return result
    # ==================================


def decoding_character(morse_character):
    # """
    # Input:
    #     - morse_character : 문자열값으로 get_morse_code_dict 함수로 알파벳으로 치환이 가능한 값의 입력이 보장됨
    # Output:
    #     - Morse Code 를 알파벳으로 치환함 값
    morse_code = get_morse_code_dict()
    for k, v in morse_code.items():
        if morse_character == v:
            return k

    return None


def encoding_character(english_character):
    # Input:
    #     - english_character : 문자열값으로 알파벳 한 글자의 입력이 보장됨
    # Output:
    #     - get_morse_code_dict 함수의 반환 값으로 인해 변환된 모스부호 문자열값
    morse_code = get_morse_code_dict()
    for k, v in morse_code.items():
        if english_character == k:
            return v

    return None


def decoding_sentence(morse_sentence):
    # Input:
    #     - morse_sentence : 문자열 값으로 모스 부호를 표현하는 문자열
    # Output:
    #     - 모스부호를 알파벳으로 변환한 문자열
    result = ""
    morse_words = morse_sentence.split("  ")

    for morse_word in morse_words:
        morse_chars = morse_word.split()
        string = "".join(decoding_character(s) for s in morse_chars)
        result = result + string + " "

    return result.strip()


def encoding_sentence(english_sentence):
    # Input:
    #     - english_sentence : 문자열 값으로 모스 부호로 변환이 가능한 영어문장
    # Output:
    #     - 입력된 영어문장 문자열 값을 모스부호로 변환된 알파벳으로 변환한 문자열
    #       단 양쪽 끝에 빈칸은 삭제한다.
    result = ""
    sentence = get_cleaned_english_sentence(english_sentence.upper())
    words = sentence.split()
    for word in words:
        morse_word = " ".join(encoding_character(c) for c in word)
        result = result + morse_word + "  "

    return result.strip()


def main():
    print("Morse Code Program!!")
    # ===Modify codes below=============
    print(decoding_sentence("..  .-.. --- ...- .  -.-- --- ..-"))
    print(encoding_sentence("Hello! This is CS fifty Class."))
    # ==================================
    print("Good Bye")
    print("Morse Code Program Finished!!")


if __name__ == "__main__":
    main()
