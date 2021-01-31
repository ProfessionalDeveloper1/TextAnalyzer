from django.http import HttpResponse
from django.shortcuts import render

# Index Function
def index(request):
    '''This function take request and return render(request,'index.htm')'''
    return render(request,'index.html')

# Analyze Function
def analyze(request):
    '''This function tekes request as an required argument and perform operations when the checkbox is on'''
    djtext=request.POST.get('text','default')
    Removepunc=request.POST.get('removepunctuations','off')
    Newline=request.POST.get('newlineremover','off')
    Extraspace=request.POST.get('removeextraspaces','off')
    Upper=request.POST.get('uppercase','off')

    if Removepunc=="on":
        analyzed=""
        punctuations='''!@#$%^&*()_}{][;"'<>,.?/|'''
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Remove Punctuations','Analyzed_text':analyzed} 
        djtext=analyzed

    if Upper=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Change To Upper Case','Analyzed_text':analyzed} 
        djtext=analyzed
    
    if Newline=="on":
        analyzed=""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed=analyzed+char

        params={'purpose':'Remove New Line','Analyzed_text':analyzed} 
        djtext=analyzed
    
    if Extraspace=="on":
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char
        params={'purpose':'Remove Extra Spaces','Analyzed_text':analyzed} 
        djtext=analyzed

    if(Removepunc != "on" and Newline!="on" and Extraspace!="on" and Upper!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request,'analyze.html',params)