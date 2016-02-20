import xml.etree.ElementTree as ET

recipe=ET.parse('../TNE.xml')
root=recipe.getroot()
ings = []
for child in root.iter('ingredients'):
    for ing in child:
        item = ing.find('item').text
        code = ing.find('item').get('value')
        amt = ing.find('amt').find('qty').text
        if(ing.find('amt').find('unit')!=None):
            unit=ing.find('amt').find('unit').text
        else:
            unit=""

        iing=(item,amt,unit,code)
        ings.append(iing)

for i in ings:
    print i
directions=[]
count=0
for child in root.iter("direstions"):
    for step in child:
        st=step.text
        if 'action' in step.attrib:
            action=step.get('action')
        else:
            action=""
        if 'ing' in step.attrib:
            ing=step.get('ing')
        else:
            ing=""
        if 'time' in step.attrib:
            t=step.get("time")
        else:
            t='0'
        #print st+" act "+action+" ing "+ing+" time "+t
        direction=(count,st,action,ing,t)
        count +=1
        directions.append(direction)


for i in directions:
    print i
