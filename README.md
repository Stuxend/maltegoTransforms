# MaltegoPython3
Maltego lib for python3 based on [MaltegoTransform-Python](https://github.com/paterva/MaltegoTransform-Python)

## Basic Examples

We will create a Person Entity with a value of "CUIT" for argentinian reverse name.

### Hello World

This transform merely returns "hello world" as a phrase, it doesn't depend on the input entity at all:

``` python
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
```


