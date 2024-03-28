

import os
#path周り
import glob
from os import listdir
#GUI周り
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog

from time import sleep



import argparse
import sys #exit用
import re #正規表現

#入力のcubeのあるpath
# input_lut_path = "/Volumes/Z-SERVER/00_FeatureFilm/N_ISG_Ikusagami/Grading/BASE_LOOK/240324/for_Zcam_Alexa_MiniLF/LMT/"
input_lut_path = ""

# 書き出すCLFファイルのパス
# output_clf_path = "/Volumes/Z-SERVER/00_FeatureFilm/N_ISG_Ikusagami/Grading/BASE_LOOK/240324/for_Zcam_Alexa_MiniLF/LMT_CLF/"
output_clf_path = ""

home_dir = os.environ['HOME']


def transocde_to_clf():

    print("input_lut_path : " + input_lut_path)
    print("output_clf_path : " + output_clf_path)

    cube_files = [filename for filename in listdir(input_lut_path) if not filename.startswith('.')]

    print(cube_files)
    # files = os.listdir(input_lut_path)
    # files = glob.glob(input_lut_path)
    var.set(0)
    for file in cube_files:
        # if file
        print(file)
        print(output_clf_path)
        filename = file.replace('.cube', '.clf')
        print(filename)
        cmd = "./ociomakeclf " + input_lut_path + file + " " + output_clf_path + filename
        print(cmd)
        os.system(cmd)
        var.set(var.get() + len(cube_files)/100)
        frame3.update_idletasks()

    messagebox.showinfo("Info", "done!!!")


def info_po(button1):
    sleep(0.5)


def exit(button6):
    sys.exit()
    root.destroy()

# フォルダ指定の関数
def dirdialog_clicked1():
    iDir = os.path.abspath(os.path.dirname(home_dir))
    print("iDir : " + iDir)
    global input_lut_path #global変数に代入したい
    input_lut_path = filedialog.askdirectory(initialdir=iDir) + "/"
    print("input_lut_path : " + input_lut_path)
    entry1.set(input_lut_path)

def dirdialog_clicked2():
    iDir = os.path.abspath(os.path.dirname(home_dir))
    print("iDir : " + iDir)
    global output_clf_path #global変数に代入したい
    output_clf_path = filedialog.askdirectory(initialdir=iDir) + "/"
    print("output_clf_path : " + output_clf_path)
    entry2.set(output_clf_path)

# label = tkinter.Label(text="input cube folder path", background='#7fffd4', font=("MSゴシック", "45", "bold"), foreground='#000000')
# label.pack()

def transcode_start():

    transocde_to_clf()



def FileExists(file_path_and_name):
  #return true, or false
  return os.path.exists(file_path_and_name)

# if FileExists(ale_path):
#     pass
# else:
#   print("this ale path is not exist.")
#   print("Exit this program once.")
#   exit()



root = tkinter.Tk()
root.title("clf transcoder")
root.geometry("700x300+350+350")
root.resizable(0, 0)

var = tkinter.IntVar()





# Frame1の作成
frame1 = ttk.Frame(root, padding=10)
frame1.grid(row=0, column=1, sticky=E)

# 「フォルダ参照」ラベルの作成
IDirLabel = ttk.Label(frame1, text="input cube folder path : ", padding=(5, 2))
IDirLabel.pack(side=LEFT)

# 「フォルダ参照」エントリーの作成
entry1 = StringVar()
IDirEntry = ttk.Entry(frame1, textvariable=entry1, width=30)
IDirEntry.pack(side=LEFT)

# 「フォルダ参照」ボタンの作成
IDirButton = ttk.Button(frame1, text="select", command=dirdialog_clicked1)
IDirButton.pack(side=LEFT)

# Frame2の作成
frame2 = ttk.Frame(root, padding=10)
frame2.grid(row=2, column=1, sticky=E)

# 「ファイル参照」ラベルの作成
IFileLabel = ttk.Label(frame2, text="output clf folder path : ", padding=(5, 2))
IFileLabel.pack(side=LEFT)

# 「ファイル参照」エントリーの作成
entry2 = StringVar()
IFileEntry = ttk.Entry(frame2, textvariable=entry2, width=30)
IFileEntry.pack(side=LEFT)

# 「ファイル参照」ボタンの作成
IFileButton = ttk.Button(frame2, text="select", command=dirdialog_clicked2)
IFileButton.pack(side=LEFT)


# label = tkinter.Label(text="output clf folder path", background='#7fffd4', font=("MSゴシック", "45", "bold"), foreground='#000000')
# label.pack()


# Frame3の作成
frame3 = ttk.Frame(root, padding=10)
frame3.grid(row=5,column=1,sticky=W)

button1 = tkinter.Button(frame3,text='cube file transcode to clf', width=30, command=transcode_start)
button1.pack()
button1.bind("<Button-1>",info_po)

pb=ttk.Progressbar(frame3,maximum=100,mode="determinate",variable=var)
pb.pack()


# Frame3の作成
frame4 = ttk.Frame(root, padding=10)
frame4.grid(row=6,column=1,sticky=W)

button6 = tkinter.Button(frame4, text='exit', width=15)
button6.pack()
button6.bind("<Button-1>",exit)

root.mainloop()
