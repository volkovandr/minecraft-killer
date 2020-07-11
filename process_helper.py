import os
import subprocess
import errno

def get_minecraft_pid():
    ps = subprocess.Popen("ps -aux | grep java | grep .minecraft", shell=True, stdout=subprocess.PIPE)
    ps_pid = ps.pid
    output = ps.stdout.read()
    ps.stdout.close()
    ps.wait()

    for line in output.decode().split("\n"):
        if line != "" and line != None:
            fields = line.split()
            pid = fields[1]
            return pid
    return 0

def kill_process(pid):
    try:
        os.kill(int(pid), 15)
    except OSError as err:
        if err.errno == errno.ESRCH:
            print("Not running")
        elif err.errno == errno.EPERM:
            print("No permission to signal this process!")
        else:
            print("Unknown error")
    else:
        print("Killed")
