import requests
import js2py


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    eval_res, tempfile = js2py.run_file("get_sid.js")
    password = tempfile.ezEncode("TestUserPassword123")
    username = "TestUser"
    my_sid = "z4aktubh"
    my_token = "d0eacd62ae552aab19278eb03ac40dca"
    # login_command = f"http://192.168.0.196:8080/cgi-bin/filemanager/utilRequest.cgi?func=check_sid&sid={my_sid}"
    # r = requests.get(login_command)
    # print(r.content)
    request_str = f"http://192.168.0.196:8080/cgi-bin/authLogin.cgi?user={username}&pwd={password}&remme=1"
    r = requests.get(request_str)
    print(r.content)

    # request_create_folder = f"http://192.168.0.196:8080/cgi-bin/filemanager/utilRequest.cgi?func=createdir&sid={my_sid}&dest_folder=Vanada_folder&dest_path=/Public"
    # r = requests.get(request_create_folder)
    # print(r.content)
