#! /usr/bin/env python3

import os
import requests
import json


def main():
    """ The script turns .txt file data to JSON format and
        uploads it.

    :return:
    """
    descr_folder = "/home/student-01-9605b3a73d76/supplier-data/descriptions"
    url = "http://localhost/fruits/"
    for root, folders, files in os.walk(descr_folder):
        for file in files:
            if file.endswith(".txt"):
                file_name, e = os.path.splitext(file)
                file_path = os.path.join(root, file)
                with open(file_path, "r") as opened_file:
                    data = opened_file.read().split("\n")
                    fruit_weight = int(data[1].strip(" lbs"))
                    file_name = file_name + ".jpeg"
                    fruts_dict = {"name": data[0], "weight": fruit_weight,
                                  "description": data[2], "image_name": file_name}
                    r = requests.post(url, json=fruts_dict)


if __name__ == '__main__':
    main()
