Docker (PostgreSQL)
# start
docker compose up --build
# stop
docker compose down



Setup (local, SQLite)
#
python -m venv .venv

. .venv/Scripts/activate  # Windows PowerShell

source .venv/bin/activate  # macOS/Linux

pip install --upgrade pip

pip install -r requirements.txt

cp .env.example .env

python manage.py migrate  

python manage.py createsuperuser

python manage.py loaddata fixtures/seed.json

python manage.py runserver


Here are some screenshots of the application:
<img width="1250" height="857" alt="image" src="https://github.com/user-attachments/assets/79a2dd17-b189-4604-b6e4-5457cfad3896" >
<img width="1250" height="857" alt="image" src="https://github.com/user-attachments/assets/2be9e4b7-1bf0-4b5b-88ce-6b0c111d4e7a" />
<img width="1250" height="857" alt="image" src="https://github.com/user-attachments/assets/98da1c73-879c-46fc-be60-b4e626f2e79d" />





      
