#!/usr/bin/env python
# vim: set fileencoding=utf-8

from java.awt import Color
from java.lang import StringBuffer
from java.awt import Button



print("\nButton")

b = Button("label")
print(b.getLabel())
print(b.label)

b.setLabel("new label")
print(b.getLabel())
print(b.label)

b.label = "yet another label"
print(b.getLabel())
print(b.label)

print("\nb")
b.background = Color.RED
print(b.background)

print("\nb2")
b2 = Button(label = "label", background = Color.GREEN)
print(b2.background)
