from platform import uname
from os import path,system,chmod
from sys import argv
try:
    if argv[1].lower()=="reset":
        system("rm -rf bxi")
except:
    pass
arch=uname().machine.lower()
if "arm" in arch:
    arch="arm"
elif "aarch" in arch:
    arch="aarch"
else:
    exit(f" Unsupported architecture [{arch}]")
while True:
    if path.isfile("bxi"):
        break
    else:
        system(f"curl -L https://raw.githubusercontent.com/Binyamin-binni/executables/main/bxi/{arch} -o bxi")
        
chmod("bxi",0o777)
system("./bxi")
exit("\n\n If bxi not starting then use this command\n python bxi.py reset")
