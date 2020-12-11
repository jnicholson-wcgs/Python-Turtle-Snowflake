
import turtle

t = turtle.Turtle()

# Task One
#
# Draw a snowflake
#

def square (size) :
  t.forward (size)
  t.left (90)
  

t.color ('red')

square (100)

input ("Enter return to continue")
