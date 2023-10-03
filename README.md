# SQLIAExtension:

SQLIAExtension is a browser extension designed to help you protect your web applications from SQL Injection Attacks. SQL Injection is a prevalent and dangerous web application vulnerability that occurs when an attacker can manipulate input to a web application, causing it to execute arbitrary SQL queries. This can lead to data breaches, unauthorized access, and other security risks.
It aims to assist web developers and security professionals in identifying and mitigating SQL Injection vulnerabilities in real time while testing web applications. This extension is designed to work with popular web browsers and provide real-time feedback on potential SQL Injection vulnerabilities.
In our project, we have opted to block malicious requests by redirecting them to a page with an SVG error message.

# Directory Organization:

The primary directory is SQLIA-detection-extension, and it has four subdirectories - Dataset, knowledgebase, static and templates. The main directory also contains core files like app.py, model.pkl, requirements.txt, runtime.txt and vectorizer.txt. The dataset folder contains the dataset that we used to train our model, and the knowledgebase folder contains the database file, populated with a few credentials for login authentication. The CSS files and SVG error file are in the static folders, while the templates directory contains the Materialize CSS templates for the various web pages that we have included in our project.

# Installation:

To upload the extension into the browser, follow the below steps:
1. Go to the "Manage Extensions" option in your browser's extensions.
2. Make sure developer mode is enabled.
3. Use the “Load unpacked extension” option to upload the extension folder.
4. Enable the extension.
The extension can now be used in the browser. 
