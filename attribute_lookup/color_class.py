#!/usr/bin/env python
# vim: set fileencoding=utf-8

from java.awt import Color
from java.lang import StringBuffer
from java.awt import Button


color = Color(0.5, 1.0, 0.0)

print("\nRed")
print(color.getRed())
print(color.red)

print("\nGreen")
print(color.getGreen())
print(color.green)

print("\nBlue")
print(color.getBlue())
print(color.blue)

print("\nTransparency")
print(color.getTransparency())
print(color.transparency)
