# Steps followed for setiing up postgresql

first, installed brew for package managing on mac, which was used to install postgresql.
- `brew install postgresql` to install postgres to the machine
- `brew services start postgresql` to start postgresql server
- validate the installation via `psql --version` psql shell can be started via `psql` command

# setting up the models, and initializing sqlalchemy for usage with project

- add new dependencies via poetry `poetry add alembic` and `poetry add python-dotenv` to add missing dependencies required for database setup
- `poetry run alembic init alembic` command to initialize alembic in the project 