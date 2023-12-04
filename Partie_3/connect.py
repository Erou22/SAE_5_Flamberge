import psycopg2


host="servbdd"
database="pg_maallain"
user="maallain"
password="C0mitejapt_"
schema="flamberge"

conn = psycopg2.connect(host=host,database=database,user=user,password=password)