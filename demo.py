import csv, operator

csvfile = open('data.csv')
data = []
readCSV = csv.reader(csvfile, delimiter=',')
for row in readCSV:
    shop_id = int(row[0])
    price = float(row[1])
    product = str(row[2])
    data.append([shop_id,price,product])

ch = raw_input("enter 1st: ")
ch1 = raw_input("enter 2nd: ")
s={}
d = {}
d1 = {}
for  i in data:
    if i[2] == ch:
        d[i[0]]=i[1]
    if i[2] == ch1:
        d1[i[0]]=i[1]

if (d1 and d):
    for i in d:
        for j in d1:
            if i == j :
                s[i]=d[i]+d1[i]
    if s:
        print "shop no",min(s.iteritems(), key=operator.itemgetter(1))[0],"with price",min(s.values())
    else:
        print "none"
else:
    print "none"
