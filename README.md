# Projet Intégration continue - Création de groupes d’utilisateurs

Votre équipe de développement a reçu une nouvelle commande de la part d’un client souhaitant
développer une application Web pour permettre à ses utilisateurs de créer des groupes de travail.

## Install

Create a virtualenv and activate it:

```bash
$ python3 -m venv env
$ source env/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all depen.

```bash
$ pip install -r requirements.txt
```

## Run

### initialize the database (create a migration repository)

```bash
$ flask db init
```

### migrate the database changes

```bash
$ flask db migrate
```

### apply the migrations

```bash
$ flask db upgrade
```

### run the application

```bash
$ python manage.py run
```

Open http://127.0.0.1:5000 in a browser.

## Test

```bash
$ python manage.py test
```

## Create Admin

```bash
$ python manage.py create_admin
```

## Generate fake users for testing

```bash
$ python manage.py generate_fake
```

#### Author
- Fidel
- Yassamine