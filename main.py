from fastapi import FastAPI, HTTPException
from schemas import User, Recommendation, Vacancy
from crud import get_user_id, add_user
from large_language_model import calculate_recommendation
import pandas as pd
app = FastAPI() 

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/recommendations/{user_id}")
async def get_recommendation(user_id: int):
    #First, we need to check if the user exists in the database
    user_id = get_user_id(user_id)
    if user_id is None:
        raise HTTPException(status_code=404, detail="User not found")
    

    #We need to calculate the recommendation

    recomendations = calculate_recommendation(user_id,k=5)
    if not recomendations:
        raise HTTPException(status_code=404, detail="Recommendations failed")

    return recomendations


@app.post("/create/user/")
async def create_user(user_info: User):
    user_info = dict(user_info)
    
    user_id = add_user(user_info)

    recomendations = calculate_recommendation(user_id,k=5)
    if not recomendations:
        raise HTTPException(status_code=404, detail="Recommendations failed")

    return recomendations



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)