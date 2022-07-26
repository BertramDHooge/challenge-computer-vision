<h2 align="center"> Computer vision challenge </h2>
<p align="center"><a href="https://becode.org/">
<img src="https://becode.org/app/uploads/2021/06/logo-becode.png" alt="Logo" width="200" height="200"></a></p>
<h3 align="center"> Computer vision project at <a href="https://github.com/becodeorg"><strong>BeCode</strong></a></h3>
<h3 align="center"> Contributors: <a href="https://https://github.com/BertramDHooge"> Bertram D'Hooge</a> (Solo Project) </h3><br>

  
## The timeline of the project: 
**16/05/2022 - 24/05/2022*

## Project flow

This was our first computer vision project and it showed. I heavily used 2 Kaggle submissions (https://www.kaggle.com/code/udayasrimandadapu/cnn-sc and https://www.kaggle.com/code/rslu2000/skin-cancer-model-97-88-accuracy) as inspiration for the model building and preprocessing. To avoid issues with predicting new images I have not used any scaling of the values and new images will just be rescaled and have some basic processing done to allow predictions. 

This was the first BeCode project where I really ran into the limitations of my personal computer and had to use Kaggle/Google CoLab, the end results ended up being copied and pasted from my Kaggle workspace and have not been run locally.

Both the building of the Flask app and deployment to Heroku initially went smoothly, but ran into issues with OpenCV, so the current version only runs locally.

## Next steps

I would like to tweak the model more and, even if I don't end up improving upon the current result, hope to play around with the layers more and get more of a feel for the workings of NN's.

I would also like to fix the issues I encountered with OpenCV on Heroku.

## Objectives of the project: 
* Detecting the severity and type of mole from an image.

## Sources (both inspiration and code):
* https://www.kaggle.com/code/udayasrimandadapu/cnn-sc
* https://www.kaggle.com/code/rslu2000/skin-cancer-model-97-88-accuracy

## Usage:
* The project currently does not run on Heroku, but can be run locally using Flask, project requirements can be found in requirements.txt

## Project outline:

* [x] Extracting relevant data from [Mole dataset](https://www.kaggle.com/kmader/skin-cancer-mnist-ham10000)
    * Image
    * Mole Type
* [x] Preprocessing images
* [x] Training a neural network to detect the mole type
* [ ] Deploying the app on Heroku

## Dataset details:
[Dataset](https://www.kaggle.com/kmader/skin-cancer-mnist-ham10000) contains the following columns :

 - [x] considered relevant for this project
 - [ ] not considered relevant for this project

* [ ] lesion_id; 
* [ ] image_id;
* [x] dx;
* [ ] dx_type;
* [ ] age;
* [ ] sex;
* [ ] localization;

Images of the moles were stored in separate folders and could be accessed using the image_id.

Despite not being used in the current version age, sex and localization are still quite relevant datapoints. Currently the algoritm will plainly use the image to attempt to predict what type of mole is being shown.
