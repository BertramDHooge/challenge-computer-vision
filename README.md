# Model deployment challenge 
## using Docker and Heroku

This is an application deployed to Heroku to predict mole types using a kaggle dataset provided to us (https://www.kaggle.com/kmader/skin-cancer-mnist-ham10000).

The application allows you to insert an image and will give you it'sprediction for which type of mole it is.

# Install

The required packages are stored in requirements.txt so if you want to run the app straight through Flask, this can be done with:
    
`pip install requirements.txt`
   
Alternatively you can access the Heroku app on https://whatmoleisthat.herokuapp.com/
    
Or you could run the app through Docker using the provided Dockerfile, whatever suits your fancy.

# The Project

This was our first computer vision project and it showed. I heavily used 2 Kaggle submissions (https://www.kaggle.com/code/udayasrimandadapu/cnn-sc and https://www.kaggle.com/code/rslu2000/skin-cancer-model-97-88-accuracy) as inspiration for the model building and preprocessing. To avoid issues with predicting new images I have not used any scaling of the values and new images will just be rescaled and have some basic processing done to allow predictions. 

Both the building of the Flask app and deployment to Heroku went very smoothly, and though I am not happy at all with the final appearance, I am not any good at making frontends, so this will have to do for now.

I would like to tweak the model more and, even if I don't end up improving upon the current result, hope to play around with the layers more and get more of a feel for the workings of NN's.
