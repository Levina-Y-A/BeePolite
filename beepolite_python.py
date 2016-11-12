import regex
briefinformal = """
선생님아
안녕 쎔 나 서윤이야. 요즘 어떻게 지내니? 난 그럭저럭 지내. 지금 워크샵에 왔는데 조금 삶에 회의감이 느껴지네. 근데 괜찮아. 네가 잘 도와줄거라 믿어. 그래서 말인데 이따가 나좀 도와줄래?
이따봐. 항상 감기 조심하고. 힘내고.
서윤이가
"""
scan = regex.findall(r'\p{IsHangul}+', briefinformal)
scan

unhoflich = [r'안녕', r'.*아\b',r'쌤',r'.*이야']

def scannen():
    #unhoflich = [r'안녕', r'*아/b',r'쌤',r'.*이야']
    #for i in range(len(scan)):
        #word = scan[i]
    for word in scan:
        for r in unhoflich:
            m = regex.match(r, word)
            if m:
                yield word
        #if scan[i] == unhoflich[0]:
            #return scan[i]+'ist unhöflich'
    
print(list(scannen()))
