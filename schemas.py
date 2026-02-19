from pydantic import BaseModel,Field
from typing import Annotated,Literal

class User(BaseModel):
    age : Annotated[int,Field(...,ge=1,le=120,description="Enter your age in years")]
   
    gender : Annotated[Literal["Male","Female"],Field(...,description="Choose from options")]
   
    smoking : Annotated[Literal["Yes","No"],Field(...,description="Choose from options")]
   
    hx_smoking : Annotated[Literal["Yes","No"],Field(...,description="Choose from options")]
   
    hx_radiotherapy : Annotated[Literal["Yes","No"],Field(...,description="Choose from options")]
   
    thyroid_function : Annotated[Literal["Euthyroid","Clinical Hyperthyroidism","Subclinical Hypothyroidism","Clinical Hypothyroidism","Subclinical Hyperthyroidism"],Field(...,description="Choose from options")]
   
    physical_examination : Annotated[Literal["Multinodular goiter","Single nodular goiter-right","Single nodular goiter-left","Normal","Diffuse goiter"],Field(...,description="Choose from options")]
   
    adenopathy : Annotated[Literal["No","Right","Bilateral","Left","Extensive","Posterior"],Field(...,description="Choose from options")]
   
    pathology : Annotated[Literal["Papillary","Micropapillary","Follicular","Hurthel cell"],Field(...,description="Choose from options")]
   
    focality : Annotated[Literal["Uni-Focal","Multi-Focal"],Field(...,description="Choose from options")]
   
    risk : Annotated[Literal["Low","Intermediate","High"],Field(...,description="Choose from options")]
   
    tumor_stage : Annotated[Literal["T2","T3a","T1a","T1b","T4a","T3b","T4b"],Field(...,description="Choose from options")]
   
    regional_node_stage : Annotated[Literal["N0","N1b","N1a"],Field(...,description="Choose from options")]
   
    metastatic_stage : Annotated[Literal["M0","M1"],Field(...,description="Choose from options")]
   
    stage : Annotated[Literal["I","II","IVB","III","IVA"],Field(...,description="Choose from options")]
   
    response : Annotated[Literal["Excellent","Structural Incomplete","Intermediate","Biochemical Incomplete"],Field(...,description="Choose from options")]