from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    wdicto = {}
    for word in wordlist:
        if word in wdicto:
            wdicto[word] += 1
        else:
            wdicto[word] = 1
    
    sw = sorted(wdicto.items(), key=operator.itemgetter(1), reverse=True)
        
    return render(request, 'count.html',{'fulltext':fulltext,'count':len(wordlist),'wd':sw})


def about(request):
    return render(request,'about.html')