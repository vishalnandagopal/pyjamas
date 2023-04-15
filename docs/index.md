# Pyjamas

A Python library for developers to securely collect and store data in an encrypted manner.

# About Pyjamas

Pyjamas is a cyber-security-focused project built using Flask and Python that enables developers to easily and securely generate forms for integration into their projects. The core feature of Pyjamas is its ability to create separate databases for each form, with data stored in CSV files. Developers can choose to securely store specific fields in their forms by hashing them, with the option to select any one key as the primary key.

We also have an integrated load balancer, that will help developers protect their backends from DDoS attacks.

This suite of products help a developer to quickly iterate on and imporve his actual product, without worrying about security threads like DoS, DDoS, and data leakage.

# What is the need for such a library?

We, as students/developers ourselves, need to be able to quickly generate forms for our apps and projects. However, securely storing the data is a challenging task. If we collecting data for research, especially sensitive data, **it is important to store it in a secure way**, but to still have it in an **accessible format** so that security does not act as a hindrance to quick development.

# Why should I store my data in a encrypted format? I am sure no one can access my data.

Pyjamas presents a way to achieve basic security without working on the security code yourself. As a developer, it is important to store your clients' and users' data securely, and sometimes it is even required by law. Encrypting the data using a password only you know is a good way to store the data you need to handle.

Even if you are sure no one can access your data, it has been proven many times in the security world that if something can be leaked, it will be leaked.

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

    ![Get  Image](./images/get%20diagram.png)

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

# Load Balancer

The integrated load balancer is meant to serve as a simple and quick way for developers to handle large loads of network requests, such as DDoS attack. While it does not prevent or stop DDoS attacks, it can help balance out the load by distributing the requests among different instances of your application, instead of all requests being spammed to one instance.

For example, if you have the same app running in 2 instances, one on port 80 and the other on 81, this will equally distribute and send requests to both those apps.

Every request will be alternated between all running instances of the app.

## So, what if your load balancer is under attack itself? Do you need to put a load balancer on the load balancer?

The load balancer is extremely optimized to handle requests. It does not process any requests, so it is extremely fast since it just forwards them and does not do any parsing or validation like your app. So it can handle and deal with a much larger load compared to your traditional app, since it is built for this one thing.

# Running the program

Make sure you have Python on your system. You can check by running `python --version` in a terminal.

1. In the `pyjamas_forms` folder, open a terminal. Run
    ```
    python app.py
    ```
2. Open the URL given by Flask in a browser. It is usually [`http://localhost:80`](http://localhost:80).

3. For the load balancer, open a terminal and cd into the `load_balancer` folder. Install all the node modules. You will need NPM and NodeJS for that. You can download both of them from [here](nodejs.org/download). Once installed, verify your installation using `node --version` and `npm --version`.
    ```
    cd load_balancer
    npm install
    npm watch
    ```
4. You can mention the ports and the number of instances (integer) it has to protect in the `package.json` file (line 7). For example, if you mention `pnpm nodemon load_balancer.ts 1880 3 round-robin`, it will distribute and forward requests to 3 ports, starting from 1880 (1880, 1881, 1882).

# Using the module

1. After running the Flask app, open the url in your browser. Create a form by filling in the required fields, as you desire.
2. As a developer, you can call the module and perform many functions by issuing API requests at various endpoints.

Read more about the endpoints and issuing requests to them [here]
