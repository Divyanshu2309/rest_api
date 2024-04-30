import mysql.connector
class user_model():
    def __init__(self):
        #connection establishment code
        try:
            con = mysql.connector.connect(host="localhost",user="root",password="Divyanshu@2021",database="flask_data")
            print("connection sucessful")
        except:
            print("some error")
    def user_getall_model(self):
        
        #query execution code
        return "This is user signup model"