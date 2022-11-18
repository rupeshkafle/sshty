from login import Login
from commands import Command
from host import Host

if __name__ == "__main__":
    
    hosts = Host()
    host = hosts.getHost()
    auth = Login(host, 22)

    if auth.proceed() == True:
        command = Command(auth)
        another_command = True
        while another_command:
            get_input = input(">>> ")
            if get_input.lower() == "exit":
                another_command = False
            response = command.custom_command(get_input)
            print(response)
    else:
        print(auth.__str__())
