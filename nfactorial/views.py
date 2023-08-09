from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def greet(request):
    return HttpResponse("Hello, nfactorial school")

def add(request, first: int, second: int):
    return HttpResponse(first + second)

def upper(request, text: str):
    return HttpResponse(text.upper())

def polindrome(request, word: str):
    return HttpResponse(word.lower() == word[::-1].lower())

def calculator(request, operation: str, first: int, second: int):
    if operation == "add":
        return HttpResponse(first + second)
    elif operation == "sub":
        return HttpResponse(first - second)
    elif operation == "mult":
        return HttpResponse(first * second)
    elif operation == "div":
        return HttpResponse(first // second)
    else:
        return HttpResponse("bad operation")