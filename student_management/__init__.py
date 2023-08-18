import os


if not os.path.exists("data.json"):
    open(file="data.json", mode='w').close()
    print("File Created!")

