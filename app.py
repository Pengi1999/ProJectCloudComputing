import sys
import logging
import rds_config
import pymysql
#rds settings
rds_host  = "rds-instance-endpoint"
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")
def handler(event, context):
    """
    This function fetches content from MySQL RDS instance
    """

    item_count = 0

    with conn.cursor() as cur:
        cur.execute("create table VatLieu ( VatLieuID  int NOT NULL, Name varchar(255) NOT NULL, PRIMARY KEY (VatLieuID))")
        cur.execute('insert into VatLieu (VatLieuID, Name) values(1, "Sat")')
        cur.execute('insert into VatLieu (VatLieuID, Name) values(2, "Go")')
        cur.execute('insert into VatLieu (VatLieuID, Name) values(3, "Vang")')
        conn.commit()
        cur.execute("select * from VatLieu")
        for row in cur:
            item_count += 1
            logger.info(row)
            #print(row)
    conn.commit()

    return "Added %d items from RDS MySQL table" %(item_count)