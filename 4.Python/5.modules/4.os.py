import os

# 현재 디렉토리를 가져온다 cwd = current working directory
print(os.getcwd())

new_directory = "sesac1234"
os.mkdir(new_directory)

# 시스템콜..
os.rmdir(new_directory)
# 삭제

os.chdir("..") # .은 현재 디렉토리, ..은 부모 디렉토리

# os.chdir(new_directory)
# 이동완료