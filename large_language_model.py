import openai
from database import vacancies, loaded_vacancies_embeddings,loaded_vacancies_ids
from crud import get_embedding_from_id
import os
from openai.embeddings_utils import (
    get_embedding,
    distances_from_embeddings,
    indices_of_nearest_neighbors_from_distances,
)

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv()


openai.api_key = os.getenv('OPENAI_API_KEY')

EMBEDDING_MODEL = "text-embedding-ada-002"


def recomendation(One_user_embed,k_nearest_neighbors=5):
    # Search the nearest k neighbors

    distances = distances_from_embeddings(One_user_embed, loaded_vacancies_embeddings, distance_metric="cosine")
    indices_of_nearest_neighbors = indices_of_nearest_neighbors_from_distances(distances)
    k_counter = 0
    recomendations = []
    for i in indices_of_nearest_neighbors:

        # stop after printing out k articles
        if k_counter >= k_nearest_neighbors:
            break
        k_counter += 1

        reco = dict()
        reco["vacancy_id"] = loaded_vacancies_ids[i]
        reco["vacancy_name"] = vacancies.iloc[i]["vacancy_name"]
        reco["vacancy_description"] = vacancies.iloc[i]["description"]
        reco["match"] = f"{(1-distances[i]) * 100:.2f}%"

        recomendations.append(reco)
    return recomendations



def calculate_recommendation(user_id,k:int=5):
    list_recomendations = None
    user_embedd = get_embedding_from_id(user_id)
    
    if user_embedd:
        # we are going to search the k recommendations
        list_recomendations = recomendation(user_embedd,k_nearest_neighbors=k)

    return list_recomendations
