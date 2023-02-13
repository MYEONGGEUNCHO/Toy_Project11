# Toy_Project11

The basic blog app built in the Flask tutorial.  


```
/Toy_Project11/
src
│ ├── app/
│ │   ├── __init__.py
│ │   ├── db.py
│ │   ├── schema.sql
│ │   ├── auth.py
│ │   ├── blog.py
│ │   ├── templates/
│ │   │   ├── base.html
│ │   │   ├── auth/
│ │   │   │   ├── login.html
│ │   │   │   └── register.html
│ │   │   └── blog/
│ │   │       ├── create.html
│ │   │       ├── index.html
│ │   │       └── update.html
│ │   └── static/
│ │       └── style.css
│ ├── tests/
│ │   ├── conftest.py
│ │   ├── data.sql
│ │   ├── test_factory.py
│ │   ├── test_db.py
│ │   ├── test_auth.py
│ │   └── test_blog.py
│ ├── venv/
│ ├── setup.py
│ └── MANIFEST.in
├── README.md
└── requirementes.txt
```


# App

The basic blog app built in the Flask tutorial.  
  
  
# Install
Clone the repository
```
git clone https://github.com/MYEONGGEUNCHO/Toy_Project11.git
cd Toy_Project11
```

Create a anaconda virtual environment:
```
conda create -n name python=3.9 -y
conda activate name
```

Install requirements.txt:
```
pip install -r requirements.txt
```

# Run
```
cd src
flask --app app init-db
flask --app app --debug run
```

# Test
```
cd src/app/tests
pytest
```