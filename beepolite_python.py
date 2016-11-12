import re
hallo = "안녕하세"
m = re.match(r"(안녕)",hallo)
print(m.group(1))
