import os, shutil
# print(os.listdir(r"F:\迅雷下载"))
alredy = os.listdir(r"F:\迅雷下载")
for i in os.listdir(r"F:\迅雷下载"):
    p = os.path.join(r"F:\迅雷下载", i)
    # print(p)
    if not os.path.isfile(p):
        print(p)
        files = os.listdir(p)
        # print(files)
        for file in files:
            if file.endswith(".avi"):
                pp = os.path.join(p, file)
                dst = r"F:\迅雷下载"
                if file not in alredy:
                    shutil.move(pp, dst)