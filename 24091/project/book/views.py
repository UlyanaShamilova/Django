from django.shortcuts import render

# Create your views hed
def main(request):
    return render(request,'book/main.html')
def book(request):
    return render(request,'book/book.html')