#!/usr/bin/env python
# vim: set fileencoding=utf-8

from java.awt import Color
from java.lang import StringBuffer
from java.awt import Button


print("\nString buffer")

s = StringBuffer()
print(s)
print(s.length())

s.append("hello world!")
print(s)
print(s.length())

s.setLength(10)
print(s)
print(s.length())

# nebude fungovat
s.length = 5
print(s)
print(s.length())
