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
    return user_input.upper() in ['H', 'HELP']

def is_validated_english_sentence(user_input):
    for i in user_input:
        if i.isdigit():
            return False
    for i in user_input:
        if i in ['_', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '[', ']',
                 '{', '}', '"', ';', ':', '|', '`', '~']:
            return False
    temp = []
    for i in user_input.split():
        if i == '.' or i == ',' or i == '!' or i == '?':
            continue
        temp.append(i)
    if not temp:
        return False
    return True

def is_validated_morse_code(user_input):
    for i in user_input.split():
        for j in i:
            if j != '-' and j != '.':
                return False
    temp = user_input.split()
    arr = list(get_morse_code_dict().values())
    for i in temp:
        if i not in arr:
            return False
    return True

def get_cleaned_english_sentence(raw_english_sentence):
    temp = []
    for i in raw_english_sentence:
        if i == '.' or i == ',' or i == '!' or i == '?':
            continue
        temp.append(i)
    return ''.join(temp).lstrip().rstrip()

def decoding_character(morse_character):
    morse_code_dict = get_morse_code_dict()
    temp = dict()
    for i in morse_code_dict:
        temp[morse_code_dict[i]] = i
    return temp[morse_character]

def encoding_character(english_character):
    morse_code_dict = get_morse_code_dict()
    return morse_code_dict[english_character]

def decoding_sentence(morse_sentence):
    temp = morse_sentence.split('  ')
    morse_code_dict = get_morse_code_dict()
    rev = dict()
    for i in morse_code_dict:
        rev[morse_code_dict[i]] = i
    ans = []
    for i in temp:
        each = i.split()
        res = ''
        for j in each:
            res += rev[j]
        ans.append(res)
    return ' '.join(ans)

def encoding_sentence(english_sentence):
    morse_code_dict = get_morse_code_dict()
    english_sentence = english_sentence.lstrip().rstrip().upper()
    temp = []
    for i in english_sentence:
        if i != '.' and i != ',' and i != '?' and i != '!':
            temp.append(i)
    english_sentence = ''.join(temp)
    ans = []
    for i in english_sentence.split():
        res = []
        for j in i:
            res.append(morse_code_dict[j])
        ans.append(' '.join(res))
    return '  '.join(ans)


def main():
    print("Morse Code Program!!")
    terminate = False
    while not terminate:
        a = input('Input your message(H - Help, 0 - Exit): ')
        if is_help_command(a):
            print(get_help_message())
        elif a == '0':
            terminate = True
            continue
        else:
            if is_validated_english_sentence(a):
                a = get_cleaned_english_sentence(a)
                print(encoding_sentence(a))
            elif is_validated_morse_code(a):
                print(decoding_sentence(a))
            else:
                print('Wrong Input')
    print("Good Bye")
    print("Morse Code Program Finished!!")

if __name__ == "__main__":
    main()
