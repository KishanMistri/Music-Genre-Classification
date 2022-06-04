# Music-Genre-Classification in action
## _Classification based on kernel SVM_

# Description
- Database Used: http://opihi.cs.uvic.ca/sound/genres.tar.gz [1.2GB]
- We are using kernel SVM not 'Linear' because our dataset will not be linearly saperable if we visualize.So Here I am using pyAudioAnanlysis [Reference: https://github.com/tyiannak/pyAudioAnalysis ] library to extract all 34 feature from music file. 
- When our features are extracted in a vector format we will feed these data to SVM model,but as mentioned before it is not possible to saperate linearly.So we are using kernel SVM.
- Features extracted using pyaudioanalysis library.

# Feature Details:

|Feature Name | Description|
| ------------- | ------------- |
|Zero-Crossing Rate|	The rate of sign changes of the signal during the duration of a particular frame.|
|Energy	|The sum of squares of the signal values, normalized by the respective frame length.|
|Entropy of Energy	|The entropy of sub-frames normalized energies. It can be interpreted as a measure of abrupt changes.|
|Spectral Centroid|	The center of gravity of the spectrum.|
|Spectral Spread	|The second central moment of the spectrum.|
|Spectral Entropy	|The entropy of the normalized spectral energies for a set of sub-frames.|
|Spectral Flux|	The squared difference between the normalized magnitudes of the spectra of the two successive frames.|
|Spectral Rolloff|	The frequency below which 90% of the magnitude distribution of the spectrum is concentrated.|
|MFCCs (9-21)	|Mel Frequency Cepstral Coefficients form a cepstral representation where the frequency bands are not linear but distributed according to the mel-scale.|
|Chroma Vector (22-33)|	A 12-element representation of the spectral energy where the bins represent the 12 equal-tempered pitch classes of western-type music (semitone spacing).|
|Chroma Deviation	|The standard deviation of the 12 chroma coefficients.|

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
