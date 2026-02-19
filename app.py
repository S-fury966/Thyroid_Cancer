from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import pickle
import pandas as pd 
from schemas import User

app = FastAPI()

# Local Host allowment
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for local dev; restrict in production, e.g., ["http://localhost:3000"])
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Loading of the Model

with open ("predict/model.pkl",'rb') as f :
    model = pickle.load(f)

# Building the API endpoint

@app.post ("/predict",
    response_model=PredictionResponse,
    summary="Predict disease recurrence",
    description="Returns prediction with confidence score"
)

async def predict(data : User):
    df = pd.DataFrame({
        "Age" : [data.age],
        "Gender" : [data.gender],
        "Smoking" : [data.smoking],
        "Hx Smoking" : [data.hx_smoking],
        "Hx Radiothreapy" : [data.hx_radiotherapy],
        "Thyroid Function" : [data.thyroid_function],
        "Physical Examination" : [data.physical_examination],
        "Adenopathy" : [data.adenopathy],
        "Pathology" : [data.pathology],
        "Focality" : [data.focality],
        "Risk" : [data.risk],
        "Tumor_Stage" : [data.tumor_stage],
        "Regional_Node_Stage" : [data.regional_node_stage],
        "Metastatic_Stage" : [data.metastatic_stage],
        "Stage" : [data.stage],
        "Response" : [data.response]
    })
    
    prediction = model.predict(df)[0]
    
    if (prediction == 0):
        return JSONResponse(status_code=200,content={'prediction':'No Chances of Recursion'})
    
    else :
        return JSONResponse(status_code=200,content={'prediction' :'Chances of Recursion'})      