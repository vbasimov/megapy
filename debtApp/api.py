from django.http import JsonResponse, HttpResponse, QueryDict
from .models import Debt
from debtApp.serializers import DebtSerializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def allDebts(request):
    
    debts = DebtSerializer(
        Debt.objects.all().order_by('secondName')\
        .filter(name__contains = request.GET.get('name'))\
        .filter(secondName__contains = request.GET.get('secondName')),
        many = True,
        context={'request':request}
    ).data

    return JsonResponse(debts, safe=False)

@csrf_exempt
def debtCreate(request):
    
    debt = Debt.objects.create(
        name = request.POST.get("name"),
        secondName = request.POST.get("secondName"),
        debtValue = request.POST.get("debtValue"),
    )

    return JsonResponse(model_to_dict(debt))

@csrf_exempt
def debtUpdate(request, debt_id):
    
    debt = Debt.objects.get(pk = debt_id)
    put = QueryDict(request.body)
    debt.name = put.get('name')
    debt.secondName = put.get('secondName')
    debt.debtValue = put.get('debtValue')
    debt.save()

    return HttpResponse(status = 200)

@csrf_exempt
def debtDelete(request, debt_id):
   
    debt = Debt.objects.get(pk = debt_id)
    debt.delete()
    
    return HttpResponse(status = 200)