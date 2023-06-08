<a href="https://github.com/rafsaf/minimal-fastapi-postgres-template/blob/main/LICENSE" target="_blank">
    <img src="https://img.shields.io/github/license/rafsaf/minimal-fastapi-postgres-template" alt="License">
</a>
<a href="https://docs.python.org/3/whatsnew/3.11.html" target="_blank">
    <img src="https://img.shields.io/badge/python-3.11-blue" alt="Python">
</a>

# PDF Data Extractor

## About

An application that process uploaded pdf and extract text and store the same in the database for further usage.

## Backend Stack
 - [x] FastAPI (Python)
 - [x] Postgres


## Project Installation Steps

### 1. Clone the repository
### 2. Install dependecies with poetry or without it

```bash
cd project_name
### Poetry install (python3.11)
poetry install

### Optionally there is also `requirements.txt` file
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Note, be sure to use `python3.11` with this template with either poetry or standard venv & pip, if you need to stick to some earlier python version, you should adapt it yourself (remove new versions specific syntax for example `str | int` for python < 3.10 or `tomllib` for python < 3.11)

### 3. Setup Postgres
### 4. Now you can run app

```bash
### And this is it:
uvicorn app.main:app --reload

```

You should then use `git init` to initialize git repository and access OpenAPI spec at http://localhost:8000/ by default. To customize docs url, cors and allowed hosts settings, read section about it.
