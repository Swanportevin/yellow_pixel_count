from PIL import Image

# Open the image file
image = Image.open('bild2.png')
b = 0
# Get the size of the image in pixels
width, height = image.size

# Set the color threshold for yellow (R, G, B)
yellow_threshold = (200, 200, 0)

# Create a new image with the same dimensions as the original image
yellow_image = Image.new('RGB', (width, height), color='white')

# Loop over each pixel in the image and set the corresponding pixel in the new image to yellow
for x in range(width):
    for y in range(height):
        pixel = image.getpixel((x, y))
        if pixel >= yellow_threshold :
            yellow_image.putpixel((x, y), (255, 255, 0))
            b += 1
c = x * y
# Save the new yellow image
yellow_image.save('images/bild2.jpg')
print('b-->',b,'c--->', c, b/c*100)
