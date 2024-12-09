from PIL import Image

def image_to_ascii(image_path, new_width=100):
    image = Image.open(image_path)
    width, height = image.size
    aspect_ratio = height/width
    new_height = int(aspect_ratio * new_width)
    image = image.resize((new_width, new_height))

    grayscale_chars = "@%#*+=-:. "
    pixels = list(image.getdata())
    ascii_str = ""

    for pixel in pixels:
        grayscale_value = sum(pixel) // 3
        ascii_str += grayscale_chars[grayscale_value // 25]

    ascii_str = '\n'.join([ascii_str[i:i+new_width] for i in range(0, len(ascii_str), new_width)])
    return ascii_str

# Example usage
ascii_art = image_to_ascii("example_image.jpg", new_width=120)
print(ascii_art)
