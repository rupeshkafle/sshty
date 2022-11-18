import time
import paramiko as p

class Command:
    def __init__(self, auth):
        self.auth = auth

    def list_directory(self, dir=None):
        try:
            if dir == None:
                stdin, stdout, stderr = self.auth.client.exec_command('ls -al')
            else:
                stdin, stdout, stderr = self.auth.client.exec_command(f'ls -al {dir}')
            err = stderr.read().decode()
            if err:
                raise RuntimeError("Error while reading directory contents.")
            return stdout.read().decode()
        except RuntimeError as e:
            return e

    def custom_command(self, command):
        try:
            stdin, stdout, stderr = self.auth.client.exec_command(command)
            time.sleep(5)
            err = stderr.read().decode()
            if err:
                raise RuntimeError("Error while executing command")
            return stdout.read().decode()
        except RuntimeError as e:
            return e
        
        