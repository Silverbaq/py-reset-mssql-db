#!/usr/python
import pymssql
import sql

# Resets the database
def reset_db(host, user, password, database):
    print '[*] Connecting to db: %s' % database
    conn = pymssql.connect(host=host, user=user, password=password)
    cur = conn.cursor()

    print '[*] Executing sql script'
    cur.execute(sql.sql_query)
    conn.commit()

    conn.close()
    print '[+] Complete!\n'


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
		
        reset_db(host, usr, pas, db)
        count = count + 1
		

    print '[*] Finished'

# Start the script
run()