# Press the green button in the gutter to run the script.
from qnap_connection import QnapConnection

if __name__ == '__main__':
    password = "TestUserPassword123"
    username = "TestUser"
    connection = QnapConnection("192.168.0.196", "8080")
    connection.connect(username, password)

    # request_create_folder = f"http://192.168.0.196:8080/cgi-bin/filemanager/utilRequest.cgi?func=createdir&sid={my_sid}&dest_folder=Vanada_folder&dest_path=/Public"
    # r = requests.get(request_create_folder)
    # print(r.content)
