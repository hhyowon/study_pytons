# user input 받아 갯수 만큼  fruits list 만큼 출력 반복하는 python code 작성
# - fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# - 출력은 index와 fruit name
# - Q 입력 시 while문 종료

# 과일 리스트
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

#무한루프
while True:
   number = input("Loops count: ") # 입력받기

   if number == "Q" : # Q입력시 while문 종료
       break
   elif number >= "1"  : 
    fruit_print_format = "{}: {}" #출력형태 1 : "apple"
    count = int(number) # int형으로 바꿔줌 
    if count > len(fruits) : #리스트 길이보다 큰 수 입력 시 
       print("숫자를 다시 입력하세요")
    else :
        for index, fruit in enumerate(fruits[:count], 1):  #과일 리스트 처음부터 ~ count 까지만 가져오기, index시작값은 1  
         print(fruit_print_format.format(index, fruit))

