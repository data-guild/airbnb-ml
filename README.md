# airbnb-ml

machine learnine on airbnb barcelona listings

Inspired by [clean-code-ml](https://github.com/davified/clean-code-ml)

# Environment setup

### Pre-requisit

```bash
# pyenv installed
curl https://pyenv.run | bash

# install python 3.7.6 in pyenv
pyenv install 3.7.6

# verifiy
pyenv versions
# $ pyenv versions
#     system
#     3.7.6  <- this is what we installed
```

### Setup on local machine

```
pyenv_version=3.7.6
pyenv_name=`cat .python-version`
pyenv virtualenv $pyenv_version $pyenv_name
pyenv activate $pyenv_name
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Running test

```bash
nosetests # single run
nosetests --with-watch --rednose --nologcapture # run in watch mode with color
```

### Package flask app into docker

As the application obtains the model from S3, you should have **AWS_ACCESS_KEY_ID** and **AWS_SECRET_ACCESS_KEY** when running locally

```
docker build -t airbnb_barcelona_ml:latest .
docker run -e AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID> -e AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY> -p 5000:5000 -d airbnb_barcelona_ml
```
