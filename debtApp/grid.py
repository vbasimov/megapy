from .models import Debt
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from collections import OrderedDict

@login_required(login_url = 'login')
def debtGrid(request):
    
    message = {}
    if request.method == "POST":

        filehandle = request.FILES['file']
        
        message = checkFileExtention(filehandle)   
        if message != {}:
            return render(request, 'debtApp/debt-grid.html', {'message': message})
        
        debts = filehandle.get_records()
        successAdded = len(debts)

        for debt in debts:
            preparedDebt = _debtIndexLowerCase(debt)
            message = _checkHeadersOfEntries(request, preparedDebt)
            if message != {}:
                return render(request, 'debtApp/debt-grid.html', {'message': message})
            successAdded = _createNewDebtInstances(preparedDebt, successAdded)

        message = _addingDebtsMessage(request, successAdded, len(debts))
        return render(request, 'debtApp/debt-grid.html', {'message': message})

    return render(request, 'debtApp/debt-grid.html')

def checkFileExtention(filehandle):

    message = {}

    if not (filehandle.name.endswith('.xls') or filehandle.name.endswith('.xlsx')):
            message['text'] = 'Ошибка! Вы выбрали файл с неверным расширением. Выберите файл с расширением \".xls\" или \".xlsx\"'
            message['status'] = 'bad'

    return message

def _debtIndexLowerCase(debt):

    newDebtFormat = OrderedDict()
    for key, value in debt.items(): 
        newDebtFormat[key.lower()] = value

    return newDebtFormat

def _checkHeadersOfEntries(request, debt):

    message = {}

    if not ('имя' in debt and 'фамилия' in debt and 'задолженность' in debt):
        message['text'] = 'Ошибка чтения файла. Невозможно прочитать заголовки записей. '\
        + ' Проверьте правильность заполнения согласно примера, доступного по ссылке ниже'
        message['status'] = 'bad'

    return message

def _createNewDebtInstances(debt, successCount):

    if (debt['имя'].strip() != ''
        and debt['фамилия'].strip() != ''
        and type(debt['задолженность']) == int):
        
        Debt.objects.create(
            name = debt['имя'],
            secondName = debt['фамилия'],
            debtValue = debt['задолженность'],
        )
    else:
        successCount -= 1

    return successCount

def _addingDebtsMessage(request, successCount, entriesFromXlsCount):

    message = {}

    if (successCount == entriesFromXlsCount):
        message['text'] = 'Вы успешно добавили ' + str(successCount)\
            + _pluralForm(successCount, ' запись', ' записи', ' записей')
        message['status'] = 'good'
    elif (successCount > 0):
            message['text'] = 'Были добавлены не все записи . '\
                + 'Вы успешно добавили ' + str(successCount)\
                + _pluralForm(successCount, ' запись', ' записи', ' записей') + ' из ' + str(entriesFromXlsCount)\
                + '. Проверьте правильность заполнения согласно примера, доступного по ссылке ниже'
            message['status'] = 'bad'
    else: 
        message['text'] = 'Ошибка чтения файла. Все записи имеют ошибочые данные. '\
        + ' Проверьте правильность заполнения согласно примера, доступного по ссылке ниже'
        message['status'] = 'bad'

    return message

def _pluralForm(n, form1, form2, form5):

    n = abs(n) % 100
    n1 = n % 10

    if (n > 10 and n < 20):
        return form5
    if (n1 > 1 and n1 < 5):
        return form2
    if (n1 == 1):
        return form1

    return form5
