import xml.etree.ElementTree as ET

tree = ET.parse('../files/users.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)
    for _child in child:
        print(_child.tag, _child.text)
