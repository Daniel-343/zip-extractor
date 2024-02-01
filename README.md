## Zip extractor
This app is used to extract password protected .zip files with a number of known passwords, where we do not know which password goes to which .zip file.
User information is stored in a postgresql database.

### Why is it useful?
Let's say you have a company with hundreds of customers. You occasionally ask a government office to provide information about your customers.
So they send you a password protected .zip file, but they do not tell you which customer the .zip file belongs to, because of GDPR regulations.
The passwords can be calculated by the credentials of your customers so they are given.
What do you do?
Build a python app with a postgresql database that tries to extract the .zip file with every single password that exists in your database.
Once the extraction was successful, you are given a notification about which user the .zip file belongs to.

## How to use it?

### System requirements:
- Linux (for running the supplied database)
- 500mb of storage space
- Docker installed on your system

### Dependencies:
- psycopg2
- dotenv
- tk

Make sure to have these packages installed. The installation process can vary based on your system.

Ideally, you should create your own database for this application, but a dummy database is there if you want to try it.

```
docker run -p 5432:5432 daniel343/zipdb:1.0
```

If you chose to create your own database, you can use the `create.sql` script to set it up.

After you set everything up, you can start up the application with:

```
python3 main.py
```
