Django rest_framework API project for ATS candidates  
This project is dockerized with docker-compose.yml.  
For db we have used postgresql docker image mounted in the docker-compose settings.  
To start the project-  
>first time - docker-compose up -d --build  
>later - docker-compose up -d  
>for logs - docker-compose logs -f (ctrl + c to exit)  
>docker-compose down (docker-compose down -v to unmount the volume)    
>docker-compose exec web_ats pipenv install package_name  
>docker-compose exec web_ats python manage.py shell  

It consists of ats_project and candidates as app
Api end points available for candidates are given below-
1. GET - localhost:8000/candidates
2. GET - localhost:8000/candidates/int_number
3. GET - localhost:8000/candidates/create/
4. PUT - localhost:8000/candidates/update/int_number with body consists of all fields with updated values
5. DELETE - localhost:8000/candidates/delete/int_number
6. GET - localhost:8000/candidates/search/ with params q value search
All the end points were tested in the postman software and results are attached in the PDF format.
