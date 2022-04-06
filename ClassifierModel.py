from pyAudioAnalysis import audioTrainTest as aT
import os

dirname = '/home/kmistri/audioClassificationNew/trainingData'

subdirectories = os.listdir(dirname)[:10]
subdirectories = [dirname + "/" + subDirName for subDirName in subdirectories]
# print(subdirectories)
aT.featureAndTrain(subdirectories, 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "newModel", False)

'''
(list of directories,mid window size,mid window steps, short window size, short window step,type, file name to be saved,Frequency)
'''
