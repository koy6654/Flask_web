import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='myflaskapp')
cursor = db.cursor()

# sql = ''' 
#         CREATE TABLE users(
#             id INT(11) AUTO_INCREMENT PRIMARY KEY, 
#             name VARCHAR(100),
#             email VARCHAR(100),
#             username VARCHAR(30),
#             password VARCHAR(100),
#             register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
#             ENGINE=InnoDB DEFAULT CHARSET=utf8;
#     '''
# sql=''' 
#     CREATE TABLE `topic` (
#     `id` int(11) NOT NULL AUTO_INCREMENT,
#     `title` varchar(100) NOT NULL,
#     `body` text NOT NULL,
#     `author` varchar(30) NOT NULL,
#     `create_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     PRIMARY KEY (id)
#     ) ENGINE=innoDB DEFAULT CHARSET=utf8;
# '''
# cursor.execute(sql)
# db.commit()
# db.close()


# sql_1 조회
sql_1 = 'SELECT * FROM users WHERE `id` = 1;'		# *에 원하는 인자 and where 없으면 전부 조회
cursor.execute(sql_1)
db.commit()

users = cursor.fetchall()
print(users)



# sql_2 행 삽입
sql_2=  '''
        INSERT INTO users(id, name, email , username, password) 		
        VALUES ('3', 'LEE' ,'3@n', 'LEE', '1234');
        '''
#cursor.execute(sql_2)
#db.commt()



# sql_3 변수 받아서 행 삽입
name = 'SONG' 
email = 'S@D'
username = 'HYS'
password = '1234'
sql_3 = '''
        INSERT INTO users(name, email , username, password) 
        VALUES (%s ,%s, %s, %s);
        '''
# cursor.execute(sql_3, (name, email, username, password))
# db.commit()



# sql_4 행 삭제
sql_4 = '''
		DELETE FROM `myflaskapp`.`users` WHERE  `name` = "LEE";

		'''
# cursor.execute(sql_4)
# db.commit()



# sql_5 행 변경
sql_5 = '''
		UPDATE `myflaskapp`.`users` SET `name`='koy' WHERE  `id`=1;
		'''
cursor.execute(sql_5)
db.commit()




db.close()

