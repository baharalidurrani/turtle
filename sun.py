from turtle import *

# forward(100)

color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
# done()

input("Press Enter to exit")