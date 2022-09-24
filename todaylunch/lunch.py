total_list = []

while True:
  question = input("질문을 입력해주세요")
  if question == "q":
    break
  else:
    total_list.append({"질문" : question, "답" : ""})

set_lunch = set(lunch)
while True:
  print(set_lunch)
  item = input("음식을 삭제해주세요 : ")
  if (item == "q"):
    break
  else:
    set_lunch = set_lunch - set([item]) 

print(set_lunch, "중에서 선택합니다.") 
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
