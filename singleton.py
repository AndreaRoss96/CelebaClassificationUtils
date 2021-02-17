import os
import numpy as np
import pandas as pd
import sys
mypath = "Hey\\img_align_celeba\\img_align_celeba"

#This singleton helps when it comes to have a single class that manages the images and the results
class ImageGetterSingleton(object):
    #this is the class that is used
    class __ImageGetterSingleton:

        def __init__(self):
            #The images are considered only if they are not in the dataset
            self.__dataframe = pd.read_csv("mergeOrientation.csv")

            #delete the useless rows and columns
            self.__names = self.__dataframe.loc[self.__dataframe["final_conf"]<0.6, "Filename"].tolist()

            self.__indx = 0
            self.current_img = mypath + "\\\\" +self.__names[self.__indx]
            #TODO questa variabile dice se devono essere settate le fonti luminose
            self.__light = None
            self.__light_to_be_Set = True
            self.background_changed = True
            self.__options_light = {  0: "left_pose",
                                1: "center_pose",
                                2: "right_pose"}
            self.names_number = len(self.__names)

        def set_params(self, position):
            if self.__light_to_be_Set:
                #Saves the lights position
                self.__light = self.__options_light[position]
                self.__light_to_be_Set = False
                return self.pop()

        #Moves to the following image.
        def pop(self):
            if self.__light != None:
                #TODO elimina row prima di inserirla
                self.__dataframe.drop(self.__dataframe[ self.__dataframe['Filename'] == self.__names[self.__indx] ].index , inplace=True)
                self.__dataframe.loc[len(self.__dataframe)] = [self.__names[self.__indx],self.__light, 1.0]
                self.__light = None
            self.background_changed = True
            self.__indx -= -1
            if self.__indx == self.names_number:
                self.quit()
                sys.exit()
            print(self.__names[self.__indx])
            self.__light_to_be_Set = True
            print("Set the orientation of this image")
            self.current_img = mypath + "\\\\" + self.__names[self.__indx]
            return self.__names[self.__indx] + "\nSet the orientation of this image"

        def quit(self):
            self.__dataframe.to_csv("mergeOrientation.csv", encoding='utf-8', index=False)

        def __one_hot_encoder(self, position):
            list = [0,0,0]
            if -1 < position < 3:
                list[position] = 1
            else:
                print("errore posizione sbagliata nel one hot encoder")
            return list.copy()


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
