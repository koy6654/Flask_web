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
sql_1 = 'SELECT * FROM users;'		# *에 원하는 인자 and where 없으면 전부 조회
cursor.execute(sql_1)
users = cursor.fetchall()

db.commit()
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
# cursor.execute(sql_5)
# db.commit()




# sql_6 topic에 변수 데이터 삽입
title = "JavaScript"
body = "프로토타입기반의 객체지향 프로그래밍 언어로 스크립트 언어에 해당된다. 특수한 목적이 아닌 이상 모든 웹 브라우저에 인터프리터가 내장되어 있다. 오늘날 HTML, CSS와 함께 웹을 구성하는 요소 중 하나다. HTML이 웹 페이지의 기본 구조를 담당하고, CSS가 디자인을 담당한다면 JavaScript는 클라이언트 단에서 웹 페이지가 동작하는 것을 담당한다."
author = "Koy"

sql_6 = '''
                INSERT INTO topic(title, body, author)
                VALUES(%s, %s, %s)
        '''
# cursor.execute(sql_6, (title, body, author))
# db.commit()





# sql_7 topic 행 조회
sql_7 = '''
                SELECT * FROM topic WHERE `id` = 1;
        '''
# cursor.execute(sql_7)
# db.commit()

# users_7 = cursor.fetchall()
# print(users_7)






# sql_8
sql_8 = '''
                INSERT INTO topic(title, body, author)
                VALUES('gary', 'bodddddddddddy' , 'gary')
        '''
# cursor.execute(sql_8)
# db.commit()

db.close()

