import os
import urllib.request
import zipfile

def image_files(train_file = "train.zip",train_folder = "train"):
    if not os.path.exists(train_file):
        urllib.request.urlretrieve("https://www.dropbox.com/s/8lbkqktfofzjraj/train.zip?raw=1", train_file)
        print("Done")
    else:
        print("data file {} has already been downloaded".format(train_file))

    # unzip files
    # If folder train does not exists extract all elements
    if not os.path.exists(train_folder):
        with zipfile.ZipFile(train_file, 'r') as myzip:
            myzip.extractall()
        print("Extracted")
    else:
        print("Data has already been extracted")

    return [os.path.join("train",img) for img in os.listdir("train")]
