from maltego import *
import sys
import requests
from lxml import html

cuit_arg = sys.argv[1]

page = requests.get("https://www.cuitonline.com/detalle/"+cuit_arg+"/") 
tree = html.fromstring(page.content)
nombre = str(tree.xpath('//span[@itemprop="name"]/text()')) 

me = MaltegoTransform()
me.addEntity("Person", nombre)
me.returnOutput()
