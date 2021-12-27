# %%
import base64
import gvar as gv

f=open('SM.png','rb') #二进制方式打开图文件
ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
f.close()
gv.dump(ls_f, 'ls_f')

# %%
bs=gv.load('ls_f')
imgdata=base64.b64decode(bs)
file=open('SM_re.jpg','wb')
file.write(imgdata)
file.close()