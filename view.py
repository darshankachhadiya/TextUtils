#created by d
from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    return render(request,'index.html')
   # return HttpResponse("<h1>Home </h1>")


def analyze(request):
    #get the text
    djtext=request.GET.get('text','default')

    #check checkbox value
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspaceremover=request.GET.get('extraspaceremover','off')
    charcount=request.GET.get('charcount','off')


    #Chech which checkbox is on
    if removepunc == "on":
        punctuation='''!()-[]{}:;'"\,<>./?@#$%^&*_~`'''
        analyzed=""
        for char in djtext:
            if char not in punctuation:
                analyzed=analyzed+char
        d={'purpose':'Removed Punctuation','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',d)
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        d = {'purpose': 'changed to Upercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # analyze the text
        #return render(request, 'analyze.html', d)
    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n":
                analyzed = analyzed + char
        d = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext=analyzed

        # analyze the text
        #return render(request, 'analyze.html', d)
    if (extraspaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        d = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed
        # analyze the text
        #return render(request, 'analyze.html', d)
    elif(charcount=="on"):
        analyzed = ""
        count = 0
        for char in djtext:
            count += 1
        analyzed = count
        d = {'purpose': 'Total Character', 'analyzed_text': analyzed}

    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on"):
        return HttpResponse("Please Select the option")

    return render(request, 'analyze.html', d)

