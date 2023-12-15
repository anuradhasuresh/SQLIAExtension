# Chrome Extension for Recognition of SQL Injection Attacks:

# Overview
This project, conducted between March 2021 and May 2022, encompasses the design and development of a Chrome Extension dedicated to recognising SQL injection attacks within web form fields. Leveraging a unique combination of a random forest and an Adaptive Deep Forest neural network model, this extension showcases expertise in Python, JavaScript, and cybersecurity concepts.

SQLIAExtension is a browser extension designed to help you protect your web applications from SQL Injection Attacks. SQL Injection is a prevalent and dangerous web application vulnerability that occurs when an attacker can manipulate input to a web application, causing it to execute arbitrary SQL queries. This can lead to data breaches, unauthorized access, and other security risks.
It aims to assist web developers and security professionals in identifying and mitigating SQL Injection vulnerabilities in real-time while testing web applications. This extension is designed to work with popular web browsers and provide real-time feedback on potential SQL Injection vulnerabilities.
In our project, we have opted to block malicious requests by redirecting them to a page with an SVG error message.

# Directory Organization:

The primary directory is SQLIA-detection-extension, and it has four subdirectories - Dataset, knowledgebase, static and templates. The main directory also contains core files like app.py, model.pkl, requirements.txt, runtime.txt and vectorizer.txt. The dataset folder contains the dataset that we used to train our model, and the knowledgebase folder contains the database file, populated with a few credentials for login authentication. The CSS files and SVG error files are in the static folders, while the templates directory contains the Materialize CSS templates for the various web pages that we have included in our project.

# Features:
1. SQL Injection Detection: Orchestrated the development of a Chrome Extension capable of detecting SQL injection attacks in web form fields.
2. Database Integration: Used Linode and SQLite as databases for storing and retrieving information related to SQL injection attacks.
3. Model Training: Actively led the model training process to optimize the extension's ability to recognize and mitigate SQL injection threats.
4. Machine Learning Models: Implemented a unique combination of a random forest and an Adaptive Deep Forest neural network model to enhance the accuracy of SQL injection attack detection.
5. Linux Development Environment: Developed and tested the extension in a Linux development environment, ensuring compatibility and robust performance.
6. Hosting with Flask and Heroku: Seamlessly integrated and hosted the extension using Flask and Heroku, showcasing a commitment to security-conscious programming.

# Research Paper:
A comprehensive survey paper was written during the research phase of this project:

Title: "Literature Survey on Web-based Recognition of SQL Injection Attacks"
Date: March 29th, 2022
Link: https://www.irjet.net/archives/V9/i3/IRJET-V9I3281.pdf


# Installation:
To upload the extension into the browser, follow the below steps:
1. Go to the "Manage Extensions" option in your browser's extensions.
2. Make sure developer mode is enabled.
3. Use the “Load unpacked extension” option to upload the extension folder.
4. Enable the extension.
The extension can now be used in the browser. 

# Testing:
Conducted rigorous testing to ensure the extension's accuracy in detecting SQL injection attacks.

# Contributors:
1. Anuradha Ramchandran
2. Nikita Bhyri
3. Sreeraksha H R

# License
This project is licensed under the MIT License.

Feel free to explore, contribute, and enhance the Chrome Extension for Recognition of SQL Injection Attacks! If you encounter any issues or have suggestions, please open an issue or submit a pull request. Your contributions and feedback are valuable in furthering the project's security capabilities.
