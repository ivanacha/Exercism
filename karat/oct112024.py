'''
Our sensor technology has received a major upgrade, and now provides two-dimensional images using nested arrays.

- Every pixel is still a 1 or a 0.
- The image will contain exactly one rectangle of 0s on a background of 1s.
- We consider the top left pixel of the images to be at position 0,0.

Write a function that takes the image as input and returns the row and column indices of the rectangle's top-left corner.

You can choose to reuse or modify first_zero or get_width, or start over.

Sample input and output:

image1 = [
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 0, 0, 0, 1],
  [1, 1, 1, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1, 1],
]
find_rectangle(image1) => (2,3)  row, column

image2 = [
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 0],
]
find_rectangle(image2) => (4,6)

image3 = [
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 0, 0],
  [1, 1, 1, 1, 1, 0, 0],
]
find_rectangle(image3) => (3,5)
  
image4 = [
  [0, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
]
find_rectangle(image4) => (0,0)

image5 = [
  [0],
]
find_rectangle(image5) => (0,0)

Complexity Analysis variables:

w: width
h: height

'''


def first_zero(image):
    for idx, pixel in enumerate(image):
        if pixel == 0:
            return idx

def get_width(image):
    width = 0
    for idx in range(len(image)):
        if image[idx] == 0:
            width += 1
    return width

def find_rectangle(image):
    for row in range(len(image)):
        for col in range(len(image[row])):
            return (first_zero(image[row], col))
                   
          
image1 = [
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 0, 0, 0, 1],
  [1, 1, 1, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1, 1],
]
print(find_rectangle(image1)) # (2,3)  row, column

image2 = [
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 0],
]
print(find_rectangle(image2)) # (4,6)

image3 = [
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 0, 0],
  [1, 1, 1, 1, 1, 0, 0],
]
print(find_rectangle(image3)) # (3,5)
  
image4 = [
  [0, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
]
print(find_rectangle(image4)) # (0,0)

image5 = [
  [0],
]
print(find_rectangle(image5)) # (0,0)