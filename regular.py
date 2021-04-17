import re


text = """expressions Regular
use the backslash
how kaveh, how
he
Hey boy You are hey man
Heyloo


character""" 
# text = "He was carefully disguised but captured quickly by police."
p = re.compile(r"a",re.I | re.MULTILINE)
result = p.search(text)
print(result)


# result_iter = p.finditer(text)

# # print(result.group())

# for i in result_iter:
#     print(i.group())


# print(re.match("\w+s",text))
# 
# print(re.findall("\w+ly",text))