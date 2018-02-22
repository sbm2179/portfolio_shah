# -*- coding: utf-8 -*-
"""
Created on Tue May 02 16:50:38 2017

@author: Shah Faisal Mazhar
"""
#Keep this .py file with the data file to get the result
import xml.etree.cElementTree as ET
#Loading the xml file
tree=ET.ElementTree(file="CsI.xml")
root=tree.getroot()
#Creating seperate files for each of the waveform 
for events in root:
    if(events.tag=="event"):
        fo=open(events.get("id")+".txt","wb")
        for attr in events:
            if(attr.tag=="trace"):
                fo.write(attr.text)