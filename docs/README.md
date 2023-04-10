# Pyjamas

A Python library for developers to way to securely collect and store data in an encrypted manner.

# About Pyjamas

Pyjamas is a cyber-security-focused project built using Flask and Python that enables developers to easily and securely generate forms for integration into their projects. The core feature of Pyjamas is its ability to create separate databases for each form, with data stored in CSV files. Developers can choose to securely store specific fields in their forms by hashing them, with the option to select any one key as the primary key.

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

Read more about the endpoints and issuing requests to them [here](./endpoints)