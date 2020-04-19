from django.shortcuts import render
import re
# Create your views here.

global what

def index(request):
    print(request.GET.get('text','default'))
    return render(request,'filter_text/index.html')
    
def removepunch(request):
    raw_text = request.POST.get('text','default')
    removepunch = request.POST.get('removepunch','off')
    capitalize = request.POST.get('capitalize','off')
    newlineremove = request.POST.get('newlineremove','off')
    extraspaceremover = request.POST.get('spaceremover','off')
    wordcount = request.POST.get('wordcount','off')
    findemail = request.POST.get('findemail','off')

    
    if removepunch=='on' :
        punch = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        freshstr=''
        for char in raw_text:
            if char not in punch:
                freshstr = freshstr+char
        raw_text = freshstr 
        what = 'Removepunch '
        params={'what':what,'analyzedText': freshstr}
        
    if capitalize=='on':
        cap = ""
        for c in raw_text:
            cap = cap+c.capitalize()
        what = what + 'capitalize '
        params={'what':what,'analyzedText':cap}
        raw_text = cap
        
    if newlineremove=='on':
        newlinerm = ""
        for c in raw_text:
            if c !='\n' and c !='\r':
                newlinerm = newlinerm+c
        what = what + 'newlineremove '
        params={'what':what,'analyzedText':newlinerm}
        raw_text = newlinerm

    if extraspaceremover=='on':
        spacerm =  raw_text.strip()
        what = what + 'extraspaceremover'
        params={'what':what,'analyzedText':spacerm}
        raw_text = spacerm

    if findemail=='on':
        match = re.findall(r'[\w\.-]+@[\w\.-]+', raw_text)
        what = what + 'findemail'
        params={'what':'findemail','analyzedText':match}


#checkin if every Switch
    if removepunch!='on' and capitalize!='on' and newlineremove!='on' and extraspaceremover!='on' and findemail!='on':
        return HttpResponse("Error")
    else:
        return render(request,'filter_text/analyze.html',params)

