git clone git@github.com:zhihao404/django-diary.git
cd django-diary
 cd djangotutorial 
cd mydiaryproject
——————————————————————
仮想環境の起動
python3 -m venv .djangoenv
source .djangoenv/bin/activate
pip install django==3.1.2
pip install django-allauth
python3 manage.py runserver
http://127.0.0.1:8000/account/login/ にアクセス
