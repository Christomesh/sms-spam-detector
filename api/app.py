from fastapi import FastAPI
import joblib

model = joblib.load('models/model.sav')

app = FastAPI(title="Ham or Spam API", description="API to predict if a SMS is ham or spam")

@app.post('/predict', summary="Make a prediction for a new SMS")
def predict(message: str):
    pred =  model.predict([message])[0]
    dict = {"message": message, "prediction": pred}
    return dict