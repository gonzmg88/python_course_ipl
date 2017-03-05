# Basic python workshop
This repo contains a basic python course for the [image and signal processing group](http://isp.uv.es/) at IPL. It covers basic syntax and  some scientific python packages like `numpy`, `matplotlib` and `sklearn`. It focuses in image classification.

[slides](https://gonzmg88.github.io/python_course_ipl/index.slides.html).

The goal will be to make some predictions for the dogs vs cats classification problem [kaggle competition](https://www.kaggle.com/c/dogs-vs-cats-redux-kernels-edition)

## Requirements
* **Laptop**
* Download in advance:
  * Anaconda for python 3.5 https://www.continuum.io/downloads 
  * Train images: https://www.dropbox.com/s/8lbkqktfofzjraj/train.zip?raw=1
  * clone/download this repo.

## Program
The workshop outline is the following:

The workshop is divided in two parts dessigned to be covered in two days (~3-4h each day):

### Part I
* Preliminars:
  * What's python?
  * Why python?
  * Installing python
  * `jupyter` notebook basics
* Python language (`basic_syntax.ipynb`):
  * Basic syntax and core structures (loops, functions, lists, ifs, strings...classes, dicts)
  * file operations (list directory, r/w files, get data from web,...)
  * Example dogs vs cats.
* `numpy` (`numpy.ipynb`):
  * basic matrices
  * read image as matrix
  * basics on matrix transformations.

### Part II
* `scikit-learn` (`machine_learning.ipynb`):
  * predict label on image
  * hyper-parameter selection via cross-validation
  * show prediction metrics (accuracy, ROC, confussion matrix).
* Deep learning (`deep_learning.ipynb`):
  * Use pretrained CNN with `keras`.
* Conclussions:
  * my way of working.
  * Where to go to learn more.

