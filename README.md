# Music-Genre-Classification in action
## _Classification based on kernel SVM_

# Description
- Database Used: http://opihi.cs.uvic.ca/sound/genres.tar.gz [1.2GB]
- We are using kernel SVM not 'Linear' because our dataset will not be linearly saperable if we visualize.So Here I am using pyAudioAnanlysis [Reference: https://github.com/tyiannak/pyAudioAnalysis ] library to extract all 34 feature from music file. 
- When our features are extracted in a vector format we will feed these data to SVM model,but as mentioned before it is not possible to saperate linearly.So we are using kernel SVM.

# Some information about kernel SVM:
- Kernel SVM use different type of function which transform data into new dimension where data is linearly saperable.
  - Here is good reference: http://crsouza.com/2010/03/17/kernel-functions-for-machine-learning-applications/
- I have utilized '.wav' format but we can be used to convert all type of extension to .wav format. 
  
So after training our SVM classifier we will test on any file.
- I have selected 'isSignificant' level which is minimum probability to classify our test file.[In my code : 0.6]

> Note: This is a utilisation of library to perform classification to get understanding of Kernel SVM.
