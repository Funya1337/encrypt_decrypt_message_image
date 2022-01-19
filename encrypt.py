from PIL import Image, ImageDraw

def encrypt():
  original = Image.open('original.png')
  message = Image.open('message.png')
  draw = ImageDraw.Draw(original)
  width = message.size[0]
  height = message.size[1]
  pix = message.load()
  original_pix = original.load()
  mostUsedPixel = (original_pix[20, 20][0] + 1, original_pix[20, 20][1] + 1, original_pix[20, 20][2] + 1)
  for x in range(width):
    for y in range(height):
      r = pix[x, y][0]
      g = pix[x, y][1]
      b = pix[x, y][2]
      if r == 0 and g == 0 and b == 0:
        draw.point((x, y), mostUsedPixel)
  original.save('result.png', 'PNG')

encrypt()
