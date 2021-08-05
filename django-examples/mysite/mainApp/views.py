from django.shortcuts import render
def index(request):
    return render(request,'mainApp/homepage.html')
def contact(request):
    return render(request,'mainApp/basic.html',{'values':['Если у вас остались вопросы, то задавайте их мне по телефону',
                      '8707-149-85-35','www.nurtileu.kz@gmail.com']})

