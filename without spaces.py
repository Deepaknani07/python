import re
text ='python Life'
print("orginal text",text)
print("without white spaces:",re.sub(r'\s+','',text))
