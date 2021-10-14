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
The next step is to configure the `.env` file. You have to enter the generated `SECRET_KEY` value and define with the `DEBUG` variable if the debugging mode is to be enabled. You should also configure the URL that will be the link to the database you created earlier. This can be done by setting the `DATABASE_URL` value. The remaining variables - `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_USE_TLS`, `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` are related to the configuration of sending emails. Remember that the `EMAIL_HOST_PASSWORD` is the password for the created and configured application available when two-step verification is enabled, not the password for your Google account.

An example of the `.env` file contents is shown below:
```shell
SECRET_KEY={generated_secret_key}
DEBUG=False
DATABASE_URL=postgres://{user}:{password}@{hostname}:{port}/{database_name}
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=example@gmail.com
EMAIL_HOST_PASSWORD=password
```
Before running the application migrate the data using the following commands:
```shell
python3 manage.py makemigrations
python3 manage.py migrate
```
To start the application use the following command:
```shell
python3 manage.py runserver
```

## Live demo
Heroku deployment: https://application-to-do-list.herokuapp.com
