abhidic={}
abhidic['attrib']='property'
abhidic['class']='emptyblueprint'
abhidic['dictionar']='keyvalue_{}'
abhidic['tuple']='fasterlist_cantchangeitems ()'
abhidic['list']='canchangeitems_andindex []'

print(abhidic)

for i,j in abhidic.items():
    print(i+': '+j)


tuple_=(1,2,3,4343)
for t in tuple_:
    print(t)

i=0
while i<len(tuple_):
    print(tuple_[i])
    i+=1



abhitupe=(11,22,33,44)
print(abhitupe[3])

gradebook = [('Math 212', 'Linear Algebra', 'Fall 2012', 'B'),
             ('CS 130', 'Python', 'Spring 2013', 'A')]

for grade in gradebook:
    for i in grade:
        print(i)

i=0
j=0
while i<len(gradebook):
    while j < len(gradebook[i]):
        print(gradebook[i][j])
        j+=1
    i+=1


i=0

while i<len(gradebook):
    print(gradebook[i][0]+'           ' + gradebook[i][1]+' '+ gradebook[i][2] + '       ' + gradebook[i][3])
    i+=1

for x in gradebook:
    print(x[0], x[1])

