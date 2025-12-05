<<<<<<< HEAD
# PythonProject
# airport-api
# py-airport-api
=======
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
<img width="836" height="667" alt="image" src="https://github.com/user-attachments/assets/252e3ff1-c63d-4bdb-8728-f26b070636ad" />

<img width="850" height="457" alt="image" src="https://github.com/user-attachments/assets/79a2dd17-b189-4604-b6e4-5457cfad3896" >
<img width="850" height="457" alt="image" src="https://github.com/user-attachments/assets/2be9e4b7-1bf0-4b5b-88ce-6b0c111d4e7a" />
<img width="850" height="457" alt="image" src="https://github.com/user-attachments/assets/98da1c73-879c-46fc-be60-b4e626f2e79d" />
<img width="850" height="457" alt="image" src="https://github.com/user-attachments/assets/510c1937-92e8-4500-aabb-e014c57d5f40" />
<img width="850" height="493" alt="image" src="https://github.com/user-attachments/assets/7a7ff0b5-f175-49a9-a5ac-f1151241f102" />
<img width="850" height="457" alt="image" src="https://github.com/user-attachments/assets/8747ee3c-c4d3-4531-8cfe-7291df0dfc0b" />
<img width="850" height="457" alt="image" src="https://github.com/user-attachments/assets/15fe6584-3b02-43d0-9751-e60e0112f9ef" />
<img width="850" height="457" alt="image" src="https://github.com/user-attachments/assets/84b8b6e9-1d1e-405a-9e62-816f93118387" />










      
>>>>>>> ed8e9cfd5f0f2b704a52608c25883e4c6a988709
