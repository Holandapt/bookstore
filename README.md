# Bookstore

Bookstore APP from Backend Python course from EBAC

## Prerequisites

* Python 3.11+
* Poetry
* Docker && docker-compose

## Quickstart

1. Clone this project:
   ```bash
   git clone git@github.com:Holandaptr/bookstore.git
   ```

2. Install dependencies:
   ```bash
   cd bookstore
   poetry install
   ```

3. Run local dev server:
   ```bash
   poetry run python manage.py migrate
   poetry run python manage.py runserver
   ```

4. Run docker dev server environment:
   ```bash
   docker-compose up -d --build 
   docker-compose exec web python manage.py migrate
   ```

5. Run tests inside of docker:
   ```bash
   docker-compose exec web python manage.py test
   ```

## Continuous Deployment (PythonAnywhere)

The application is deployed on PythonAnywhere with automatic updates via GitHub Webhooks.

* **Webhook Endpoint:** `https://holandaptr.pythonanywhere.com/update_server/`
* **Server Path:** `/home/Holandaptr/bookstore`

### Manual Pull on PythonAnywhere

If needed, trigger a manual pull from the PythonAnywhere Bash console:
```bash
cd ~/bookstore
git pull
```
*(Remember to click **Reload** in the PythonAnywhere Web tab after pushing or pulling changes).*