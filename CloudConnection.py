import time

import mysql.connector
import sqlalchemy
import os

# Assuming the .pem files are in the same directory as the Python script
server_ca_pem_filepath = r"C:\Users\YuvrajKorotana\PycharmProjects\PythonAutomationScriptforCloudServices\server-ca.pem"
client_cert_pem_filepath = r"C:\Users\YuvrajKorotana\PycharmProjects\PythonAutomationScriptforCloudServices\client-cert.pem"
client_key_pem_filepath = r"C:\Users\YuvrajKorotana\PycharmProjects\PythonAutomationScriptforCloudServices\client-key.pem"



with open(server_ca_pem_filepath, 'r') as f:
    server_ca_pem = f.read()

with open(client_cert_pem_filepath, 'r') as f:
    client_cert_pem = f.read()

with open(client_key_pem_filepath, 'r') as f:
    client_key_pem = f.read()


# Database credentials
db_host = "35.232.135.149"  # Replace with your Cloud SQL connection name
db_user = "ykmain"
db_password = "ykmain-password"
db_name = "ProductSentiment"

def get_cloud_connection():
    try:
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name,
            connection_timeout=20,  # Set timeout (in seconds)
            ssl_ca=server_ca_pem_filepath,
            ssl_cert=client_cert_pem_filepath,
            ssl_key=client_key_pem_filepath,
        )
        print("Connection successful!")


        return connection

    except mysql.connector.Error as err:
        print(f"Error: {err}")












    # return connection
#
# # Using SQLAlchemy for queries
# engine = sqlalchemy.create_engine(
#     f"mysql+pymysql://root:{db_password}@{db_host}?ssl_ca={server_ca_pem_filepath}&ssl_cert={client_cert_pem_filepath}&ssl_key={client_key_pem_filepath}"
# )
# try:
#   with engine.connect() as conn:
#     result = conn.execute("SELECT 1")
#     print("Connection successful!")
# except Exception as e:
#     import traceback
#     print(f"Error connecting to database: {e}")
#     traceback.print_exc()
#
# # mysql -uroot -p -h 35.232.135.149 --ssl-ca=server-ca.pem --ssl-cert=client-cert.pem --ssl-key=client-key.pem