import os
import numpy as np
import pandas as pd
import sys

mypath = "img"

#This singleton helps when it comes to have a single class that manages the images and the results
class ImageGetterSingleton(object):
    #this is the class that is used
    class __ImageGetterSingleton:
        def __init__(self):
            #The images are considered only if they are not in the dataset
            self.__dataframe = pd.read_csv("dataset.csv")
            self.__names = np.setdiff1d([filen for filen in os.listdir(mypath)],[self.__dataframe.iloc[:,0]])
            print(self.__names)
            self.__indx = 0
            self.current_img = mypath + "\\\\" +self.__names[self.__indx]
            #TODO questa variabile dice se devono essere settate le fonti luminose
            self.__light = None
            self.__orientation = None
            self.__light_to_be_Set = True
            self.background_changed = True

        def set_params(self, position):
            if self.__light_to_be_Set:
                #Saves the lights position
                self.__light = self.__one_hot_encoder(position)
                self.__light_to_be_Set = False
                print("Now set the orientation of the face")
                return "Now set the orientation of the face"
            else:
                #Saves the face orientation
                self.__orientation = self.__one_hot_encoder(position)
                self.__light_to_be_Set = True
                return self.pop()

        #Moves to the following image.
        #The current image is stored only both orientation and lights are set
        def pop(self):
            if self.__light != None and self.__orientation != None:
                self.__dataframe.loc[len(self.__dataframe)] = [self.__names[self.__indx]] + self.__light + self.__orientation
                self.__light = None
                self.__orientation = None
            self.background_changed = True
            self.__indx -= -1
            if self.__indx == len(self.__names):
                self.quit()
                sys.exit()
            print(self.__names[self.__indx])
            self.__light_to_be_Set = True
            print("Set the light source in this image")
            self.current_img = mypath + "\\\\" + self.__names[self.__indx]
            return self.__names[self.__indx] + "\nSet the light source in this image"

        def quit(self):
            self.__dataframe.to_csv("dataset.csv", encoding='utf-8', index=False)

        def __one_hot_encoder(self, position):
            list = [0,0,0]
            if -1 < position < 3:
                list[position] = 1
            else:
                print("errore posizione sbagliata nel one hot encoder")
            return list.copy()


        def __str__(self):
            return 'self' + self.val


    instance = None

    #this is the actual singleton operations
    def __new__(cls): # __new__ always a classmethod
        if not ImageGetterSingleton.instance:
            ImageGetterSingleton.instance = ImageGetterSingleton.__ImageGetterSingleton()
        return ImageGetterSingleton.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)
