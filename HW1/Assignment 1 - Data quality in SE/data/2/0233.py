# I have created this file - Akanshu
from django.http import HttpResponse
from django.shortcuts import render
from .methods import *


def index(request):
    return render(request, 'index.html')

def analyse(request):
    #getting the text
    djtext = request.POST.get("text", "default")

    #applied operation
    djpunc = request.POST.get("removepunc", "off")
    djcaps = request.POST.get("fullcaps", "off")
    newlineremover = request.POST.get("newlineremover", "off")
    extraspaceremover = request.POST.get("extraspaceremover", "off")
    capfirst = request.POST.get("capfirst", "off")

    if djpunc == "on":
        analysed = removepunc(djtext)

        params = {'purpose': 'Remove punctuations', 'analysed_text': analysed }
        djtext = analysed

    if capfirst == "on":
        analysed = capitalisefirst(djtext)

        params = {'purpose': 'Capitalised the first letter.', 'analysed_text': analysed}

    if djcaps == "on":
        analysed = toUpper(djtext)

        params = {'purpose': 'All capitalised', 'analysed_text': analysed}
        djtext = analysed

    if newlineremover == "on":
        analysed = newlineremove(djtext)

        params = {'purpose': 'New lines removed', 'analysed_text': analysed}
        djtext = analysed

    if extraspaceremover == "on":
        analysed = extraspaceremove(djtext)

        params = {'purpose': 'Space removed', 'analysed_text': analysed}

    if capfirst != "on" and extraspaceremover != "on" and newlineremover != "on" and djcaps != "on" and djpunc != "on":
        return HttpResponse("Please select any operation and try again..!!")

    return render(request, "analyse.html", params)