import re


def generate_letter(instance, letter_template):
    maps = {
        'name': r'{{ name }}',
        'age': r'{{ age }}',
        'address': r'{{ address }}'
    }

    for key, value in maps.items():
        data = getattr(instance, key)
        pattern = re.compile(value)
        letter_template = pattern.sub(data, letter_template)

    print(letter_template)
    return letter_template
