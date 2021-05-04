"""
[STEPIK]
Python: основы и применение https://stepik.org/512
03_06_01 XML, библиотека ElementTree, библиотека lxml
"""

"""
Вам дано описание пирамиды из кубиков в формате XML.
Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue).
Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.

Пример:

<cube color="blue">
  <cube color="red">
    <cube color="green">
    </cube>
  </cube>
  <cube color="red">
  </cube>
</cube>
 
Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 1. 
Кубики, расположенные прямо под ним, имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками, 
имеют ценность 3. И т. д.

Ценность цвета равна сумме ценностей всех кубиков этого цвета.

Выведите через пробел три числа: ценности красного, зеленого и синего цветов.

Sample Input:
<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>

Sample Output:
4 3 1
"""

from xml.etree import ElementTree as ET


# https://docs.python.org/3/library/xml.etree.elementtree.html#xmlparser-objects
class WeightColors:
    depth = 0
    colors = {'red': 0, 'green': 0, 'blue': 0}

    def start(self, tag, attrib):
        self.depth += 1
        self.add_weight(attrib)

    def add_weight(self, attrib):
        self.colors[attrib['color']] += self.depth

    def end(self, tag):
        self.depth -= 1

    def data(self, data):
        pass

    def close(self):
        return self.colors


parser = ET.XMLParser(target=WeightColors())
parser.feed(input())
weighted_colors = parser.close()

print(f'{weighted_colors["red"]} {weighted_colors["green"]} {weighted_colors["blue"]}')

# # Recursion
# tree = ET.fromstring(input())
# colors = {'red': 0, 'green': 0, 'blue': 0}
#
#
# def count_weights(root, weight):
#     colors[root.attrib['color']] += weight
#     for child in root:
#         count_weights(child, weight+1)
#
#
# count_weights(tree, 1)
# print(colors["red"], colors["green"], colors["blue"])
