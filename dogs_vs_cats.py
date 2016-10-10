import os
import urllib.request
import zipfile
import numpy as np
from scipy import ndimage
import skimage.transform as sktrans
from sklearn import metrics
import matplotlib.pyplot as plt

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

def training_test_datasets(all_files,n_images_train=500,n_images_test=500,image_size=(50,50,3)):
    """
    Returns a randomly selected test and train datasets of the specified size.

    :param all_files:
    :param n_images_train:
    :param n_images_test:
    :param image_size:

    :return: train_features, train_labels, test_features, test_labels
    """
    perm = np.random.permutation(len(all_files))
    image_files = np.array(all_files)[perm]
    test_files = image_files[n_images_test:]
    train_files = image_files[:n_images_train]
    print("Loading train set")
    train_features, train_labels = sample_image_set(train_files, n_images=n_images_train, image_size=image_size)

    print("Loading test set")
    test_features, test_labels = sample_image_set(test_files, n_images=n_images_test, image_size=image_size)

    return train_features, train_labels, test_features, test_labels

def plotROC(true_labels, test_probs_model):
    """
    plot ROC curve from true labels and probabilities.

    :param true_labels: true labels.
    :param test_probs_model: probabilities computed by a model (in sklearn usually the output of clf.predict_proba or clf.decision_function)
    :return:
    """
    fpr, tpr, thresholds = metrics.roc_curve(true_labels, test_probs_model)
    roc_auc = metrics.auc(fpr, tpr)

    plt.plot(fpr, tpr, 'k--',
             label='ROC (area = %0.2f)' % roc_auc, lw=2)
    plt.plot([0, 1], [0, 1], '--', color=(0.6, 0.6, 0.6), label='Luck')

    plt.xlim([-0.05, 1.05])
    plt.ylim([-0.05, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic')
    plt.legend(loc="lower right")





