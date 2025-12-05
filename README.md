#Setup – Docker (PostgreSQL)

docker compose up --build

#Setup – Local (SQLite)

python -m venv .venv

source .venv/bin/activate     # Linux/macOS

. .venv/Scripts/activate      # Windows PowerShell

pip install -r requirements.txt

cp .env.example .env

python manage.py migrate

python manage.py createsuperuser

python manage.py loaddata fixtures/seed.json

python manage.py runserver

<img width="836" height="567" alt="schema" src="https://github.com/user-attachments/assets/7ed36d22-67ef-4b9c-8205-9bcdba5ff1d4" />
<img width="850" height="557" alt="airplane_type" src="https://github.com/user-attachments/assets/3007173c-e14a-4ef1-b638-66345d9a9bdd" />
<img width="850" height="557" alt="airports" src="https://github.com/user-attachments/assets/c5109a9b-a286-42d9-b5d3-da42f8a896f3" />
<img width="850" height="557" alt="crew:id" src="https://github.com/user-attachments/assets/91f97e9e-57a3-4dd7-a6b0-6e60328e2b9c" />
<img width="850" height="557" alt="crews" src="https://github.com/user-attachments/assets/10219804-8ea7-4110-ac0c-b7513c9d4524" />
<img width="850" height="593" alt="flight_list" src="https://github.com/user-attachments/assets/8c014abe-e7e1-4f86-a0cd-d7a9ef963602" />
<img width="850" height="557" alt="routes" src="https://github.com/user-attachments/assets/e5241663-fe99-4407-b671-5d277614cd69" />

<img width="850" height="457" alt="orders" src="https://github.com/user-attachments/assets/49fd3e1e-c02e-43e1-9ecc-fdf7d4e1df77" />

<img width="850" height="457" alt="image" src="https://github.com/user-attachments/assets/6acdeb2c-c67c-487b-b590-915a5c6c85d4" />
