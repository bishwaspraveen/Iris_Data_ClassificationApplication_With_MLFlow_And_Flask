## Iris Data Classification Application With MLFlow And Flask

### Step 1 : Adding an experiment from research environment to MLflow for experiment tracking.
![result1](https://user-images.githubusercontent.com/79660080/220559345-796ddc01-1b3b-430d-a42f-940f80b9e07c.PNG)

### Step 2 : Registering the model which produces the best results and staging it into production using sqlite on the backend for information storage on MLflow.
![result2](https://user-images.githubusercontent.com/79660080/220559441-55098441-a32f-4983-b5b8-cf13937f1e17.PNG)

### Step 3 : Using the MLflow endpoint for inference and creating a Flask application around it. The image shows the entry point of the application (Served at : `http://127.0.0.1:5000`).
![result3](https://user-images.githubusercontent.com/79660080/220559510-0024c78e-88ab-40bf-9306-839f73f3a0a3.PNG)

### Step 4 : The interface of the application to evaluate the input data features, one sample at a time.
![result4](https://user-images.githubusercontent.com/79660080/220559576-e8c39dac-7b69-475a-bc45-35a3a9712324.PNG)

### Step 5 : The result obtained for the input features in single sample mode through an AJAX request to the model serving on MLFlow in the backend.
![result5](https://user-images.githubusercontent.com/79660080/220559690-9fbd0f4f-e94c-44bd-964e-e8890d14ba41.PNG)

### Step 6 : The interface of the application to evaluate the input data features in batch mode.
![result6](https://user-images.githubusercontent.com/79660080/220559752-be83221d-04ea-4531-9ff1-cff61e7b36aa.PNG)

### Step 7 : The result obtained for the input features in batch processing (.csv file) mode through an AJAX request to the model serving on MLFlow in the backend.
![result7](https://user-images.githubusercontent.com/79660080/220559836-fad7cf97-9589-43d7-8aad-2fea40f0f7cb.PNG)

### Important notes : 

It is necssary to run four anaconda prompts simultaneously for the whole application to run smoothly.

#### First anaconda prompt : Runs the jupyter notebook in reserach environment.

Serves at : `http://localhost:8888`

#### Second anaconda prompt : Runs the MLflow UI which generates an interface for tracking, registering and productionizing the machine learning model of interest.

Serves at : `http://127.0.0.1:8000`

Command to start the MLflow UI : `C:\Users\bishw\OneDrive\Desktop\Source_codes\Regression-MLFlow-Flask-Application>mlflow server --backend-store-uri sqlite:///C:\Users\bishw\OneDrive\Desktop\Source_codes\Regression-MLFlow-Flask-Application\mlflow.db --default-artifact-root file:///C:\Users\bishw\OneDrive\Desktop\Source_codes\Regression-MLFlow-Flask-Application\artifacts --port 8000`

#### Third anaconda prompt : Running the MLflow server to generate the endpoints for the model in production during inference.

Serves at : `http://127.0.0.1:1234`

Command to start the MLflow server : `mlflow models serve --model-uri models:/iris-classifier/Production -p 1234 --no-conda`

#### Fourth anaconda prompt : Runs the Flask application with various endpoints used to facilitate the users to use the application instead of the the MLflow server endpoint directly.

Serves at : `127.0.0.1:5000`

Command to start the application (It is necessary to first navigate into the directory which has main.py and then run the command) : `python app.py`
