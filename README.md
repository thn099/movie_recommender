# Description

A movie recommendation engine using content based filtering.

Movie dataset contains 4800+ movie records. Selected features to calculate similarities are `["keywords", "cast", "genres", "director"]`

Similarity scores are not precomputed.

Project structure:

```
├── flaskapp
│   ├── __init__.py
│   ├── movie_app.py
│   ├── recommender.py
│   ├── static
│   │   └── main.css
│   └── templates
│       └── home.html
├── movie_dataset.csv
├── run.py
```

# Set up

Use `pip install` to get required packages:

`pip install flask numpy pandas scikit-learn`


# Run

```
$ export FLASK_APP=run.py
```

```
$ flask run
```

By default, service will be running on `http://127.0.0.1:5000/`


# Demo

![](demo.gif)
