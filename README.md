# Music-Genre-Classification
Classification base on kernel SVM

Here we are using kernel SVM not 'Linear' because our dataset will not be linearly saperable if we visualize.So Here I am using pyAudioAnanlysis [Reference: https://github.com/tyiannak/pyAudioAnalysis ] library to extract all 34 feature from music file. Here I have used '*.wav' but we have function in this library which can be used to convert all type of extension to .wav format. 

So when our features are extracted in a vector format we will feed these data to SVM model,but as mentioned before it is not possible to saperate linearly.So we are using kernel SVM.

Some information about kernel SVM:
  Kernel SVM use different type of function which transform data into new dimension where data is linearly saperable.
  Here is good reference: http://crsouza.com/2010/03/17/kernel-functions-for-machine-learning-applications/
  
