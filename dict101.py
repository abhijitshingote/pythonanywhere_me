abhidic={}
abhidic['attrib']='property'
abhidic['class']='emptyblueprint'
abhidic['dictionar']='keyvalue_{}'
abhidic['tuple']='fasterlist_cantchangeitems ()'
abhidic['list']='canchangeitems_andindex []'
extra={'module':'greatforimport',
                    'while':'greatforunknownsize',
                    'find':'greatforindexsearching'
                    }
abhidic.update(extra)
print(abhidic)

for i,j in abhidic.items():
    print('\n'+i+': '+j)