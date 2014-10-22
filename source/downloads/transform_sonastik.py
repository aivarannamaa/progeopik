f = open("sonastik.txt", encoding="utf-8")

dic = {}
for line in f:
    eng, est = line.strip().split("\t")
    dic[eng] = est

f.close()

f = open("sonastik_u.txt", encoding="utf-8", mode="w")

for eng in sorted(dic.keys(), key=str.upper):
    f.write(eng + "\t" + dic[eng] + "\n")

f.close()