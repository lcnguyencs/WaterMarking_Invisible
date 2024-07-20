from PIL import Image, ImageDraw, ImageFont

def embed_text(image_path, text, font_path, font_size, margin, output_path):
    # Open the image
    image = Image.open(image_path).convert('RGB')
    draw = ImageDraw.Draw(image)
    
    # Load the font
    font = ImageFont.truetype(font_path, font_size)
    
    # Calculate text bounding box
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    # Calculate text position
    img_width, img_height = image.size

    x = (img_width - text_width) / 2
    y = margin
    
    # Create a temporary image to draw the text
    temp_img = Image.new('1', (img_width, img_height), color=0)
    temp_draw = ImageDraw.Draw(temp_img)
    temp_draw.text((x, y), text, font=font, fill=1)
    
    # Embed the text into the image using LSB technique
    pixels = image.load()
    temp_pixels = temp_img.load()
    
    for i in range(img_width):
        for j in range(img_height):
            r, g, b = pixels[i, j]
            if temp_pixels[i, j] == 1:
                r = (r & ~1) | 1  # Set LSB to 1
            else:
                r = (r & ~1)  # Set LSB to 0
            pixels[i, j] = (r, g, b)
    
    # Save the modified image
    image.save(output_path)

# Example usage
embed_text('input_image.jpg', 'Invisible Watermarking', './Roboto-Italic.ttf', 30, 30, 'embedded_image.png')