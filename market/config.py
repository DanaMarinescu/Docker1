DEV_DB =  'sqlite:///market.db'

pg_user = 'admin'
pg_pass = 'admin'
pg_db = 'market'
pg_host = 'localhost'
pg_port = 5432

#define an URI that will define the connection to some service
PROD_DB = f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}'