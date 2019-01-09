import django_excel as excel

data = [
    ('Имя', 'Фамилия', 'Задолженность'),
    ('Алексей', 'Алексеев', 1000),
    ('Иван', 'Иванов', 520)
]

def downloadAsAttachment(request, file_type, file_name):
    return excel.make_response_from_array(
        data, file_type, file_name=file_name)

