import os
import urllib.request
import zipfile
import numpy as np
from scipy import ndimage
import skimage.transform as sktrans

def image_files(train_file = "train.zip",train_folder = "train"):
    """ Download the training data from dropbox if it has not been downloaded and extract in train_folder folder."""
    if not os.path.exists(train_file):
        print("Proceding to download the data. This process may take some time..")
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


def sample_image_set(all_files, n_images=4000,image_size=(50,50,3)):
    """ Returns a sample of n_images flattened and compressed to size image_size
    If image_size is (a,b,1) or (a,b) images will be converted to gray scale.
    """
    index_files_selected = np.random.choice(len(all_files),size=n_images,replace=False)
    feature_array = np.ndarray((n_images,np.multiply.reduce(image_size)),dtype=np.float64)
    label = np.ndarray((n_images),dtype=np.uint8)
    for i,indice in enumerate(index_files_selected):
        image = ndimage.imread(all_files[indice])
        image_down = sktrans.resize(image, image_size)
        if (len(image_size) < 3) or image_size[2] == 1:
            image_down = np.mean(image_down,axis=2) 
        feature_array[i] = image_down.ravel() # equivalent to feature_array[i,:]
        label[i] = "dog" in all_files[indice]
    
    return feature_array,label
