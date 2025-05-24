# Django Star Wars CRUD API

This project is a coding challenge to build a Django application that fetches Star Wars planets data from a public GraphQL API, stores it in a local database, and exposes a RESTful CRUD API for planets.

## ⚠️ Note About the Star Wars GraphQL API Endpoint

**Original challenge instructions** referenced the GraphQL endpoint:

https://swapi-graphql.netlify.app/.netlify/functions/index

with the query:
```graphql
query Query {
  allPlanets {
    planets {
      name
      population
      terrains
      climates
    }
  }
}
````

**However, as of the time of this coding challenge, that public endpoint was not reliably available or was frequently down.**

After extensive testing with multiple Star Wars GraphQL APIs, the following endpoint was selected for reliable data fetching:

https://swapi-graphql.eskerda.vercel.app/

The query and data structure remain identical, so the project logic and code are fully aligned with the original requirements.

If the endpoint ever becomes unavailable, you can adapt the data loading script or seed the database via Django admin.

---

## 🚀 Features

- **Fetches Star Wars planets data** from a public GraphQL endpoint
- **Stores planets** (name, population, terrains, climates) in a relational database
- **RESTful CRUD API** for planets using Django REST Framework
- **Easy to extend** or connect with other Star Wars data sources

---

## 🛠️ Technologies Used

- Python 3.11+
- Django 5.x
- Django REST Framework
- Requests (for API fetch)
- SQLite (default, but easily swappable)
- [Public GraphQL API](https://swapi-graphql.eskerda.vercel.app/)

---

## ⚡ Setup Instructions

1. **Clone the repository**
    ```bash
    git clone https://github.com/Hokaid/PIT-solutions-django-challenge.git
    cd PIT-solutions-django-challenge
    ```

2. **Create and activate a virtual environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**
    ```bash
    pip install django djangorestframework requests
    ```

4. **Apply migrations**
    ```bash
    cd starwars_api
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Fetch planets data from the GraphQL API**
    ```bash
    python manage.py fetch_planets
    ```

6. **Run the development server**
    ```bash
    python manage.py runserver
    ```

7. **Open the API**
    - Visit [http://127.0.0.1:8000/api/planets/](http://127.0.0.1:8000/api/planets/) in your browser.

---

## 🛰️ API Endpoints

| Method | Endpoint                     | Description                |
|--------|------------------------------|----------------------------|
| GET    | /api/planets/                | List all planets           |
| POST   | /api/planets/                | Create a new planet        |
| GET    | /api/planets/{id}/           | Retrieve a planet          |
| PUT    | /api/planets/{id}/           | Update a planet            |
| PATCH  | /api/planets/{id}/           | Partial update a planet    |
| DELETE | /api/planets/{id}/           | Delete a planet            |

**Example JSON for POST/PUT:**
```json
{
  "name": "Dagobah",
  "population": 0,
  "terrains": ["swamp", "jungles"],
  "climates": ["murky"]
}
````

---

## 📄 Requirements

* Python 3.11 or later
* Internet connection to fetch the initial data

---

## 💡 Notes

* The public GraphQL API used is [https://swapi-graphql.eskerda.vercel.app/](https://swapi-graphql.eskerda.vercel.app/)
* If the GraphQL endpoint is unavailable, you can seed the DB manually via Django admin or fixture.

---

## 🧑‍💻 Author

Geral Castillo
[LinkedIn](https://www.linkedin.com/in/geralcastillo/)
