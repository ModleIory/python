with open("../source/test.jpg","rb") as img:
    stream = img.read()
    print("Already read ...")
    with open("../source/backup.jpg","wb") as back:
        back.write(stream)
        print("Already write in ...")