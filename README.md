# DEVELOPMENT - GIT
Follow these steps. `main` branch will not allow merging of changes in any other way.
```
git checkout main
git pull
git checkout -b my-feature-branch

// Do your development work

git checkout main
git pull
git checkout my-feature-branch
git rebase main

// Fix all conflicts that are raised
// current changes refer to changes to MAIN
// incoming changes refer to YOUR changes on my-feature-branch

git branch -b // good practice - double check that you're on my-feature-branch
git push -f
```

# DEVELOPMENT - FRONTEND
1. Install dependencies
```
cd frontend
npm install
```
2. Spin up the dev server
```
npm start
```

# DEVELOPMENT - BACKEND
1. Hosted at https://ai-doctor-3409.herokuapp.com/
2. Automatic deployments are set up, so all commits to `main` will trigger a new deployment
3. Install dependencies
```
Linux:
python3 -m venv venv/ // optional if you don't want a venv
source venv/bin/activate // optional if you don't want a venv
pip install -r requirements.txt
```
4. Spin up your Flask application server
```
FLASK_APP=app.py FLASK_ENV=development flask run
```

# DEVELOPMENT - BACKEND - ADDING DEPENDENCIES

ONLY if you're on venv with ONLY libraries in requirements.txt installed
```
pip install XXX
pip freeze > requirements.txt
```

OTHERWISE
```
Manually add the library and its version into requirements.txt
```
