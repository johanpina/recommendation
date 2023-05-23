## This file is going to simulate the database connection, structure and loadings

import pandas as pd
import pickle

users = pd.read_excel("data/Data Set Users.xlsx")
## Users dataset preprocessing
users.fillna('', inplace=True) # replace NaN with empty string

vacancies = pd.read_excel("data/vacantes.xlsx")

## load cached embeddings

# load vacancies embeddings from disk (if they exist)
embedding_cache_path_vacancy1 = "data/vacancies_embeddings_cache_1.pkl"
embedding_cache_path_vacancy2 = "data/vacancies_embeddings_cache_2.pkl"

# load the vacancy's cache if it exists, and save a copy to disk
try:
    embedded_vacancies= pd.read_pickle(embedding_cache_path_vacancy1)
except FileNotFoundError:
    embedded_vacancies= {}

try:
    embedded_vacancies2= pd.read_pickle(embedding_cache_path_vacancy2)
except FileNotFoundError:
    embedded_vacancies2= {}


with open(embedding_cache_path_vacancy1, "wb") as embedding_cache_file:
    pickle.dump(embedded_vacancies, embedding_cache_file)

with open(embedding_cache_path_vacancy2, "wb") as embedding_cache_file:
    pickle.dump(embedded_vacancies2, embedding_cache_file)

loaded_vacancies_ids1, loaded_vacancies_embeddings1 = zip(*embedded_vacancies)
loaded_vacancies_ids2, loaded_vacancies_embeddings2 = zip(*embedded_vacancies2)


loaded_vacancies_ids = list(loaded_vacancies_ids1 + loaded_vacancies_ids2)
loaded_vacancies_embeddings = list(loaded_vacancies_embeddings1 + loaded_vacancies_embeddings2)

# load vacancies embeddings from disk (if they exist)
embedding_cache_path_users = "data/users_embeddings_cache.pkl"

# load the vacancy's cache if it exists, and save a copy to disk
try:
    embedded_users= pd.read_pickle(embedding_cache_path_users)
except FileNotFoundError:
    embedded_users= {}

with open(embedding_cache_path_users, "wb") as embedding_cache_file:
    pickle.dump(embedded_users, embedding_cache_file)

loaded_user_embeddings = dict(embedded_users)