SETTING = {'non_related_fields': [], 'related_fields': {}}
STUDENT = {
    'non_related_fields': ['subjects', 'name', 'age', 'address'],
    'related_fields': {'student subjects': ['subject']}
}
STUDENT_SUBJECTS = {'non_related_fields': ['subject'], 'related_fields': {}}
STUDENT_LETTER = {'non_related_fields': ['template'], 'related_fields': {}}


STUDENT = {
    'name': 'name',
    'age': 'age',
    'address': 'address',
    'subject_name': 'subjects.name'
}