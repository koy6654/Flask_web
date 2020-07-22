#서버와 교류하는 방법은 get 방식과 post 방식이 있다
#get 방식은 URL에 데이터를 포함시켜서 교류함 (보안 취약, 빠름)
#post 방식은 html문서 body에 데이터를 포함시켜서 교류함(보안 강하고 get보다 느림)

from flask import Flask, render_template       # render_template : 요청한 클라이언트에 HTML형식으로 문서화 시켜서 보내는 Class
from data import Articles
from flask import flash, redirect, url_for, session, request, logging
import pymysql

app = Flask(__name__)
app.debug = True

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='myflaskapp')


@app.route("/")      # decoration : 메소드를 연계하게 해준다. (app.route 경로지정)
def index():
    print("World success")                                  # cmd에 World success 출력
    # return "TEST"
    return render_template("home.html", hello = "Koy")      # 만들어둔 home.html의 문서 데이터를 페이지로 불러 시각화함
                                                            # render_template class 및 method는 파일 내 templates 파일에 플러그인 함(내부 class 자체가 이렇게 코딩되어있음 즉, templates 파일을 만들 것)
                                                            # hello 변수에 "koy" 저장 후 home.html에 사용가능 {{}}로 호출
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/articles", methods = ['GET', 'POST'])      # GET 형식과 POST 형식 둘 다 적용되게 함
def articles():
    articles = Articles()
    print(len(articles))
    return render_template("articles.html", articles = articles)


@app.route("/image")
def image():
    return render_template("image.html")


@app.route("/article/<int:id>")
def article(id):
    print(type(id))
    articles = Articles()
    return render_template("article.html", articles = [articles, id])


@app.route("/register", methods=['GET','POST'])
def register():
    if request.method == 'POST':
        # data = request.body.get('author')
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        re_password = request.form.get('re_password')
        username = request.form.get('username')

        if password == re_password:
            print(name, email, password, re_password, username)

            cursor = db.cursor()
            sql =   '''
                        INSERT INTO users(`name`, `email`, `username`, `password`)
                        VALUES(%s, %s, %s, %s)
                    '''

            cursor.execute(sql, (name, email, username, password))
            db.commit()
            

            cursor = db.cursor()
            sql_select = 'SELECT * FROM users;'
            cursor.execute(sql_select)
            users = cursor.fetchall()
            db.commit()
            print(users)
            db.close()
           

            return "POST SUCCESS"
        else:
        # name = form.name.data
            return "Invaild Password"
    else:
        return "GET Success"


if __name__ == "__main__":      # 여길 제일 먼저 실행 (가장 초입에 작성)
    # app.run(host = "0.0.0.0", port = "8080")
    app.run()                   # defalut 값 port = "5000"