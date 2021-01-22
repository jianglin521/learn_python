import re

test = "let a = 'http://www.baidu.com'"

aa = re.findall('let a = \S*\.com', test)
print(aa, '000000')