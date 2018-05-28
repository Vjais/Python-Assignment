import MySQLdb
from intercom.client import client


#access token
intercom=Client(personal_access_token='testing')

# Open database connection
db = MySQLdb.connect("localhost", "testuser", "testpassword", "gfgdb")

cursor = db.cursor()

# Drop table if it already exist using execute()
cursor.execute("DROP TABLE IF EXISTS user")

# Create table as per requirement
sql = CREATE TABLE user (
   id int(11) NOT NULL AUTO_INCREMENT,
   name text NOT NULL,
   email varchar(120) NOT NULL
   PRIMARY KEY (id),
   UNIQUE KEY email (email)
)  ENGINE=InnoDB DEFAULT CHARSET=utf8; # table created

#Create user on intercom and list on intercom
intercom.user.create(name='john',email='john23@gmail.com')
for i in intercom.user.all():
    intercom.user.find_all(i)

intercom.user.findall(tag_email='john23@gmail.com')
# disconnect from server
db.close()