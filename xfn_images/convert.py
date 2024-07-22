from PIL import Image
import struct
import sys
import os

start_path = ''
end_path = ''
def convert_png_to_xfn(png_path, xfn_path):
    image = Image.open(png_path)
    width, height = image.size
    pixels = list(image.getdata())

    with open(xfn_path, 'wb') as file:

        file.write(f"{width} {height}\n".encode('utf-8'))


        pixel_data = []
        for pixel in pixels:
            r, g, b = pixel[:3]
            pixel_data.append((r, g, b))

        for r, g, b in pixel_data:
            file.write(struct.pack('3B', r, g, b))



if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("error: bad arguments")
        sys.exit(1)
    else:
        start_path = sys.argv[1]
        end_path = sys.argv[2]
convert_png_to_xfn(start_path, end_path)
print("Successfully converted image.")
os.system("python3 image.py")