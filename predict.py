import tensorflow as tf
import os
from tensorflow import keras
import cv2
import matplotlib.pyplot as plt
import  numpy as np
SIZE = 120
model = keras.models.load_model("F:/anna_university aka/alzheimer_stage_detection_github/alzheimer-stage-classifier_final/model/model.h5")
categories = ["NonDemented", "MildDemented", "ModerateDemented", "VeryMildDemented"]

nimage = cv2.imread("F:/anna_university aka/alzheimers_data/test/VeryMildDemented/26 (66).jpg", cv2.IMREAD_GRAYSCALE)
image = cv2.resize(nimage,(SIZE,SIZE))
image = image/255.0
prediction = model.predict(np.array(image).reshape(-1,SIZE,SIZE,1))
pclass = np.argmax(prediction)
plt.imshow(image,cmap="gray")
pValue = "Prediction: {0}".format(categories[int(pclass)])
plt.title(pValue)
realvalue = "Real Value 1"
plt.figtext(0,0,realvalue)
plt.show()
# import os
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# from tensorflow import keras
# import tensorflow as tf
# from model import createModel


# def predict(SIZE):
#     categories = ["NonDemented", "MildDemented", "ModerateDemented", "VeryMildDemented"]

#     path = "F:/anna_university aka/alzheimers_data/test/ModerateDemented/"
#     images = []
#     for img in os.listdir(path):
#         data = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
#         new_data = cv2.resize(data, (SIZE, SIZE))
#         new_data = new_data / 255.0
#         images.append(new_data)
#     model = createModel()
#     title = os.listdir('F:/anna_university aka/alzheimers_data/test/ModerateDemented')
#     print(len(title))
#     x = 0
#     for img ,indx,value in images,enumerate(title):
#         image = np.array(img).reshape(-1, SIZE, SIZE, 1)
#         prediction = model.predict(image)
#         plt.imshow(img, cmap="gray")
#         ptitle = "Prediction: {0}".format(categories[np.argmax(prediction)])

#         plt.figtext(0, 0, title[indx])
#         plt.title(ptitle)
#         plt.show()
#         print(prediction)


#     print(len(images), len(title))


# predict(128)
