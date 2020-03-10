# airbnb-ml

machine learnine on airbnb barcelona data

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

### Setup

```
pyenv_version=3.7.6
pyenv_name=`cat .python-version`
pyenv virtualenv $pyenv_version $pyenv_name
pyenv activate $pyenv_name
pip install -r requirements.txt
```

### Running stuff

```bash
jupyter notebook # start jupyter kernal

nosetests # single run
nosetests --with-watch --rednose --nologcapture # run in watch mode with color
```
