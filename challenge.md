<img width="940" alt="image" src="https://github.com/aquaristar/backend-challenge/assets/681512/a2e29d1d-ed62-41ee-8a01-a8666f90316c"># Michael's Result for AAK Testing Project

Thank you for your checking my testing project in the Backend Developer position at AAK Tele-Science. This coding challenge is designed to assess your skills in developing a Django and Django Rest Framework (DRF) backend. Please follow the instructions below to install this project.

## Project Description

You are tasked with building a backend for a simple task management system. The application should include at least `Task` and `Label` models, and you need to expose API endpoints for CRUD operations on these models.

## How to deploy and test

1.  Clone project using HTTPS or SSH.

    - HTTPS:
      `git clone https://github.com/aquaristar/backend-challenge.git`
      
    - SSH:(to use SSH set your email in local project config file)
      `git clone git@github.com:aquaristar/backend-challenge.git`

2. Install python virtual environment.
   ```
   cd backend-challenge
   python3 -m pip install --upgrade pip
   python3 -m pip install virtualenv
   python3 -m virtualenv venv
   . venv\Scripts\activate
   python -m pip install -r requirements.txt
   ```

3. Migrate db and create super-user and staff-user for testing.
   ```
   cd ./MikeTest
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ...   
   python manage.py runserver   
   ```
   After the server is started up please open your web browser and login with the super-user in admin page `http://localhost:8000`.
   And then add another new User with `staff` privillege like following.
   <img width="897" alt="image" src="https://github.com/aquaristar/backend-challenge/assets/681512/ffa4a7db-4007-4b7b-bb51-38d4bb554f48">
   
4. Test api endpoints using web browser or Postman:
   Open your web browser and login with credentionals what you've just created.
<img width="892" alt="image" src="https://github.com/aquaristar/backend-challenge/assets/681512/9aef4cd8-6209-47aa-a7d7-e8395445f3b9">
<img width="616" alt="image" src="https://github.com/aquaristar/backend-challenge/assets/681512/3a642b6b-b014-43c1-ba0f-2556d8c71d64">

   - testing of tasks endpoint :  `http://localhost:8000/api/v1/tasks/`
     <img width="896" alt="image" src="https://github.com/aquaristar/backend-challenge/assets/681512/b023f1a3-0901-4d19-b320-f5a9d5848dc2">

   - testing of labels endpoint :  `http://localhost:8000/api/v1/labels/`
     <img width="922" alt="image" src="https://github.com/aquaristar/backend-challenge/assets/681512/1ee69341-c2ec-4eae-ab73-f885f96e3ba0">

   - testing of tasks filter
     <img width="974" alt="image" src="https://github.com/aquaristar/backend-challenge/assets/681512/bf4c6bd8-351e-45ab-a36e-368e1de3c925">

   - testing of labels filter
     <img width="946" alt="image" src="https://github.com/aquaristar/backend-challenge/assets/681512/a4758d23-852c-4517-9d78-1bbb6d015c17">

   If you test the api endpoints using Postman please refer following screen.
   <img width="959" alt="image" src="https://github.com/aquaristar/backend-challenge/assets/681512/b6424f99-d6bf-46f1-a212-2c0db669d1bd">

