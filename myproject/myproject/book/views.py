from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, "book/main.html") 

def maxim(request):
    return render(request, "book/maxim.html")


