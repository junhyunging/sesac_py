try :
    with open("hello.txt") as file:
        contents = file.read()

    print("파일내용 :" ,contents)
except FileNotFoundError:
    print("파일이 존재하지 않습니다.")
except IOError:
    print("파일을 읽을 수 없습니다.")
except :
    print("파일이 존재하지 않습니다")

    