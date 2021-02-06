# PHOTO ALBUM (DJANGO)
A full-stack web application for storing photos to AWS S3 Bucket.

## SOFTWARE TECHNOLOGIES 

- Django
- Bootstrap 5
- AWS S3 Backets

## GETTING STARTED

### Clone The Project

`git clone https://github.com/placiderapson/photo-album-with-django`

#### Create and Activate Virtual Environment

`virtualenv env && source env/bin/activate`

#### Install Dependencies

`pip3 install -r requirements.txt`

#### Apply Migrations

`python3 manage.py makemigrations && python3 manage.py migrate`

#### Create Super User

`python3 manage.py createsuperuser`

#### Provide AWS Credentials

`Register for an AWS account and create S3 Bucket and assign a user with corresponding credentials.`
`Rename the .env.example file to .env and provide the AWS User Credentials`

#### Start the Server

`python3 manage.py runserver && navigato to http://localhost:8000 for project && http://localhost:8000/admin for the dashboard`
`Add some photos and categories`
