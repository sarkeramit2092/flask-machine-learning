# IPL Flask App with SQLAlchemy

The Python script is a basic **Flask web application** integrated with **SQLAlchemy**, an Object-Relational Mapper (ORM), for interacting with a SQLite database named `ipl.db`. Here's a breakdown of what each part does:

---

## ✅ Flask & SQLAlchemy Setup

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
```

* **Flask**: A lightweight web framework used to create web applications.
* **SQLAlchemy**: A Python ORM for working with databases in an object-oriented way.

```python
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ipl.db"
```

* Initializes the Flask app.
* Configures SQLAlchemy to use **SQLite** as the database with a file named `ipl.db`.

```python
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
```

* Disables a feature that unnecessarily tracks changes to objects, preventing warnings and saving system resources.

```python
db = SQLAlchemy(app)
```

* Binds the SQLAlchemy object to the Flask app so you can define models and interact with the database.

---

## ✅ Database Models (ORM)

### Team Model

```python
class Team(db.Model):
    __tablename__ = "teams"
```

* Declares a table named `teams` in the database.

```python
    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(50), nullable=False, unique=True)
    state = db.Column(db.String(50), nullable=False)
```

* Defines columns:

  * `id`: Primary key (unique identifier for each team).
  * `team`: Team name (must be unique and not null).
  * `state`: The state the team belongs to.

```python
    members = db.relationship("Player", backref="team")
```

* Establishes a **one-to-many relationship**: One team can have many players.
* `backref="team"` allows accessing the team from a player object using `.team`.

```python
    def __repr__(self):
        return f"Team('{self.team}', '{self.state}')"
```

* String representation for debugging/logging.

### Player Model

```python
class Player(db.Model):
    __tablename__ = "players"
```

* Declares a table named `players`.

```python
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    nationality = db.Column(db.String(50), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"))
```

* Defines columns:

  * `id`: Primary key.
  * `name`: Player name (required).
  * `nationality`: Player nationality (required).
  * `team_id`: Foreign key linking the player to a team in the `teams` table.

```python
    def __repr__(self):
        return f"Player('{self.name}', '{self.nationality}')"
```

* String representation for debugging/logging.

---

## ✅ Running the App

```python
if __name__ == "__main__":
    app.run(debug=True)
```

* Runs the Flask app in **debug mode**, which helps during development by reloading the server automatically on code changes and showing detailed error messages.

---

## 🧠 Summary

This script:

* Defines a simple schema for an IPL system with teams and players.
* Uses Flask for the web framework and SQLAlchemy for database handling.
* Sets up a one-to-many relationship: one team has many players.
* Can be extended to support routes (e.g., `@app.route(...)`) for web API functionality.
