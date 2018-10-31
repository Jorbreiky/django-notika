from django.shortcuts import render, redirect
#from Plantilla.app.modelos.user import UserDAO

class User():
    
    def index(self, request):
        #users = UserDAO.objects.all().order_by('nombre')
        context = {'users': 'usuario'}
        return render(request, 'user_all.html', context)

    def add(self, request):
        return render(request, 'user_add.html')
    
    def insert(self, request):
        request.clean_fields()
        return redirect('/')
        