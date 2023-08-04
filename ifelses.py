first = 3
second =4

# 기본 if-elif-else
# if(first < second){
# }else{
#   }
if(first < second) :
    print('less first')
else :
    print('greater second')

# break
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
for fruit in thislist:
    pass 
    if(fruit =='orange'):
        break 
    print(fruit)

# while
first = 3
while( first > 4) : 
    pass
    print('while count{}'.format(first))
    first = first + 1

# list with numbering : list 는 []  
fruit= ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# enumerate 원리 이해 
fruits_enumerate = enumerate(fruit)
pass

# next()
# Traceback (most recent call last):
#  File "<string>", line 1, in <module>
# TypeError: next expected at least 1 argument, got 0

# list with numbering : list 는 []  
fruits= ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
fruits_enumerate = enumerate(fruits)
for index_fruit in fruits_enumerate: #튜플 묶음
    print(index_fruit)
    pass

fruits_enumerate = enumerate(fruits)
fruit_print_format = "number: {}, fruit name: {}"
for index, fruit in enumerate(fruits):
    print(fruit_print_format.format(index, fruit))
    pass
pass