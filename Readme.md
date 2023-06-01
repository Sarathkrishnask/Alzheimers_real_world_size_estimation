# Alzheimer Stage Classifier

This is my first attempt creating  Convolutional Neural Networks.I created
a CNN to predict  if a patient has Alzheimer's Disease   and to classify the current Alzheimer stage based on patient's brain MRI scan
The CNN has approximately 95% accuracy 

## Stages for classification
The  neural network classifies a patient's brain MRI scan into the following categories
* Non   Demented
* Very Mild Demented
* Mild Demented
* Moderate Demented 

## Dataset
The dataset used can me found [here](https://www.kaggle.com/tourist55/alzheimers-dataset-4-class-of-images). I have merged
the train and test directories found in the dataset , and split them  using **sklearn.modelselection.train_test_split** to  achieve better results in the training process.
## Before you start
Before you start playing with the model run in the repo directory the following command to install the required packages 
for the model to run
```shell script
$ pip install -r requirments.txt
```

## Training the model
To train the model  all you have to do is to run :
```
$ python train.py
```
Make sure the data folder which contains the training data  has not been altered in anyway
  
The model will be saved in the **model**  directory with name "**model.h5**" overwriting the current pre-trained model.
### Training Statistics
##### Model Accuracy 
![accuracy](/images/accuracy.png)

##### Model Loss

![loss](/images/loss.png)


## Using the model for making predictions
To use the model for making predictions first put  brain **MRI** scans in the **test directory**
  
After, run :
```shell script
$ python predict.py 
```
The script will load all the photos located in the test folder and will try to predict the Alzheimer stage based on the
MRI scan

## Alzheimer size estimation

python predict.py 

The calibration python file will load the checkboard image took from the camera used for size estimation from that find the corners of 
the checkboard and corners coordinates send to the contour_.py 

## contour

From the contour_.py file load the corners value from the calibration.py file and mark the mouse clicke point as my coordintes and the clicked
coordinated will take it as input and pass the value to inverse matrix function and polygon area calculation it gives the real world area of
alzheimer affect area in CM square values.