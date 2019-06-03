
from tkinter import *
from tkinter.messagebox import *
import pymysql
import os,subprocess
# from mstsc_rdp import Authentication

class LoginPage(Frame):
    def __init__(self):
        Frame.__init__(self)
        # self.username = StringVar()
        # self.password = StringVar()
        self.pack()
        self.createForm()

    def createForm(self):
        # Label(self,bg='#B9D3EE',fg='red').grid(row=0, stick=W, pady=10)
        # Label(self,bg='#B9D3EE', text='学号: ').grid(row=1, stick=W, pady=10)
        # Entry(self, textvariable=self.username).grid(row=1, column=1, stick=E)
        # Label(self,bg='#B9D3EE', text='密码: ').grid(row=2, stick=W, pady=10)
        # Entry(self, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self,bg='#B03060', text='上传作业',fg='white', command=self.loginStudent).grid(row=4, stick=W, pady=10)
        Button(self,bg='#458B00',  text='下载作业', fg='white',command=self.loginTeacher).grid(row=5, stick=E)

    def loginStudent(self):
        sharedir = os.popen('whoami').read()
        print(sharedir)
        #     if len(result) != 0 :
        host = '192.168.128.28'
        sharedir= sharedir.split('\\')[1]
        print(sharedir)
        netuse = 'net use u: \\GZYHJLIC\个人网盘\{0} 123456 /user:gzucm\{1} '.format(sharedir,sharedir)
        mult = netuse.split('\n')
        # for i in list(netuse):

        print(mult[0]+mult[1])
        cmd_netuse = mult[0]+mult[1]
        print ("login success")
        # do_to = Authentication()
        # do_to.cmdkey_pc(host)

        cmd = r"start u: "

        os.system(netuse)
        os.system(cmd)
        print(cmd)
        self.destroy()
    def loginTeacher(self):

        host = '192.168.128.28'

        netuse = r"""net use z: \\GZYHJLIC\class"""
        print(netuse)
        print ("login success")
        # do_to = Authentication()
        # do_to.cmdkey_pc(host)

        cmd = r"start z: "

        os.system(netuse)
        os.system(cmd)
        print(cmd)
        self.quit()

def donothing(*e):
  pass
if __name__ == '__main__':

    delnetuse = "net use u: /del"
    os.system(delnetuse)
    root = Tk()
    root.title('作业客户端')
    # root.iconbitmap('2.ico')

    width = 240
    height = 160
    Label(root,bg='#B9D3EE',text=" 版本：V1.0",fg='#27408B').pack(side = "bottom")
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)  # 居中对齐
    root['background']='#B9D3EE'
    # root.protocol("WM_DELETE_WINDOW", donothing)
    root.resizable(False, False)
    # root.overrideredirect(True)
    page1 = LoginPage()
    page1['background']='#B9D3EE'
    root.mainloop()
