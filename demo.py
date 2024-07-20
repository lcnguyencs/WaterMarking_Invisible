from PIL import Image, ImageDraw, ImageFont

# Open the image file
demo_image = Image.open('image.jpg')
img_width, img_height = demo_image.size

# Create a drawing object
draw_image = ImageDraw.Draw(demo_image)

# Define the text and font
text_image = "Visible Watermark"
font_image = ImageFont.truetype('Roboto-Italic.ttf', 30)

# Calculate text size
text_bbox = draw_image.textbbox((0, 0), text_image, font=font_image)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

# Define margin and calculate position
font_margin = 40
x = (img_width - text_width) / 2
y = font_margin

# Draw the text on the image
draw_image.text((x, y), text_image, font=font_image)

# Show the image
demo_image.show()

# Save the modified image
demo_image.save("watermark.jpg")