# Endpoints

1. `/`

    1. Methods accepted

    - `GET`

    2. Functionality

    - Opens the default page. This is for viewing the default page, and does not serve as an API endpoint.

    3. Parameters

    - None

2. `/submit`

    1. Methods accepted

    - `POST`

    2. Functionality

    - You submit all form data in a `POST` request to this endpoint. You include all required fields in the form request, and it will automatically read the form fields from your by getting their names from your local config file (`pyjamas-config.json`). The contents are then passed to the database to be stored.

    3. Parameters

    - All fields defined in the database
    - Example:
        ```json
        {
            "name": "Vishal",
            "id": 1001,
            "country": "India"
        }
        ```

3. `/find`

    1. Methods accepted

    - `POST`

    2. Functionality

    - This is a lookup API endpoint. You post a request containing the details needed to assemble the primary key in the database, and it returns the row corresponding to the primary key.

    3. Parameters

    - Primary key
    - Example:
        ```json
        {
            "id": 1001
        }
        ```

4. `/get`

    1. Methods accepted

    - `GET`
    - `POST`

    2. Functionality

    - This is a UI for the lookup function, and it returns the primary keys of the database so that you can use the primary key to call the `/find` function.

    3. Parameters

    - None

5. `insert`
    1. Methods accepted
    - `GET`
    2. Functionality
    - This is a UI for the submit function, and it returns a webpage where you can insert data.
    3. Parameters
    - None
