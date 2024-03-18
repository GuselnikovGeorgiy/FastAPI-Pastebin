How to run:
1. Create a postgres server, set name, user, password, host, port
2. put in .env your preferences, choose secret key and algorithm
3. install or update python 3.12 version
4. create virtual enviroment for python
   ```
   python -m venv venv
   #  and activate it
   .\venv\Scripts\activate
   ```
5. install package poetry in venv
   ```
   pip install poetry
   poetry lock          # to resolve dependencies
   poetry install       # to install all packages from lock file
   ```
6. initialize alembic and run first migration
   ```
   alembic init
   alembic revision --autogenerate -m "Initial migration"
   alembic upgrade head
   ```
7. start app with uvicorn (or poetry)
   ```
   poetry run uvicorn app.main:app --reload
   # or
   uvicorn app.main:app --reload
   ```
   you can also set host and port. For example:
   ```
   poetry run uvicorn app.main:app --reload --host 127.0.0.1 --port 8081
   ```
