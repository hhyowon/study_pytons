# user input 받아 갯수 만큼  fruits list 만큼 출력 반복하는 python code 작성
# - fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# - 출력은 index와 fruit name
# - Q 입력 시 while문 종료

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

while True:
   number = input("Loops count: ")

   if number == "Q" :
       break
   elif number >= "1"  :
    fruit_print_format = "{}: {}"
    count = int(number)
    for index, fruit in enumerate(fruits[:count], 1):
        print(fruit_print_format.format(index, fruit))

