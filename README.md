# Django CRUD API  

A Django-based REST API with CRUD operations and JSON data import functionality.  

## Features  

- Import JSON data into the database using a custom Django management command  
- CRUD operations using Django REST Framework (APIView)  
- Pagination for large datasets  
- Modular project structure following Django best practices  

## Installation  

### Clone the Repository  

- git clone https://github.com/<your-username>/<repo-name>.git  
- cd <repo-name>  

### Create and Activate Virtual Environment
- python3 -m venv venv  
- source venv/bin/activate

### Install Dependencies
- pip install -r requirements.txt  

### Apply Migrations
- python manage.py migrate  

### Run the Server
- python manage.py runserver  

### Import JSON Data
python manage.py initial-setup <json_file_path>  


## API Endpoints
- GET	/api/userdata/	Retrieve all user data with pagination
- POST	/api/userdata/	Create a new user record
- GET	/api/userdata/<id>/	Retrieve a specific user record
- PUT	/api/userdata/<id>/	Update an existing user record
- DELETE	/api/userdata/<id>/	Delete a user record
