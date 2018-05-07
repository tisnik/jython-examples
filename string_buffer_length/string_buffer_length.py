from java.lang import StringBuffer

s = StringBuffer("Hello world!")

print(s.length())
print(s)
print("")

s.setLength(11)

print(s.length())
print(s)
print("")

s.length = 5

print(s.length())
print(s)
print("")

