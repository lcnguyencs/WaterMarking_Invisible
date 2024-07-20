from PIL import Image

def reveal_text(image_path, output_path):
    # Open the image
    image = Image.open(image_path).convert('RGB')
    pixels = image.load()
    
    # Create a new image to highlight the embedded text
    highlighted_img = Image.new('RGB', image.size, color='white')
    highlighted_pixels = highlighted_img.load()
    
    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]
            if r & 1:  # Check if the LSB of the red channel is 1
                highlighted_pixels[i, j] = (255, 0, 0)  # Highlight in red
            else:
                highlighted_pixels[i, j] = (255, 255, 255)  # Keep white
    
    # Save the highlighted image
    highlighted_img.save(output_path)

# Example usage
reveal_text('embedded_image.png', 'revealed_image.png')