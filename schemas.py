from pydantic import BaseModel
from typing import List

class User(BaseModel):
    id_user: int
    country: str
    area: str
    subareas: str
    degrees: str
    wage_aspiration: float
    currency:   str
    current_wage: float
    change_cities: bool
    language: str
    years_experience: int
    months_experience: int
    wish_role_name: str
    work_modality : str
    hardskills: str

class Vacancy(BaseModel):
    id: int
    name: str
    description: str

class Recommendation(BaseModel):
    user_id: int
    vacancies: List[Vacancy]


