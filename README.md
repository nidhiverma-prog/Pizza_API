# Pizza_API
Api to list all the data stored in database :
       GET http://127.0.0.1:8000/pizza/
To filter the data based on Pizza size or Pizza Type:
        GET http://127.0.0.1:8000/pizza/
        params:
        Key:pizza_type or pizza_size with the value.
To post new entry to the database:
      POST http://127.0.0.1:8000/pizza/
      key : value(form-data)
      pizza_size : 
      pizza_type :
      toppings :
To delete all entry from the database:
     DELETE http://127.0.0.1:8000/pizza/
To delete particular entry from the databse:
    DELETE http://127.0.0.1:8000/pizzadetail/ID/
    pass the particular id you want to delete in url 
To update particular data stored in database:
    PUT http://127.0.0.1:8000/pizzadetail/ID/
    Give the data you want to update (input in JSON Format)
    
Steps to Run The Project:
1.create virtual environment and install all the package listed in Requirements.txt file
2.Activate the virtual environment by env_name\Scripts\activate.
3.Go inside the directory pizza_site.
4.Run command python manage.py runserver.
   
