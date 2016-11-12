import regex
briefinformal = """
유림이에게
안녕 유림아 나 서윤이야. 요즘 어떻게 지내니? 난 그럭저럭 지내. 지금 워크샵에 왔는데 조금 삶에 회의감이 느껴지네. 근데 괜찮아. 너가 내 옆에 있으니까 말야. 그래서 말인데  우리 오늘 밤엔 진짜 열심히 놀자.
이따봐. 감기 조심하고!
서윤이가
"""
scan = regex.findall(r'\p{IsHangul}+', briefinformal)
scan
