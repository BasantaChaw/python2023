from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    dic = {
        'title': 'Home', 'Name': 'WelCome To Basanta Chaudhary !',
        'numbers': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'emplist':[1],
        'language': ['Python', 'C', 'C+', 'Go', 'Java', 'PHP'],
        'student': [{'name': 'basanta', 'phone': 9808046983},{'name': 'rituraj', 'phone': 9843179885}],
        
    }
    return render(request, 'page.html', dic)


def about(request):
    return HttpResponse("Welcome to dream !")


def courseall(request):
    return HttpResponse("Welcome to dream !")


def course(request, courseid):
    return HttpResponse(courseid)
