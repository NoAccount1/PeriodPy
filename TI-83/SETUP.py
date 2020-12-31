content=open("HELPER.py","r").read()

print("The TI-83 Premium CE's resolution is 32*11 characters")
ln=input("Device length :\n>>> ")
wd=input("Device width :\n>>> ")

data="width="+wd+"\nlength="+ln+"\n\n"+content

open("HELPER.py","w").write(data)