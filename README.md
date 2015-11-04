# py-reset-mssql-db

## Description
This is a script made to clean up MS SQL databases.

## Dependency
The script is build for python 2.7 and is using pymssql

``` pip install pymssql ```

Ubuntu also needs:

``` sudo apt-get install freetds-dev ```

## How to use
Edit the run function of the app.py so that it fits your desire

```
  def run():
    host = 'HOST_ADDRESS'
    user = 'USER'
    password = 'PASSWORD'
    database = "DATABASE"


    count = 0

    # Chance 0 to the amount of times to loop
    while (count < 0):
        reset_db(host, user+count, password+count, database)
        count = count + 1

    print '[*] Finished'
```

Afterwards you can run the script with:
```
python app.py
```
