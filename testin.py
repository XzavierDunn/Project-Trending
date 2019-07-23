import psycopg2

while True:
        engine = psycopg2.connect(
                database='postgres',
                user='newtestuser',
                password='masterpass12',
                host='testid.csrw9zlcpo5t.us-east-1.rds.amazonaws.com',
                port='5432'
                )
        if engine:
                print('worked')

# db instance id 'testid'
# master username 'newtestuser'
# master password 'masterpass12'
# database name 'trenddb'
# port '5432'
