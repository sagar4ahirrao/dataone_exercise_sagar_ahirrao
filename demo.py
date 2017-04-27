import csv, operator, sys

file = sys.argv[1]
csvfile = open(file)
data = []
readCSV = csv.reader(csvfile, delimiter=',')
for row in readCSV:
    shop_id = int(row[0])
    price = float(row[1])
    product = str(row[2])
    data.append([shop_id, price, product])

ch = sys.argv[2]
ch1 = sys.argv[3]
d = {}
d1 = {}
shop_data = {}

for  i in data:
    if i[2] == ch:
        d[i[0]]=i[1]
    if i[2] == ch1:
        d1[i[0]]=i[1]

if (d1 and d):
    for i in d:
        for j in d1:
            if i == j :
                shop_data[i]=d[i]+d1[i]
    if shop_data:
        print "shop no",min(shop_data.iteritems(), key=operator.itemgetter(1))[0],"with price",min(shop_data.values())
    else:
        print "none"
else:
    print "none"
