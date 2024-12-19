# open()

# "x"-tạo file
# f=open("vidu2.txt","x")
# try:
#     f = open("vidu1.txt", "x")
# except Exception as err:
#     print(err)
# finally:
#     f.close()

# ghi  file
# "w"-ghi dữ liệu file

try:
    with open("vidu1.txt", "w") as f:
        f.write("helloword\n")
        f.close()
except Exception as err:
    print(err)

# "a"-nối và0 file
try:
    with open("vidu1.txt", "a") as f:
        f.write("helloword\n ")
        f.close()
except Exception as err:
    print(err)

# "r"-đọc file
try:
    with open("vidu1.txt", "r") as f:
        noiDung = f.read()
        print(noiDung)
        # f.close()
except Exception as err:
    print(err)

# "r"-đọc tấtc cả các dòng trong file
# try:
#     with open("vidu1.txt", "r") as f:
#         listNoiDung = f.readlines()
#         i = 1
#         for noidung in listNoiDung:

#             print(str(i) + ": " + noiDung)
#             i+=1
#             # f.close()
# except Exception as err:
#     print(err)


try:
    with open("vidu1.txt", "r") as f:
        noiDung = f.readlines()
        print(noiDung)
            # f.close()
except Exception as err:
    print(err)






# endcoding=utf-8
f=open()
f=open("sample-file.txt",encoding="utf-8")
f=open("sample-file.txt",mode='w',encoding='utf-8')


# file có 2 dang
#"t":text
#"b" :"binary"