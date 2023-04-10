# Endpoints

1. `/`
    a. Methods accepted
        - `GET`
    b. Functionality
        - Opens the default page. This is for viewing the default page, and does not serve as an API endpoint.
    c. Parameters
         - None

2. `/submit`
    a. Methods accepted
         - `POST`
    b. Functionality
         - You submit all form data in a `POST` request to this endpoint. You include all required fields in the form request, and it will automatically read the form fields from your by getting their names from your local config file (`pyjamas-config.json`). The contents are then passed to the database to be stored.
    c. Parameters
        - All fields defined in the database
        - Example: 
            `{"name": "Vishal", "id": 1001, "country": "India"}`

3. `/find`
    a. Methods accepted
         - `POST`
    b. Functionality
         - This is a lookup API endpoint. You post a request containing the details needed to assemble the primary key in the database, and it returns the row corresponding to the primary key.
    c. Parameters
        - Primary key
        - Example: 
            `{"id": 1001}`

4. `/get`
    a. Methods accepted
         - `GET`
         - `POST`
    b. Functionality
         - This is a UI for the lookup function, and it returns the primary keys of the database so that you can use the primary key to call the `/find` function. 
    c. Parameters
        - None

5. `insert`
    a. Methods accepted
         - `GET`
    b. Functionality
         - This is a UI for the submit function, and it returns a webpage where you can insert data.
    c. Parameters
        - None

