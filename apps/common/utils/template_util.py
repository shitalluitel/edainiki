import re

from apps.common.constants import template_map as field_reference


def generate_letter(instance, letter_template):
    pattern = re.compile(r'\r\n\r\n|\r\n(\t)*')
    letter_template = pattern.sub(' ', letter_template)
    if instance:
        template_map = getattr(field_reference, instance.__class__.__name__.upper())
        for field_name in template_map.get('non_related_fields'):
            letter_template = replace_template(instance, field_name, letter_template)

        related_fields = template_map.get('related_fields')
        for key, value in related_fields.items():
            letter_template = parse_multiple_data(
                template=letter_template,
                fields=value,
                queryset=getattr(instance, key).all()
            )
        return letter_template
    return "Not able to generate template."


def replace_template(instance, field_name, letter_template):
    pattern = re.compile(r'{{ _ }}'.replace('_', field_name))
    letter_template = pattern.sub(str(getattr(instance, field_name)), letter_template)
    return letter_template


def parse_multiple_data(template, fields=None, queryset=None):
    pattern_str = '<tr><td colspan="\d+">{{ multiple }}</td></tr>(.*)<tr><td colspan="\d+">{{ end_multiple }}</td>' \
                  '</tr>|<p>{{ multiple }}</p>(.*)<p>{{ end_multiple }}</p>|{{ multiple }}(.*){{ end_multiple }}'
    pattern = re.compile(pattern_str)
    result = add_multiple_data(
        template=pattern.search(template).group(1),
        fields=fields,
        queryset=queryset
    )
    return pattern.sub(result, template)


def add_multiple_data(template, fields, queryset):
    _data = []
    if queryset:
        for instance in queryset:
            _temp = template
            for field in fields:
                if hasattr(instance, field):
                        _temp = replace_template(
                            instance=instance,
                            field_name=field,
                            letter_template=_temp
                        )
            _data.append(_temp)
    return ''.join(_data)
