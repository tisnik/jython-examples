#!/usr/bin/env python
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2018  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

from java.lang import String

import java.util.Date
import java.math.BigInteger


def date_test():
    print "Date test"

    d = java.util.Date()
    print d
    print d.getYear()

    print


def string_test():
    print "String test"

    s = String("42")
    print s
    print type(s)

    s2 = s.toUpperCase()
    print s2
    print type(s2)

    print


def big_integer_test():
    print "Big integer test"

    b = java.math.BigInteger("2")
    print b
    print type(b)
    result = type(b.pow(10000))
    print result
    print type(result)

    print


def java_interop():
    date_test()
    string_test()
    big_integer_test()


if __name__ == "__main__":
    java_interop()
