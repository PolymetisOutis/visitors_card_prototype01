from django.shortcuts import render

def list_company(request):
    return render(request, 'visitors_card_app/analysis/list_company.html')

def list_name(request):
    return render(request, 'visitors_card_app/analysis/list_name.html')

def list_interviewer(request):
    return render(request, 'visitors_card_app/analysis/list_interviewer.html')

def list_history(request):
    return render(request, 'visitors_card_app/analysis/list_history.html')
