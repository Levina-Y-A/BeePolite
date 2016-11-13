# -*- coding: utf-8 -*-
from bottle import route, run, static_file, request, redirect
import regex, urllib

@route('/')
def index():
    return static_file('index.html', root='/Users/johl/Documents/BeePolite')

@route('/<filename>')
def index(filename):
    return static_file(filename, root='/Users/johl/Documents/BeePolite')

@route('/styles/<filename>')
def style(filename):
    return static_file(filename, root='/Users/johl/Documents/BeePolite/styles')

@route('/verarbeitet', method="POST")
def verarbeiten():
    output_text = "Alles Okay!"
    input_text = urllib.parse.unquote(request.forms.get('eingabe'), encoding='utf-8')
    print(input_text)
    scan = regex.findall(r'\p{IsHangul}+', input_text)
    unhoflich = [r'안녕', r'.*아\b',r'쌤',r'.*이야']
    for word in scan:
        for r in unhoflich:
            m = regex.match(r, word)
            if m:
                output_text = "Das geht auch höflicher!"

    #return redirect("/index.html?inputText=" + input_text +"&outputText=" + output_text)
    return redirect("/index.html?outputText=" + output_text)
run(host='localhost', port=8080, debug=True)

#for i in range word:
#   print(word[i]+'unhöflich')
