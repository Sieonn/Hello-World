# print('Hello, world')

# f = open("C:Users\MZC-USER\Desktop\매수종목2.txt", encoding="utf-8" )
# lines = f.readlines()

# data = {}
# for line in lines:
#     line = line.strip() #'\n제거'
#     k, v = line.split()

#     data[k] = v
    
# print(data)

# f.close()
# f = open("D:\PythonHome/매수종목2.txt",mode= "wt", encoding="utf-8")
# f.write("005930 삼성전자\n")
# f.write("005380 현대차\n")
# f.write("035420 NAVER\n")
# f.close()

per = ["10.31", "", "8.00"]

new = []
for i in per:
    try:
        v = float(i)
    except:
        print(0)
    new.append(v)
print(new)


