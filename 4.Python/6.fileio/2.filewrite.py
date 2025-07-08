file_path = "test.txt"

# 파일을 읽을때의 "모드"
# r = read w = write(새로쓰기) a = append(이어쓰기)
with open(file_path, "w", encoding= 'utf-8') as file: #열고 닫고 (with)
    file.write("Hello") #| 누ㅠ라인 - 줄바꿈 캐릭터
    file.write("안녕!")  
    




