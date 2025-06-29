from PIL import Image

# 이미지 열기
image = Image.open("o.img")

# 이미지 크기를 줄이고 싶음
resized_image = image.resize((400,300))

resized_image.save("small_o.img")
