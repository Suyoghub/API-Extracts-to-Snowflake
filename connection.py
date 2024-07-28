import snowflake.connector

#Use your Snowfake user credentials to connect

conn = snowflake.connector.connect(
        user='',
        password='',
        account='fo32592.central-india.azure',
                database='APILOAD',
    )

cursor = conn.cursor()