

from socket import *
import struct

fmt = 'i32sif'
ADDR = ('127.0.0.1',8888)

s = socket(AF_INET,SOCK_DGRAM)

while True:
    print("\n*****************************")
    stu_id = int(input("ID:"))
    stu_name = input("Name:")
    stu_age = int(input("Age:"))
    stu_score = float(input("Score:"))

    data = struct.pack(fmt,stu_id,stu_name.encode(),stu_age,stu_score)
    s.sendto(data,ADDR)

s.close()