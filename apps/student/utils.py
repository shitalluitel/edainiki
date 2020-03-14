import re


def generate_letter(instance, letter_template):
    letter_template = letter_template.replace('\\r\\n\\r\\n', ' ')
    if instance:
        for field in instance._meta.fields:
            field_name = field.attname
            pattern = re.compile(r'{{ _ }}'.replace('_', field_name))
            letter_template = pattern.sub(str(getattr(instance, field_name)), letter_template)

        letter_template = parse_multiple_data(temp=letter_template)
        return letter_template
    return "Not able to generate template."


def parse_multiple_data(temp, queryset=None):
    pattern = re.compile(r'\r\n\r\n')
    temp = pattern.sub(' ', temp)
    pattern = re.compile(r'\r\n(\t)*')
    template = pattern.sub(' ', temp)

    # other possible patterns
    # pattern = re.compile('<p>{{ multiple }}</p>(.*)<p>{{ end_multiple }}</p>')
    # pattern = re.compile('{{ multiple }}(.*){{ end_multiple }}')

    pattern = re.compile('<tr><td colspan="\d+">{{ multiple }}</td></tr>(.*)<tr><td colspan="\d+">{{ end_multiple }}</td></tr>')

    result = pattern.search(template).group(1)

    return pattern.sub(result, template)


def add_multiple_data(template, queryset):
    pass