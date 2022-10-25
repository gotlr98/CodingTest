import psycopg2

connection = psycopg2.connect("host=localhost dbname=postgres user=haesik password=janghaesick98 port=5432")

cur = connection.cursor()

cur.execute('CREATE TABLE test (id SERIAL PRIMARY KEY);')
connection.commit()