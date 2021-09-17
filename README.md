# To-do list
## Introduction
An application that is an implementation of a to-do list built using Django.

## Setup
First download the project folder or clone the repository using the following command:
```shell
git clone https://github.com/wieczorek-daniel/to-do-list.git
```
Then create and run the virtual environment. Depending on your operating system the commands may vary.

### Linux and OS X
```shell
python3 -m venv venv
. venv/bin/activate
```

### Windows
```shell
python -m venv venv
venv\Scripts\activate
```

Later install the dependencies (required packages) using the following command:
```shell
pip install -r requirements.txt
```
In the project directory also create an .env file containing environment variables based on the .env.example file.
```shell
cp .env.example .env # for Linux
copy .env.example .env # for Windows
```
To start the application use the following command:
```shell
python3 manage.py runserver
```
