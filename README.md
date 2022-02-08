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

# Screens
- Base-view

![Base-View](https://user-images.githubusercontent.com/20341930/153004011-5f1ec146-0984-4517-9be0-1e8fd0f74bb3.png)

- Upload file format enforcing

![Upload-filtering-to-wav](https://user-images.githubusercontent.com/20341930/153004040-e91575c5-d199-4170-83ff-dcfebcaecc1f.png)

- Prediction of uploaded file
 
![Test-Prediction-screen](https://user-images.githubusercontent.com/20341930/153004058-c00e28f5-f3f2-4f2e-84b8-551a43e72b43.png)

- Output when it fails to predict based on significance set

![Failed-to-classify](https://user-images.githubusercontent.com/20341930/153004078-deea8ca6-f2a9-43c8-982b-87f1f1d13ad5.png)


> Note: This is a utilisation of library to perform classification to get understanding of Kernel SVM.
