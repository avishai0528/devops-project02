import pymysql

conn = pymysql.connect(host='remotemysql.com', port=3306, user='e09xbh3mYL', passwd='8ThSvbUTOG', db='e09xbh3mYL')
conn.autocommit(True)
cursor = conn.cursor()


class mysql:

    def select(user_id):
        cursor.execute("SELECT user_name FROM users WHERE user_id = {};".format(user_id))
        user_name = cursor.fetchone()
        return user_name

    def post(user_id, user_name, formatted_date):
        cursor.execute("INSERT into users (user_id, user_name, creation_date) VALUES ('{}', '{}', '{}');".format(user_id, user_name, formatted_date))

    def update(user_id, user_name):
        cursor.execute("UPDATE users SET user_name = '{}' WHERE user_id = '{}';".format(user_name, user_id))

    def check_userid(user_id):
        cursor.execute("SELECT user_id from users where user_id = '{}';".format(user_id))
        a = cursor.fetchone()
        return a[0]

    def delete_user(user_id):
        cursor.execute("DELETE FROM users WHERE user_id = '{}';".format(user_id))