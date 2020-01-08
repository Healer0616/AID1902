import os
os.makedirs("file_demo/a/")
with open("file_demo/a/my_file01.txt","w",encoding="utf-8") as my_file:
    my_file.write("写入文字\n")
    my_file.write("a\n")
    my_file.write("b\n")
    my_file.write("c\n")
    my_file.write("d\n")