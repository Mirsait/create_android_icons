# конвертация png в webp

import os
import PIL
import glob
from PIL import Image

src_image = 'launcher.png'
ic_name = 'ic_launcher'
res_folder = 'results'

destinations = [
    {'folder': 'mipmap-hdpi', 'size': (72, 72)},
    {'folder': 'mipmap-mdpi', 'size': (48, 48)},
    {'folder': 'mipmap-xhdpi', 'size': (96, 96)},
    {'folder': 'mipmap-xxhdpi', 'size': (144, 144)},
    {'folder': 'mipmap-xxxhdpi', 'size': (192, 192)},
]


def create_folder(src: str, folder: str) -> (bool, str):
    """ Create folder {folder} in folder {src}."""

    dest = os.path.join(src, folder)
    if (os.path.exists(dest)):
        return True

    try:
        os.mkdir(dest)
    except OSError:
        print(f"Error: creation of the directory {dest} failed")
        return False
    else:
        print(f"OK: successfully created the directory {dest}")
        return True


def create_dest_folders() -> bool:
    """ Create all folders """

    global src_image
    global res_folder

    cwd = os.getcwd()
    print('current folder: {0}'.format(cwd))
    src_image = os.path.join(cwd, src_image)

    # создает папки в текущей
    success = create_folder(cwd, res_folder)
    if (success):
        res_folder = os.path.join(cwd, res_folder)
        for destination in destinations:
            success = create_folder(res_folder, destination['folder'])
            if success is False:
                return False
    return success


def thumbnail(src_img: str, dest_img: str, size: (int, int)):
    print(f'size: {size}')
    image = Image.open(src_img)
    image.thumbnail(size, Image.ANTIALIAS)
    image.save(dest_img, 'WEBP')


def convert():
    """resize, convert and save thumbnails"""
    global src_image
    global res_folder
    src_image = os.path.join(res_folder, src_image)
    for dest in destinations:
        dest_image = os.path.join(
            res_folder, dest['folder'], f'{ic_name}.webp')
        dest_size = dest['size']
        thumbnail(src_image, dest_image, dest_size)


if __name__ == "__main__":
    is_exist_folders = create_dest_folders()
    if (is_exist_folders):
        convert()
        print('done')
    else:
        print("folders don't exist")
