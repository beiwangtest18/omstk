#coding=utf-8

import xml.dom.minidom as xmldom
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

xmlfilepath = os.path.abspath("./test/functional/WhackaPodUIAuto/config/ServerConfig.xml")
domobj = xmldom.parse(xmlfilepath)
elementobj = domobj.documentElement
subElementObj = elementobj.getElementsByTagName("UIAdvancedUrl")
print(subElementObj[0].firstChild.data)
