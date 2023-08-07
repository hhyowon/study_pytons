#초기화 방법
thisdict = {}     #empty initial
thisdict = dict() #empty initial
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

len(thisdict)
# 3

type(thisdict)
# <class 'dict'>

thisdict['model']
# 'Mustang'

thisdict['brand'] = "hyowon"

thisdict.keys()
# dict_keys(['brand', 'model', 'year'])

type(thisdict.keys())
# <class 'dict_keys'>

thisdict.values()
# dict_values(['hyowon', 'Mustang', 1964])

dict_format ="key : {0} , value : {1} "
for key, value in thisdict.items():
    print(dict_format.format(key, value))
    pass 
pass

# add item in dict
thisdict['color'] = 'Red'
# remove item in dict
del thisdict['year']
del thisdict