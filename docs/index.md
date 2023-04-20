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

1. Download the code using [this url](https://github.com/vishalnandagopal/pyjamas/archive/refs/heads/master.zip) or git clone the repo.
    ```
    git clone https://github.com/vishalnandagopal/pyjamas/
    ```

2. In the `pyjamas_forms` folder, open a terminal. Run
    ```
    python app.py
    ```
3. Open the URL given by Flask in a browser. It is usually [`http://localhost:80`](http://localhost:80).

4. For the load balancer, open a terminal and cd into the `load_balancer` folder. Install all the node modules. You will need NPM and NodeJS for that. You can download both of them from [here](nodejs.org/download). Once installed, verify your installation using `node --version` and `npm --version`.
    ```
    cd load_balancer
    npm install
    npm watch
    ```
5. You can mention the ports and the number of instances (integer) it has to protect in the `package.json` file (line 7). For example, if you mention `pnpm nodemon load_balancer.ts 1880 3 round-robin`, it will distribute and forward requests to 3 ports, starting from 1880 (1880, 1881, 1882).

# Using the module

1. After running the Flask app, open the url in your browser. Create a form by filling in the required fields, as you desire.
2. As a developer, you can call the module and perform many functions by issuing API requests at various endpoints.


# Documentation for contributions by Vishal N (20BCE1043) - DA1

This documentation is for a part of my contributions to the project, which was implementing the security protocols and ciphers that can be used by developers when they integrate Pyjamas.

# How it works?

When developers call the `/submit` endpoint, the following takes place.

![Submit  Image](./images/submit%20diagram.png)

The developer can choose any of the ciphers we have implemented. The ciphers we have implemented are:-
1. AES (can be called with `AES_Cipher.encrypt()`)
2. DES (can be called with `DES_Cipher.encrypt()`)
3. Blowfish (can be called with `Blowfish_Cipher.encrypt()`)
4. Caesar Cipher (can be called with `Caesar_Cipher.encrypt()`)

The ciphers we have integrated are all objects of the `Cipher` class.

The `Cipher` class is:-
```python
    class Cipher:
        def __init__(self, encryption_function, decryption_function, description):
            self.encrypt = encryption_function
            self.decrypt = decryption_function
            self.__doc__ = description
            if not self.testing():
                raise Exception(
                    self.__doc__
                    + " does not seem to be a working decrypt and encrypt functions. Please check the code"
                )
                
        def testing(self) -> bool:
            msg = "vishal"
            if self.decrypt(self.encrypt(msg)).casefold() == msg.casefold():
                return True
            return False

        def verify(self, plain_text, encrypted_message, is_encrypted):
            if not is_encrypted:
                return plain_text == encrypted_message
            return plain_text.casefold() == self.decrypt(encrypted_message).casefold()
```

The `testing` function automatically tests every cipher we implement by encrypting and decrypting the text "vishal", and if it does not match, it raises an error. This is a very important step in automated testing, and for ensuring that there is no change to the encryption or decryption function without throwing an error.


Using the tried and tested `pycryptodome` library, we ensure that these ciphers are implemented without any common vulnerabilities or attacks, like leaking of keys or text.

# Running the Python backend to test the ciphers

Make sure you have Python on your system. You can check by running `python --version` in a terminal.

1. Download the code using [this url](https://github.com/vishalnandagopal/pyjamas/archive/refs/heads/master.zip) or git clone the repo.
    ```
    git clone https://github.com/vishalnandagopal/pyjamas/
    ```

2. In the `pyjamas_forms` folder, open a terminal. Run
    ```
    python app.py
    ```
3. Open the URL given by Flask in a browser. It is usually [`http://localhost:80`](http://localhost:80).

# Commits by Vishal N (20BCE1043) - DA2

This documentation is to showcase the commits I have made while working on this project, as a submission for DA-2.

Author: [`vishalnandagopal`](https://github.com/vishalnandagopal)

## GitHub repository to verify commits

-   [vishalnandagopal/pyjamas - GitHub](https://github.com/vishalnandagopal/pyjamas)
-   [hemangahuja/pyjamas_forms - GitHub](https://github.com/hemangahuja/pyjamas_forms)

Links to individual commits have also been attached below.

## Commit Info

Total Commits: **20+**

-   Major commits: 10
-   Minor commits: 10+

## Selected major commits

1. **Check if the password used is extremely common and occurs in wordlists**

    1. Description: This checks whether the password given is present in a file containing 10,000 of the most commonly used passwords. The list is taken from a [collection of security resources](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10k-most-common.txt)
    2. ID: `c760f02adf608cb067f7bc74019e4012c258afb9`
    3. Link: [@c760f0](https://github.com/vishalnandagopal/pyjamas/commit/c760f02adf608cb067f7bc74019e4012c258afb9)

2. **Initial commit of package during review 1**

    1. Description: This was the inital commit of a full working partial implementation. It was the start of our project.
    2. ID: `da456573ea2bb067ee9dfd9670141af7392c4893`
    3. Link: [@da4565](https://github.com/vishalnandagopal/pyjamas/commit/da456573ea2bb067ee9dfd9670141af7392c4893)

3. **Added documentation as a website.**

    1. Description: Added the documentation and the automatic website generation from .md files, which can be now found at [vishalnandagopal.com/pyjamas](https://vishalnandagopal.com/pyjamas)
    2. ID: `5bdade569da9a60db2c0f1802604ed66516c96f9`
    3. Link: [@5bdade](https://github.com/vishalnandagopal/pyjamas/commit/5bdade569da9a60db2c0f1802604ed66516c96f9)

4. **Added a database component to the project**

    1. Description: Enhanced the project by building a database feature to store data provided by developers.
    2. ID: `95da43c34b71bbe1e55985e0d5d4f24774073694`
    3. Link: [@95da43](https://github.com/vishalnandagopal/pyjamas/commit/95da43c34b71bbe1e55985e0d5d4f24774073694)

5. **Added personal documentation to the website.**

    1. Description: Added my personal DAs and PBL contribution docs.
    2. ID: `065ec1204105383009238920c53d9100191eeb4d`
    3. Link: [@065ec1](https://github.com/vishalnandagopal/pyjamas/commit/065ec1204105383009238920c53d9100191eeb4d)

6. **DES Cipher and OOP of cipher class**

    1. Description: Implemented the DES as a cipher that can be used as developers, and also moved all ciphers to act as an object of a generalized `Cipher` class.
    2. ID: `82a53abf23c697baeef84c3bcb4e3c47031b0831`
    3. Link: [@82a53a](https://github.com/hemangahuja/pyjamas_forms/commit/82a53abf23c697baeef84c3bcb4e3c47031b0831)

7. **Firebase integration**

    1. Description: Integrated Firebase as the cloud component of the project, and developers can now securely store their data in Firebase, as well as access it from anywhere quickly due to using Google's distributed servers.
    2. ID: `86105bd46b1f7091c07868083d9117c2277d0d65`
    3. Link: [@86105b](https://github.com/hemangahuja/pyjamas_forms/commit/86105bd46b1f7091c07868083d9117c2277d0d65)

8. **Added blowfish cipher**

    1. Description: Implemented a quick blowfish cipher.
    2. ID: `80c0881954c1fede88ad5e44bbac656cfa362dcf`
    3. Link: [@80c088](https://github.com/hemangahuja/pyjamas_forms/commit/80c0881954c1fede88ad5e44bbac656cfa362dcf)

# Comments in Code for contributions by Vishal N (20BCE1043) - DA3

This documentation is to showcase well commented code as part of DA-3.

1. **Cipher class**

    ```python
    class Cipher:
        '''
        This class is used to control all ciphers. You can create any cipher by passing it's name and references to it's encryption and decryption function as parameters to this class.
        '''
        def __init__(self):
            # Initialization function that takes in encryption function, decryption function and a description of the cipher
            # This raises an exception if the testing function fails to verify the encryption and decryption functions

        def testing(self) -> bool:
            # A testing function to verify if encryption and decryption are working correctly.
            # It  automatically encrypts and then decrypts the word "vishal". If the output is not the same as "vishal", it returns false.
            # If it is same, it returns true

        def verify(self, plain_text, encrypted_message, is_encrypted):
            # A function to verify if an encrypted message matches the plain text
            # if the message is not encrypted, return True if it matches the plain text
            # Otherwise, return True if the decrypted message (in lowercase) matches the plain text (in lowercase)
    ```

2. **Blowfish encryption and decryption functions**

    1. Encryption

        ```python
        def blowfish_encrypt(plaintext):
            '''
            Create a new instance of the Blowfish cipher with the provided key and ECB mode
            '''
            # Pad the plaintext to match the block size of the cipher
            # Encrypt the padded plaintext using the Blowfish cipher
            # Encode the encrypted plaintext using base64 and return the result
        ```

    2. Decryption

        ```python
        def blowfish_decrypt(encoded_plaintext):
            '''
            Create a new instance of the Blowfish cipher with the provided key and ECB mode
            '''
            # Decode the base64-encoded encrypted plaintext
            # Decrypt the encrypted plaintext using the Blowfish cipher
            # Unpad the decrypted plaintext and decode it to return the result
        ```

3. **Caesar cipher encryption and decryption functions**

    1. Encryption

        ```python
        def caesar_encrypt(message):
            """
            Encrypts a message using the Caesar cipher with the given key.
            """
            # Check if character is a letter
            # Convert to uppercase
            # Apply shift based on key
            # Add shifted character to result
            # Add non-letter character as is
        ```

    2. Decryption

        ```python
            def caesar_decrypt(message):
            """
            Decrypts a message using the Caesar cipher with the given key.
            """
            # Check if character is a letter
            # Convert to uppercase
            # Apply reverse shift based on key
            # Add shifted character to result
            # Add non-letter character as is
        ```

4. AES encryption and decryption functions

    1. Encryption

        ```python
        def aes_encrypt(message):
            """
            Encrypts a message using the AES algorithm in ECB mode.
            """
            # Create a new AES object with the key and mode
            # Pad the message to a multiple of 16 bytes using spaces
            # Encrypt the padded message using AES
            # Encode the encrypted message in base64 and return as a string
        ```

    2. Decryption
        ```python
        def aes_decrypt(encrypted_message):
            """
            Decrypts an encrypted message using the AES algorithm in ECB mode.
            """
            # Create a new AES object with the key and mode
            # Decode the encrypted message from base64
            # Decrypt the decoded message using AES
            # Remove any trailing whitespace from the decrypted message and return
        ```

# Commits contributions by Hemang Ahuja (20BCE1302)

This documentation is to showcase the commits I have made while working on this project, as a submission for DA-2.

## GitHub repository to verify commits

[hemangahuja/pyjamas_forms - GitHub](https://github.com/hemangahuja/pyjamas_forms)

### **[initial commit · hemangahuja/pyjamas_forms@111b62f · GitHub](https://github.com/hemangahuja/pyjamas_forms/commit/111b62f35093dfef5b0b8cf9b9b2f4672839f64e)**

- This commit is the first commit of the project.
- Commit hash: 111b62f35093dfef5b0b8cf9b9b2f4672839f64e

### **[add lookup and primiary key feature · hemangahuja/pyjamas_forms@cda0093 · GitHub](https://github.com/hemangahuja/pyjamas_forms/commit/cda0093e23913f839f1cf98755a7e7ce217f4797)**

- This commit adds a lookup and primary key feature to the project.
- It allows users to search for specific data in the project using a primary key.
- Commit hash: cda0093e23913f839f1cf98755a7e7ce217f4797

### **[implement encryption · hemangahuja/pyjamas_forms@dc25cc9 · GitHub](https://github.com/hemangahuja/pyjamas_forms/commit/dc25cc96358aa3fbb22adc53b4bbb10e5bd4ae69)**

- This commit implements encryption in the project.
- It encrypts sensitive data that can be stored of users to protect it from unauthorized access.
- Commit hash: dc25cc96358aa3fbb22adc53b4bbb10e5bd4ae69

### **[added load_balancer and logging · hemangahuja/pyjamas_forms@926ff19 · GitHub](https://github.com/hemangahuja/pyjamas_forms/commit/926ff191337982c64389f04b8e7c471b04aa0f93)**

- This commit adds a load balancer and logging to the project.
- The load balancer distributes incoming network traffic across multiple servers to improve performance and reliability. 
- The logging feature records events that occur in the project for debugging purposes.
- Commit hash: 926ff191337982c64389f04b8e7c471b04aa0f93

### **[add comments to contributions · hemangahuja/pyjamas_forms@1bc7ca4 · GitHub](https://github.com/hemangahuja/pyjamas_forms/commit/1bc7ca42ae1e5d17547a94e38060bbfa3a58f44e)**

- This commit adds comments to contributions

- Commit hash: 1bc7ca42ae1e5d17547a94e38060bbfa3a58f44e

# Comments in code contributions by Hemang Ahuja (20BCE1302)

This documentation is to showcase the comments I have made while working on this project, as a submission for DA-3.

## load_balancer.ts

-   ### configures the load balancer to point to the specified port using the specified algorithm

-   ```typescript
    const [basePort, _count, algorithm] = process.argv.slice(2);
    const count = Number(_count);
    ```

-   ### creates proxy instance for request forwarding

    ```typescript
    const proxy = httpProxy.createProxyServer({});
    ```

-   ### hashes a string to a number

    ```typescript
    const hashCode = (str: string): number
    ```

-   ### returns index of the server to be used using different algorithms for load balancing.

    ```typescript
    const getServer = (options?: object): number
    ```

-   ### processes the request and returns the response after balancing the load

    ```typescript
    const handler = async (req: express.Request, res: express.Response)
    ```

-   ### calculate server address using algorithm and base port

    ```typescript
    const server = `http://localhost:${
        Number(basePort) +
        getServer({
            query,
            method,
            body,
        })
    }`;
    ```

-   ### sends request to the server

    ```typescript
    proxy.web(req, res, { target: server });
    ```

-   ### starts the server at the specified port

    ```typescript
    app.use(handler);
    app.listen(1337, () => console.log("Load balancer running at port 1337"));
    ```

## http-proxy.ts

-   ### Create your proxy server and set the target in the options.

    ```typescript
    httpProxy
        .createProxyServer({ target: "http://localhost:9000" })
        .listen(8000);
    ```

-   ### Create your target server

    ```typescript
    http.createServer(function (req, res) {
        res.writeHead(200, { "Content-Type": "text/plain" });
        res.write(
            "request successfully proxied!" +
                "\n" +
                JSON.stringify(req.headers, true, 2)
        );
        res.end();
    }).listen(9000);
    ```

-   ### Create your custom server and just call `proxy.web()` to proxy a web request to the target passed in the options

    ```typescript
    var server = http.createServer(function (req, res) {
        proxy.web(req, res, { target: "http://127.0.0.1:5050" });
    });
    ```

-   also you can use `proxy.ws()` to proxy a websockets request

    ```typescript
    proxy.ws(req, res, { target: "http://127.0.0.1:5050" });
    ```

# Pyjamas

# Commits by Sreenath 20BCE1450

This documentation is to showcase commits as part of DA-2.
<br><br>
<b>_Author_</b> : `StormPredator-Sr`
<br><br>

-   Comment Name : sreenath

    <u>Description of commit</u> &nbsp;: &nbsp;Added template for frontend.

    <u>Commit id</u> &nbsp; : &nbsp; `bed4513cf24331c8ee73111a2db9fa81f74087ef`

    <u>Link</u> &nbsp; : &nbsp; [https://github.com/hemangahuja/pyjamas_forms/commit/bed4513cf24331c8ee73111a2db9fa81f74087ef](https://github.com/hemangahuja/pyjamas_forms/commit/bed4513cf24331c8ee73111a2db9fa81f74087ef)

    <u>Changes made</u> &nbsp; : &nbsp; Added template for the index file along with css file and logo.gif along with dynamic form generation using JavaScript to adjust number of fields in form according to number of fields entered by user.

<br>

-   Comment Name : Fix the server and some comments

    <u>Description of commit</u> &nbsp;: &nbsp; Fixed issues with the server

    <u>Commit id</u> &nbsp; : &nbsp; `3dbe21fcd80e1fd68abca98f0f1eb0ca77970a16`

    <u>Link</u> &nbsp; : &nbsp; [https://github.com/hemangahuja/pyjamas_forms/commit/3dbe21fcd80e1fd68abca98f0f1eb0ca77970a16](https://github.com/hemangahuja/pyjamas_forms/commit/3dbe21fcd80e1fd68abca98f0f1eb0ca77970a16)

    <u>Changes made</u> &nbsp; : &nbsp; Added loading config file, creatng database, creating logger for logging, loading configuration file and render template and also get form response and encrypts the fields that are to be encrypted and write processed data to database. Added render UI for insertng row in database.

<br>

-   Comment Name : Use AES_Cipher class

    <u>Description of commit</u> &nbsp;: &nbsp; Addition on AES_Cipher class for encryptions.

    <u>Commit id</u> &nbsp; : &nbsp; `76545d2bd3b59aad215e2514a52767968532ff3f`

    <u>Link</u> &nbsp; : &nbsp; [https://github.com/hemangahuja/pyjamas_forms/commit/76545d2bd3b59aad215e2514a52767968532ff3f](https://github.com/hemangahuja/pyjamas_forms/commit/76545d2bd3b59aad215e2514a52767968532ff3f)

    <u>Changes made</u> &nbsp; : &nbsp; Added AES encryption and decryption function, Caesar encryption and decryption function, Blowfish encryption and decryption function.

# Pyjamas

# Comments by Sreenath 20BCE1450

This documentation is to showcase commented code as part of DA-3.

-   `/pyjamas_forms`

    -   `app.py`

        i. This module contains the main application logic and routes.

        ii. The app.py module has the following steps:

        -   <b>Loading the config</b> - _import the config.py module that contains the configuration variables such as encryption key, database name, etc._

        -   <b>Create the database</b> - _create an instance of the Database class from database.py and pass it the database name from config.py_

        -   <b>Create a logger instance for logging purposes </b>- _use the logging module to create a logger object that can log messages to a file or console._

        -   <b>Logging each request</b> - _use a decorator function to log each request made to the app with its method, path and status code._

        -   <b>Load the configuration file and render the index template </b>- _use the render_template function from flask to load the index.html template and pass it the configuration variables from config.py_

        -   <b>Get a form response and encrypts the fields that are to be encrypted </b>- _use the request.form object from flask to get the data from a POST request and use the cryptography module to encrypt some of the fields using the encryption key from config.py_

        -   <b>Writes the processed data to the database</b> - _use the write_row method from Database class to write the encrypted data to the database._

        -   <b>Gets a form response to be searched for in the database</b> - _use the request.form object from flask to get the data from a POST request and use it as a query for finding a row in the database._

        -   <b>Decrypt the rows in database based on encryption key and matches to form response</b> - _use the cryptography module to decrypt some of the fields in each row using the encryption key from config.py and compare them with the query data._

        -   <b>Return the row if found </b>- _use the jsonify function from flask to return a JSON response with the row data if found or an error message if not found._

        -   <b>Render a UI for searching in the database with the appropriate primary keys and inserting row in database</b> - _use the render_template function from flask to load the search.html template and pass it a list of primary keys that are required for searching in the database._

    -   `database.py`

        This module contains the class Database that handles the database operations.

        i. <b>Methods used</b>:

        -   To initialize the database instance with the given name

                   __init__(self, db_name)

        -   Write a row to the database with the given data dictionary

                  write_row(self, data)

        -   Prints all the rows in the database to the console

                  print_all(self)

        -   Find operaton on the database, loops through all the encrypted data to find the matching row.

                  find(self, query)

            i. `query`: a dictionary of key-value pairs to search for

            ii. `returns`: a list of rows that match the query or an empty list if none found