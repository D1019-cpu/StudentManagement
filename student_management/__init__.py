import os


if not os.path.exists("data.txt"):
    open(file="data.txt", mode='w',encoding='utf-8').close()
    print("File Created!")

