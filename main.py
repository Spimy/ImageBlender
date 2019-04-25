import os
from PIL import Image, ImageDraw, ImageFont

# Get all image files
pngs = [file for file in os.listdir(".") if file.endswith(".png") or file.endswith(".jpg")]
top = pngs[::2]
bottom = pngs[1::2]

# Intialize canvas and text
canvas = Image.new("RGB", (1080, 1080))
w, h = canvas.size
name = "@OfficialSpimy"

# Create output folder if it doesn't exist
if not os.path.exists("./output"):
	os.mkdir("./output")

# Loop over all images
for i in range(0, len(top)):

	# Open appropriate images to paste on canvas
	img = Image.open(f"{top[i]}")
	img2 = Image.open(f"{bottom[i]}")

	# Resize image to fit the canvas
	img = img.resize((w,h//2))
	img2 = img2.resize((w, h//2))

	# Paste images on canvas
	canvas.paste(img)
	canvas.paste(img2, (0,1080//2))

	# Intialise font and draw
	font = ImageFont.truetype("impact.ttf", 30)
	draw = ImageDraw.Draw(canvas)

	# Get size of text to be draw
	w_t, h_t = draw.textsize(name, font)

	# Draws outline for the text
	draw.text(((w-w_t)-7, h//2), name, "black", font)
	draw.text(((w-w_t)-13, h//2), name, "black", font)
	draw.text(((w-w_t)-10, (h//2)+3), name, "black", font)
	draw.text(((w-w_t)-10, (h//2)-3), name, "black", font)

	# Overlay the actual text over the outlines
	draw.text(((w-w_t)-10, h//2), name, "white", font)

	# Save the file
	canvas.save(f"output/{i+1}.png")

input("Done")