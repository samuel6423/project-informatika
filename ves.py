import PIL
from PIL import Image
def draw_line(img, A, B, color):
  dx = B[0] - A[0]
  dy = B[1] - A[1]
  width, height = img.size
  if dx == 0:
    if A[1] > B[1]:
      A, B = B, A
    for y in range(A[1], B[1]):
      x = A[0]
      if not (x < 0 or y < 0 or x >= width or y >= height):
        img.putpixel((A[0], y), color)

  elif dy == 0:
    for x in range(A[0], B[0]):
      y = 0*x + A[1]
      if not (x < 0 or y < 0 or x >= width or y >= height):
        img.putpixel((x, y), color)

  elif abs(dx) > abs(dy):
    if A[0] > B[0]:
      A, B = B, A
    for x in range(A[0], B[0] + 1):
      y = int((dy)/(dx) * (x - A[0]) + A[1])
      if not (x < 0 or y < 0 or x >= width or y >= height):
        img.putpixel((x, y), color)

  else:
    if A[1] > B[1]:
      A, B = B, A
    for y in range(A[1], B[1] + 1):
      x = int( (dx / dy) * (y - A[1]) + A[0])
      if not (x < 0 or y < 0 or x >= width or y >= height):
        img.putpixel((x, y), color)

def get_line_pixels(img, A, B):
    w, h = img.size
    x1, y1 = A
    x2, y2 = B
    dx, dy = x2 - x1, y2 - y1
    pixel = []

    if abs(dx) >= abs(dy):
        step = 1 if dx >= 0 else -1
        for x in range(x1, x2 + step, step):
            y = int(y1 + dy * (x - x1) / dx) if dx else y1
            if 0 <= x < w and 0 <= y < h:
                pixel.append((x, y))
    else:
        step = 1 if dy >= 0 else -1
        for y in range(y1, y2 + step, step):
            x = int(x1 + dx * (y - y1) / dy)
            if 0 <= x < w and 0 <= y < h:
                pixel.append((x, y))

    return pixel


def draw_pixel(img, X, farba):
  width, heigh = img.size
  x, y = X
  if not (x < 0 or y < 0 or x >= width or y >= heigh):
    img.putpixel(X, farba)

def thick_line(img, A, B, hrubka, color):
  for pixel in get_line_pixels(img, A, B):
    fill_circle(img, pixel, hrubka, color)
def circle(img, A, r, hrubka, color):
  S = A
  for x in range(0, int(r / (2**0.5)) + 1):
    y = int((r**2 - x**2)**0.5)
    fill_circle(img, (x + S[0], y + S[1]), hrubka, color)
    fill_circle(img, (y + S[0], x + S[1]), hrubka, color)
    fill_circle(img, (y + S[0], -x + S[1]), hrubka, color)
    fill_circle(img, (x + S[0], -y + S[1]), hrubka, color)
    fill_circle(img, (-x + S[0], -y + S[1]), hrubka, color)
    fill_circle(img, (-y + S[0], -x + S[1]), hrubka, color)
    fill_circle(img, (-y + S[0], x + S[1]),hrubka, color)
    fill_circle(img, (-x + S[0], y + S[1]), hrubka, color)


def fill_circle(img, S, r, color):
  for x in range(0, int(r / (2**0.5)) + 1):
    y = int((r**2 - x**2)**0.5)

    draw_line(img, (x + S[0], y + S[1]), (x + S[0], -y + S[1]), color)
    draw_line(img, (y + S[0], x + S[1]), (y + S[0], -x + S[1]), color)
    draw_line(img, (-x + S[0], -y + S[1]), (-x + S[0], y + S[1]), color)
    draw_line(img, (-y + S[0], -x + S[1]), (-y + S[0], x + S[1]), color)
def fill_rect(img, A, B, color):
  ax, ay = A
  width, height = B
  bx, by = ax + width, ay + height
  img_w, img_h = img.size

  if ax > bx:
    ax, bx = bx, ax
  if ay > by:
    ay, by = by, ay

  # Clip to image bounds
  ax = max(0, min(ax, img_w))
  bx = max(0, min(bx, img_w))
  ay = max(0, min(ay, img_h))
  by = max(0, min(by, img_h))

  for x in range(ax, bx):
    for y in range(ay, by):
      img.putpixel((x, y), color)
def triangle(obrazok, A, B, C, hrubka, color):
  thick_line(obrazok, A, B, hrubka, color)
  thick_line(obrazok, B, C, hrubka, color)
  thick_line(obrazok, A, C, hrubka, color)

def fill_triangle(img, A, B, C, color):
  ymin = min(A[1], B[1], C[1])
  ymax = max(A[1], B[1], C[1])

  if ymin < 0:
    ymin = 0
  if ymax >= img.height:
    ymax = img.height - 1

  pixels = get_line_pixels(img, A, B) + get_line_pixels(img, B, C) + get_line_pixels(img, C, A)

  xmin = [img.width] * (ymax + 1)
  xmax = [-1] * (ymax + 1)

  for p in pixels:
    x, y = p

    if y > ymax or y < ymin:
      continue

    if x < xmin[y]:
      xmin[y] = x
    if x > xmax[y]:
      xmax[y] = x

  for y in range(ymin, ymax + 1):
    if xmin[y] <= xmax[y]:
      draw_line(img, (xmin[y], y), (xmax[y], y), color)

def rect(img, A, B, hrubka, color):
    ax, ay = A
    w, h = B
    bx, by = ax + w, ay + h

    x1 = min(ax, bx)
    x2 = max(ax, bx)
    y1 = min(ay, by)
    y2 = max(ay, by)

    thick_line(img, (x1, y1), (x2, y1), hrubka, color)
    thick_line(img, (x2, y1), (x2, y2), hrubka, color)
    thick_line(img, (x1, y1), (x1, y2), hrubka, color)
    thick_line(img, (x1, y2), (x2, y2), hrubka, color)

def desatdosest(cislo):
   a = ""
   if cislo == 0:
     return "0"
   while cislo > 0:
    zvysok = cislo % 16

    if zvysok == 10:
      zvysok = "A"
    elif zvysok == 11:
      zvysok = "B"
    elif zvysok == 12:
      zvysok = "C"
    elif zvysok == 13:
      zvysok = "D"
    elif zvysok == 14:
      zvysok = "E"
    elif zvysok == 15:
      zvysok = "F"

    a += str(zvysok)
    cislo = cislo // 16
   return a[::-1]

def sestdodesat(a):
  a = a[::-1]
  sucet = 0
  exp = 0
  for i in a:
    if i == "A":
      sucet += 10 * 16**exp
    elif i == "B":
      sucet += 11 * 16**exp
    elif i == "C":
      sucet += 12 * 16**exp
    elif i == "D":
      sucet += 13 * 16**exp
    elif i == "E":
      sucet += 14 * 16**exp
    elif i == "F":
      sucet += 15 * 16**exp
    else:
      sucet += int(i) * 16**exp
    exp += 1
  return sucet

def farbaz16do10(a):
  r = a[1:3]
  g = a[3:5]
  b = a[5:]
  return sestdodesat(r), sestdodesat(g), sestdodesat(b)

def dec2hex_color(a):
  red, green, blue = a
  r = desatdosest(red)
  if len(r) < 2:
    r = "0" + r
  g = desatdosest(green)
  if len(g) < 2:
    g = "0" + g
  b = desatdosest(blue)
  if len(b) < 2:
    b = "0" + b
  return f"#{r}{g}{b}"
from PIL import Image

def load_subor(a):
  b = []
  try:
    with open(a, "r") as f:
      for riadok in f:
        b.append(riadok.split(" "))
  except FileNotFoundError:
    print("Subor sa nenasiel:", a)
    return None
  return b


def urob_obrazok(a):
  subor = load_subor(a)
  width = int(subor[0][2])
  height = int(subor[0][3].strip())

  from PIL import Image
  img = Image.new("RGB", (width, height), "white")

  for i in range(1, len(subor)):
    pokyn = subor[i][0]

    if pokyn == "CLEAR" and len(subor[i]) == 2:
      fill_rect(img, (0, 0), (width, height),
                farbaz16do10(subor[i][1].strip()))

    elif pokyn == "LINE":
      thick_line(img,(int(subor[i][1]), int(subor[i][2])),
        (int(subor[i][3]), int(subor[i][4])),
        int(subor[i][5]),
        farbaz16do10(subor[i][6].strip()))

    elif pokyn == "RECT":
      rect(img,(int(subor[i][1]), int(subor[i][2])),
        (int(subor[i][3]), int(subor[i][4])),
        int(subor[i][5]),
        farbaz16do10(subor[i][6].strip()) )

    elif pokyn == "TRIANGLE":
      triangle(img,(int(subor[i][1]), int(subor[i][2])),
        (int(subor[i][3]), int(subor[i][4])),
        (int(subor[i][5]), int(subor[i][6])),
        int(subor[i][7]),
        farbaz16do10(subor[i][8].strip()) )

    elif pokyn == "CIRCLE":
      circle(img,(int(subor[i][1]), int(subor[i][2])),
        int(subor[i][3]),
        int(subor[i][4]),
        farbaz16do10(subor[i][5].strip()))

    elif pokyn == "FILL_CIRCLE":
      fill_circle(img,(int(subor[i][1]), int(subor[i][2])),
        int(subor[i][3]),
        farbaz16do10(subor[i][4].strip()))

    elif pokyn == "FILL_TRIANGLE":
      fill_triangle(img,(int(subor[i][1]), int(subor[i][2])),
        (int(subor[i][3]), int(subor[i][4])),
        (int(subor[i][5]), int(subor[i][6])),
        farbaz16do10(subor[i][7].strip()))

    elif pokyn == "FILL_RECT":
      fill_rect(img, (int(subor[i][1]), int(subor[i][2])),
        (int(subor[i][3]), int(subor[i][4])),
        farbaz16do10(subor[i][5].strip()))
  
def parse_ves_string(ves_string):
  b = []
  for riadok in ves_string.strip().split("\n"):
    riadok = riadok.strip()
    if riadok:
      b.append(riadok.split(" "))
  return b

def render_ves(ves_string, target_width=None):
  subor = parse_ves_string(ves_string)
  if not subor:
    return None
    
  width = int(subor[0][2])
  height = int(subor[0][3].strip())

  from PIL import Image
  img = Image.new("RGB", (width, height), "white")

  for i in range(1, len(subor)):
    pokyn = subor[i][0]
    
    if len(subor[i]) == 0:
      continue

    try:
      if pokyn == "CLEAR" and len(subor[i]) >= 2:
        fill_rect(img, (0, 0), (width, height),
                  farbaz16do10(subor[i][1].strip()))

      elif pokyn == "LINE" and len(subor[i]) >= 7:
        thick_line(img,(int(subor[i][1]), int(subor[i][2])),
          (int(subor[i][3]), int(subor[i][4])),
          int(subor[i][5]),
          farbaz16do10(subor[i][6].strip()))

      elif pokyn == "RECT" and len(subor[i]) >= 7:
        rect(img,(int(subor[i][1]), int(subor[i][2])),
          (int(subor[i][3]), int(subor[i][4])),
          int(subor[i][5]),
          farbaz16do10(subor[i][6].strip()) )

      elif pokyn == "TRIANGLE" and len(subor[i]) >= 9:
        triangle(img,(int(subor[i][1]), int(subor[i][2])),
          (int(subor[i][3]), int(subor[i][4])),
          (int(subor[i][5]), int(subor[i][6])),
          int(subor[i][7]),
          farbaz16do10(subor[i][8].strip()) )

      elif pokyn == "CIRCLE" and len(subor[i]) >= 6:
        circle(img,(int(subor[i][1]), int(subor[i][2])),
          int(subor[i][3]),
          int(subor[i][4]),
          farbaz16do10(subor[i][5].strip()))

      elif pokyn == "FILL_CIRCLE" and len(subor[i]) >= 5:
        fill_circle(img,(int(subor[i][1]), int(subor[i][2])),
          int(subor[i][3]),
          farbaz16do10(subor[i][4].strip()))

      elif pokyn == "FILL_TRIANGLE" and len(subor[i]) >= 8:
        fill_triangle(img,(int(subor[i][1]), int(subor[i][2])),
          (int(subor[i][3]), int(subor[i][4])),
          (int(subor[i][5]), int(subor[i][6])),
          farbaz16do10(subor[i][7].strip()))

      elif pokyn == "FILL_RECT" and len(subor[i]) >= 6:
        fill_rect(img, (int(subor[i][1]), int(subor[i][2])),
          (int(subor[i][3]), int(subor[i][4])),
          farbaz16do10(subor[i][5].strip()))
    except Exception as e:
      try:
        print(f"Error parsing line {i}: {e}")
      except OSError:
        pass
      
  if target_width:
    target_width = int(target_width)
    if target_width != width:
      aspect_ratio = height / width
      target_height = int(target_width * aspect_ratio)
      img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
      
  return img
