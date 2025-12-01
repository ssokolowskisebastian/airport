Docker (PostgreSQL)
# start (build images and run containers)
docker compose up --build
# stop
docker compose down



Setup (local, SQLite)
python -m venv .venv
. .venv/Scripts/activate  # Windows PowerShell
source .venv/bin/activate  # macOS/Linux

pip install --upgrade pip
pip install -r requirements.txt

cp .env.example .env
# By default SQLite will be used (no extra steps needed)

python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata fixtures/seed.json
python manage.py runserver
