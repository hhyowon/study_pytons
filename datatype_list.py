# slicing 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
   

len(thislist)
# 7

thislist[1:3]
# ['banana', 'cherry']

thislist[:-1]
# ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon']   

# change value in list 
thislist[1] = 'Watermelon' 
thislist[1:3] = ['cherry','Watermelon']

#sort
thislist.sort()
thislist.sort(reverse=True)

# 붙여넣기
thislist = ["apple", "banana", "cherry"]
thislist.append('melon')
thislist.append('orange')
thislist.pop()
# 'orange'

# 초기화 방식
thislist = []
thislist = list()

#List thislist = new List();

pass

