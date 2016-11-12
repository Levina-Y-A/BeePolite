from bottle import route, run, static_file, request, redirect

@route('/')
def index():
    return static_file('index.html', root='/Users/Anna/documents/BeePolite')
    
@route('/<filename>')
def index(filename):
    return static_file(filename, root='/Users/Anna/documents/BeePolite')
    
@route('/styles/<filename>')
def style(filename): 
    return static_file(filename, root='/Users/Anna/documents/BeePolite/styles')

@route('/verarbeitet', method="POST")
def verarbeiten():
    output_text = "hallo"
    input_text = request.forms.get('eingabe')
    import regex
    scan = regex.findall(r'\p{IsHangul}+', input_text)
    unhoflich = [r'안녕', r'.*아\b',r'쌤',r'.*이야']

    result = ""
    for word in scan:
        for r in unhoflich:
            m = regex.match(r, word)
            if m:
                result = result + word

    return redirect("/index.html?inputText=" + input_text +"&outputText=" + result)
run(host='localhost', port=8080, debug=True)

#for i in range word:
#   print(word[i]+'unhöflich')