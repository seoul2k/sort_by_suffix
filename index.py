import os
dir = input("请输入目录:")
for file in os.listdir(dir):
    suffix = os.path.splitext(file)[1]
    try:
        with open(file)as f:
            s = f.read()
        os.makedirs(suffix.replace('.', ''))
    except Exception:
        pass
    with open("./"+suffix.replace('.', '')+'/'+file, 'w')as w:
        w.write(s)
