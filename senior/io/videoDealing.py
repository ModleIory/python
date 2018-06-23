with open("../source/vedio.mp4","rb") as vedio:
    with open("../source/vedio.txt",'wb') as file:
        file.write(vedio.read())