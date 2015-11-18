#!/usr/python
import pymssql
import sql

# Resets the database
def reset_db(host, user, password, database):
    print '[*] Connecting to db: %s' % database
    conn = pymssql.connect(host=host, user=user, password=password, database=database)
    cur = conn.cursor()

    print '[*] Executing sql script'
    cur.execute(sql.sql_query)
    conn.commit()

    conn.close()
    print '[+] Complete!\n'


# Main function
def run():
    host = 'HOST_ADDRESS'
    user = 'USER'
    password = 'PASSWORD'
    database = "DATABASE"


    count = 0

    # Chance 0 to the amount of times to loop
	## Edit this part so it fits your settings.
    while (count < 0):
        reset_db(host, user+str(count), password+str(count), database)
        count = count + 1

    print '[*] Finished'

# Start the script
run()