import snowflake.connector
import connection.connection as connect


cursor=connect.cursor

#Initial creation of snowflake filestage
# cursor.execute("create or replace stage API_LOAD.DW_STG.file_stg file_format = (type = 'CSV' field_delimiter = ',' skip_header = 1);")


def loadextracts():
    try:
        cursor.execute(r"PUT 'file:///C:/Users/suyog.pandey/Desktop/API_EXTARCT_SNOWFLAKE/toprated_movies.csv' @API_LOAD.DW_STG.file_stg/toprated_movies.csv overwrite=true")
        print(f"top_rated.csv copied to file stage")
    except snowflake.connector.errors.ProgrammingError as e:
        print(f"error")
    
def load_to_table():
    try:
        cursor.execute(f"TRUNCATE table DW_STG.STG_TOP_MOVIES_LU")
        cursor.execute(f"COPY INTO DW_STG.STG_TOP_MOVIES_LU FROM @FILE_STG.toprated_movies.csv.gz force=false purge=false")
        print(f"data copied from internal stage to stage table successfully")

    except snowflake.connector.errors.ProgrammingError as e:
         print(f"error")
