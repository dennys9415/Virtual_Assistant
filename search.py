import re
# result = re.search(r'Tutorials', 'TP Tutorials Point TP')
# print (result.group(0))


pattern = '[a-z]+'
string = '-----2344-Hello--World!'
result = re.search(pattern, string)
print(result.group())