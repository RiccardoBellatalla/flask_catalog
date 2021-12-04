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

1. install VENV : python3 -m venv nome_virtual_venv
2. activate VENV : source nome_virtual_venv/bin/activate
3. instal Flask in VENV : pip3 install flask
4. save requirements : pip3 freeze > requirements.txt
5. install requirements : pip3 istall -r requirements.txt #questo lo uso quando devo fare deploy del progetto e voglio i requirements installati
6. create application : create application.py file
7. set environment variable : export FLASK_APP='application.py'
8. run flask application : flask run
9. initialize git repo : git init
