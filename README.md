# vkhwing
For the Wing.

Here people can upload photos & videos and chat. 


# To Run
1. `virtualenv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`	
4. `python manage.py makemigrations`
5. `python manage.py migrate`
6. `python populate_vkhwing.py`
7. `python manage.py createsuperuser`
8. `python manage.py runserver`
9. Head over to 127.0.0.1:8000 or localhost:8000
