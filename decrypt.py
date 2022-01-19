from PIL import Image, ImageDraw

def decrypt():
  original = Image.open('original.png')
  message = Image.open('result.png')
  draw = ImageDraw.Draw(original)
  width = message.size[0]
  height = message.size[1]
  pix = message.load()
  original_pix = original.load()
  mostUsedPixel = (original_pix[20, 20][0], original_pix[20, 20][1], original_pix[20, 20][2])
  for x in range(width):
    for y in range(height):
      r = pix[x, y][0]
      g = pix[x, y][1]
      b = pix[x, y][2]
      if mostUsedPixel == (r, g, b):
        draw.point((x, y), (255, 255, 255))
      else:
        draw.point((x, y), (0, 0, 0))
  original.save('result_message.png', 'PNG')

decrypt()
