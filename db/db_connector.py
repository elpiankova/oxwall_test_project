import json

import allure
import pymysql.cursors

from value_objects.user import User


def _our_hash(password):
    d = {
        "pass": "85f36cbbb0e8ac1862637f1355a6a709a678ff02ad8d856056c1452aa6b9a371",
        "test": "62fc22c0da68a727562013a405e45ad29fe67725db24870d8dff48a39b37f5ae",
        "secret": "94d1297b55907d7158b27cd91f0d0b0d212abc0ccd4a3e861b1f4e1f404c67e0"
    }
    return d[password]


param = {"host": 'localhost',
         "user": 'root',
         "password": 'mysql',
         "db":'oxwa824'
         }


class OxwallDB:
    def __init__(self, host, user, password, db):
        self.connection = pymysql.connect(host=host, user=user, password=password, db=db,
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)
        self.connection.autocommit(True)

    def close(self):
        self.connection.close()

    def create_user(self, user):
        with self.connection.cursor() as cursor:
            # Create a new record
            sql = """INSERT INTO `ow_base_user` (`username`, `email`, `password`, `emailVerify`, `joinIp`) 
                     VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(sql, (user.username, user.email, _our_hash(user.password), 0, "2130706433"))
        with self.connection.cursor() as cursor:
            sql1 = f"SELECT * FROM ow_base_user WHERE ow_base_user.username = '{user.username}'"
            cursor.execute(sql1)
            user_id = cursor.fetchone()['id']
            sql = f"""INSERT `ow_base_question_data` (`userId`, `textValue`, `questionName`)
                      VALUES ("{user_id}", "{user.real_name}", "realname")"""
            cursor.execute(sql)
            sql = f"""INSERT `ow_base_question_data`(`userId`, `intValue`, `questionName`)
                      VALUES("{user_id}", {user.gender}, "sex")"""
            cursor.execute(sql)
            sql = f"""INSERT `ow_base_question_data`(`userId`, `dateValue`, `questionName`)
                      VALUES("{user_id}", "1982-02-10 00:00:00", "birthdate")"""
            cursor.execute(sql)

    def get_users(self):

        with self.connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id`, `username`, `password`, `email` FROM `ow_base_user`"
            cursor.execute(sql)
            result = cursor.fetchall()
        return [User(**user) for user in result]

    def delete_user(self, user):
        with self.connection.cursor() as cursor:
            sql1 = f"SELECT * FROM ow_base_user WHERE ow_base_user.username = '{user.username}'"
            cursor.execute(sql1)
            user_id = cursor.fetchone()['id']
            sql = f"""DELETE FROM `ow_base_question_data`
                       WHERE `ow_base_question_data`.`userId` = {user_id};"""
            cursor.execute(sql)
        with self.connection.cursor() as cursor:
            sql = f'''DELETE FROM `ow_base_user`
                      WHERE `ow_base_user`.`username` = "{user.username}"'''
            cursor.execute(sql)

    @allure.step("Get last post from DB")
    def get_last_text_post(self):
        """ Get post with maximum id that is last added """
        with self.connection.cursor() as cursor:
            sql = """SELECT * FROM `ow_newsfeed_action`
                     WHERE `id`= (SELECT MAX(`id`) FROM `ow_newsfeed_action` WHERE `entityType`="user-status")
                     AND `entityType`="user-status"
                     """
            cursor.execute(sql)
            response = cursor.fetchone()
            data = json.loads(response["data"])["status"]
        return data


if __name__ == "__main__":
    db_obj = OxwallDB(host='localhost',
                    user='root',
                    password='mysql',
                    db='oxwa166')

