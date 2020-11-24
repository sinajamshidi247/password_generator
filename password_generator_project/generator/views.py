from django.shortcuts import render
import random




def home(request):
  
 
    return render(request,'generator/home.html')


def password(request):

   
    charecters = list('qwertyuiopasdfghjklzxcvbnm')
    length=int(request.GET.get('length',8))  
    if request.GET.get('uppercase'):
        charecters.extend('QWERTYUIOPASDFGH')
    if request.GET.get('speacial'):
        charecters.extend('!@#$%^&*+')
    if request.GET.get('Numbers'):
        charecters.extend('0123456789')
    password = ''
    for x in range(length):
        password += random.choice(charecters)




    return render(request,'generator/password.html',{'password':password})



def about(request):


    return render(request,'generator/about.html')