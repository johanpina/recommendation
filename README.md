# Job Recommendation System

This repository contains the code for a job recommendation system. The system was developed as part of a technical test for an Artificial Intelligence Developer position.

## Description

The recommendation system uses a large language model to generate job recommendations based on user information. Recommendations are generated by comparing the user's information with a database of job postings.

The system is built with Python and FastAPI, and it uses the OpenAI library to work with the large language model (LLM).

## Repository Structure

The repository is organized as follows:

- `main.py`: The entry point for the FastAPI application. It defines the routes for getting recommendations and creating users.
- `schemas.py`: Defines the Pydantic models for user data, job postings, and recommendations.
- `crud.py`: Simulates CRUD operations for the user and job postings databases.
- `large_language_model.py`: Contains the functions for generating recommendations using the large language model.
- `database.py`: Simulates the database connection, structure, and loading.



## Installation

To install the project dependencies, you will need to have Python installed on your machine. You can install the dependencies using pip, the Python package manager. At the root of the repository, run the following command:

```bash
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

## Execution
To run the recommendation system, you need to execute the main.py file. You can do this with the following command:

```bash
python main.py
```

Once the application is running, you can make a **`GET`** request to **`/recommendations/{user_id}`**  to get recommendations for a user, or you can make a **`POST`** request to **`/create/user/`** to create a new user and get recommendations for them.
## System deployment with Azure:

[Hunty recommendation API](https://huntyappreco.azurewebsites.net/docs) 
