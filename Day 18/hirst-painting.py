import colorgram

colors = colorgram.extract("image.jpg", 6)

for color in colors:
    print(color.rgb)
