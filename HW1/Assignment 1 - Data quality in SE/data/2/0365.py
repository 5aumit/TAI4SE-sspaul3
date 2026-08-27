from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from joblib import load

app = FastAPI()
clf = load("model.joblib")

class PredictionRequest(BaseModel):
    feature_vector: List[float]
    score: Optional[bool] = False

@app.post("/prediction")
def predict(req: PredictionRequest):
    prediction = clf.predict([req.feature_vector])
    response = {"is_inlier": int(prediction[0])}
    score = clf.score_samples([req.feature_vector])
    response["anomaly_score"] = score[0]

    return response

@app.get("/model_infomation")
def model_infomation():
    return clf.get_params()

if __name__ == "__main__":
    print("Running")
    