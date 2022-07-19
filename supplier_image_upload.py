#!/usr/bin/env python3


import os
import requests


def main():
    """ The module uploads changed images

    :return:
    """
    images_folder = "/home/student-01-9605b3a73d76/supplier-data/images"
    for root, folders, files in os.walk(images_folder):
        for file in files:
            if file.endswith(".jpeg"):
                print(file)
                file_path = os.path.join(root, file)
                url = "http://localhost/upload/"
                with open(file_path, "rb") as exported_file:
                    r = requests.post(url, files={"file": exported_file})


if __name__ == '__main__':
    main()
