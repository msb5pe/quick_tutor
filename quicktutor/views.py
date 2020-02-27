from django.shortcuts import redirect

def redirect_root(request):
    return redirect('http://localhost:8000/login/')