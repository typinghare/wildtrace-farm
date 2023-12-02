from pygame import Rect

rect1 = Rect(0, 0, 50, 50)
rect2 = Rect(25, 25, 50, 50)
rect3 = Rect(75, 75, 50, 50)

print(rect1.colliderect(rect2))
print(rect1.colliderect(rect3))
