import csv

csvfile = open('data.csv')
data = []
readCSV = csv.reader(csvfile, delimiter=',')
for row in readCSV:
    shop_id = int(row[0])
    price = float(row[1])
    product = str(row[2])
    data.append([shop_id,price,product])

ch = raw_input("enter 1st: ")
ch2 = raw_input("enter 2nd: ")
s=[]
s1=False
d = {}
d1 = {}
for  i in data:
    if i[2] == ch:
        d[i[0]]=i[1]
    if i[2] == ch2:
        d1[i[0]]=i[1]


# if not s1:
for i in d:
    for j in d1:
        if i == j :
            s.append([i,d[i]+d1[i]])
print s
# if s[0][1] < s[1][1]:
#     print s[0][0],s[0][1]
# else:
#     print s[1][0],s[1][1]

for i in s:
    print i
# else:
#  print "none"



# print d,d1