import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    check_args()

    try:
        image_file = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit('Input does not exist')

    shirt_file = Image.open('shirt.png')

    size = shirt_file.size
    muppet = ImageOps.fit(image_file, size)
    muppet.paste(shirt_file, shirt_file)
    muppet.save(sys.argv[2])


def check_args():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')

    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])

    if check_exts(file1[1]) == False:
        sys.exit('Invalid input')
    elif check_exts(file2[1]) == False:
        sys.exit('Invalid output')
    elif file1[1].lower() != file2[1].lower():
        sys.exit('Input and output have different extensions')


def check_exts(file):
    if file in ['.jpg', '.jepg', '.png']:
        return True
    return False


if __name__ == '__main__':
    main()