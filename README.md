# py-reset-mssql-db

## Description
This is a script made to clean up MS SQL databases.
It will:
* Drop all non-system stored procedures
* Drop all Foreign Key constraints
* Drop all Primary Key constraints
* Drop all tables

## Dependency
The script is build for python 2.7 and is using pymssql

``` pip install pymssql ```

Ubuntu also needs:

``` sudo apt-get install freetds-dev ```

## How to use
Edit the run function of the app.py so that it fits your desire

```
# Main function
def run():
    count = 0

    # Chance 0 to the amount of times to loop
	## Edit this part so it fits your settings.
    while (count < 0):
        host = 'HOST_ADDRESS'
        usr = 'USER%s' % (str(count))
        pas = 'PASSWORD%s' % (str(count))
        db = 'DATABASE%s' % (str(count))
		
        print 'usr %s, password %s, db %s' % (usr, pas, db)
		
        reset_db('ealdb1.eal.local', usr, pas, db)
        count = count + 1
		

    print '[*] Finished'

```

Afterwards you can run the script with:
```
python app.py
```
