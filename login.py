import paramiko as p
from getpass import getpass

class Login:
    authenticated = False
    def __init__(self, host, port, key=None):
        self.host = host
        self.port = port
        if key != None:
            self.key = p.RSAKey.from_private_key_file(key)
        else:
            self.key = key
    
    def __str__(self):
        return self.error

    def proceed(self):
        try:
            self.client = p.SSHClient()
            self.client.set_missing_host_key_policy(p.AutoAddPolicy())
            if self.key != None:
                return self.key_based_ssh()
            else:
                return self.password_based_ssh()
        except ConnectionError as e:
            self.error = e

    def password_based_ssh(self):
        self.username = input("Enter Username: ")
        self.password = getpass("Enter Password: ")
        try:
            self.auth = self.client.connect(
                hostname=self.host,
                username=self.username,
                password=self.password,
                allow_agent=False,
                look_for_keys=False
            )
            self.authenticated = True
        except p.AuthenticationException as e:
            self.error = e
        except p.BadHostKeyException as e:
            self.error = e
        except p.ChannelException as e:
            self.error = e.text
        except TimeoutError as e:
            self.error = e.strerror
        return self.authenticated
        
    def key_based_ssh(self):
        # TODO: implement key based SSH for advanced implementation
        pass
        
    def telnet(self):
        # TODO: implement TELNET to support legacy devices without SSH support
        pass

