# Pyjamas

A Python library for developers to way to securely collect and store data in an encrypted manner.

# About Pyjamas

Pyjamas is a cyber-security-focused project built using Flask and Python that enables developers to easily and securely generate forms for integration into their projects. The core feature of Pyjamas is its ability to create separate databases for each form, with data stored in CSV files. Developers can choose to securely store specific fields in their forms by hashing them, with the option to select any one key as the primary key.

We also have an integrated load balancer, that will help developers protect their backends from DDoS attacks.

This suite of products help a developer to quickly iterate on and imporve his actual product, without worrying about security threads like DoS, DDoS, and data leakage.

# What is the need for such a library?

We, as students/developers ourselves, need to be able to quickly generate forms for our apps and projects. However, securely storing the data is a challenging task. If we collecting data for research, especially sensitive data, **it is important to store it in a secure way**, but to still have it in an **accessible format** so that security does not act as a hindrance to quick development.

# Running the program

Make sure you have Python on your system. You can check by running `python --version` in a terminal.

1. In the `pyjamas_forms` folder, open a terminal. Run
    ```
    python app.py
    ```
2. Open the URL given by Flask in a browser. It is usually [`http://localhost:80`](http://localhost:80).

# Using the module

1. After running the Flask app, open the url in your browser. Create a form by filling in the required fields, as you desire.
2. As a developer, you can call the module and perform many functions by issuing API requests at various endpoints.

Read more about the endpoints and issuing requests to them [here]

# Endpoints

1. `/`

    1. Methods accepted

    - `GET`

    2. Functionality

    - Opens the default page. This is for viewing the default page, and does not serve as an API endpoint.

    3. Parameters

    - None

2. `/submit`

    ![Submit  Image](./images/submit%20diagram.png)

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

    ![Find  Image](./images/find%20diagram.png)

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

5. `/insert`

    1. Methods accepted

    - `GET`
    
    2. Functionality
    
    - This is a UI for the submit function, and it returns a webpage where you can insert data.
    
    3. Parameters
    
    - None