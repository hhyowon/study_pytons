# 파일 존재 확인
import os

file_path = 'codes/temp_file.txt'

if os.path.exists(file_path) : #존재 여부 return True/False
    # 파일 관련 업무 실행
    with open(file_path,'r') as fr : 
        pass 
        load_file_read = fr.read()
        pass
else : 
    print('Fils Not exists')