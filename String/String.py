letters = 'python'

print(letters[0], letters[2])

license_plate = "24가 2210"
#   슬라이싱
#   print(license_plate[startIndex : endIndex])
#   '-' 뒤에서 부터 인덱싱    
print(license_plate[ -4 : ])

string = "홀짝홀짝홀짝"
#   print(string[startIndex : endIndex : offset])
print(string[ : : 2 ])
print(string[ 1 : : 2 ])

string = "PYTHON"
#   offset에 '-'를 붙이면 문자열 마지막에서 시작한다.
print(string[ : : -1])
print(string[ : : -2])

phone_nunber = "010-1111-2222"
temp = phone_nunber.replace("-", "/")

print(temp)

temp = phone_nunber.replace("-", "")

print(temp)

url = "http://sharebook.kr"
temp = url.split(".")
print(temp[-1])

lang = "python"
lang[0] = 'p'
print(lang) 