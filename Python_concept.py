# f - strings in Python
# 3 – Formatted
# string
# literals
# PEP
# 498
# introduced
# a
# new
# string
# formatting
# mechanism
# known as Literal
# String
# Interpolation or more
# commonly as F - strings(because
# of
# the
# leading
# f
# character
# preceding
# the
# string
# literal).The
# idea
# behind
# f - strings is to
# make
# string
# interpolation
# simpler.
#
# To create an
# f - string, prefix the string
# with the letter “ f ”.
# The string itself can be formatted in much the same way that you would with str.format().
# F-strings provide a concise and convenient way to embed python expressions inside string literals for formatting.
#

# Python3 program introducing f-string
val = 'Geeks'
print(f"{val}for{val} is a portal for {val}.")


name = 'Tushar'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")


# Prints today's date with help
# of datetime library
import datetime

today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")

# Note: F - strings
# are
# faster
# than
# the
# two
# most
# commonly
# used
# string
# formatting
# mechanisms, which
# are % formatting and str.format().
#
# Let’s
# see
# few
# error
# examples, which
# might
# occur
# while using f-string:
#
# Code  # 3 : Demonstrating Syntax error.

answer = 456
f"Your answer is "{answer}""
f"newline: {ord('\n')}"
