# lets simulate a crud file, this file is goingo to contain 
# the functions to search user by id, search vacancies by id and save embeddings
from database import users, vacancies, loaded_vacancies_embeddings, loaded_user_embeddings  
import openai
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv(filename='.envv'))


openai.api_key = os.getenv('OPENAI_API_KEY')
EMBEDDING_MODEL = "text-embedding-ada-002"
from openai.embeddings_utils import get_embedding
import pandas as pd

# Verify if the user exists in the databases
def get_user_id(user_id:int):

    return user_id if user_id in users['id_user'].tolist() else None


def get_embedding_from_id(id_user:int):
    #print(loaded_user_embeddings.keys())
    if id_user in loaded_user_embeddings.keys():
        
        return loaded_user_embeddings[id_user]
    else:
        return None
    

def add_user(user_info:dict):
    pd_user_info = pd.DataFrame(user_info,index=[0])
    pd_user_info= pd_user_info[["area","language","country","work_modality","hardskills"]]
    pd_user_info['combined'] = pd_user_info.apply(lambda row: '; '.join([f'{key}: {value}' for key, value in row.items()]), axis=1)
    
    get_new_embed = get_embedding(pd_user_info['combined'][0], engine=EMBEDDING_MODEL)
    
    loaded_user_embeddings[user_info['id_user']] = get_new_embed
    
    users1 = pd.concat([users, pd_user_info])
    users1.reset_index(drop=True, inplace=True)
    return user_info['id_user']


