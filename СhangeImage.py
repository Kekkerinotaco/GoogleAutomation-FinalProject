#!/usr/bin/env python3

import os
from PIL import Image


def main():
    """ The module processes the images in /supplier-data/images folder

    :return:
    """
    images_folder = "/home/student-01-9605b3a73d76/supplier-data/images"
    for root, folders, files in os.walk(images_folder):
        for file in files:
            if file.endswith(".tiff"):
                print(file)
                change_image(root, file)


def change_image(root, file):
    """ The function changes image

    :param root: path to the image
    :param file: image filename
    :return:
    """
    input_file_path = os.path.join(root, file)
    file_name, file_ext = os.path.splitext(file)
    result_file_path = os.path.join(root, file_name)
    result_file_path = result_file_path + ".jpeg"
    image = Image.open(input_file_path)
    image = image.convert("RGB")
    resized_image = image.resize((600, 400))
    resized_image.save(result_file_path)


if __name__ == '__main__':
    main()
