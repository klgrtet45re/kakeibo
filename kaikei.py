# coding: utf-8

import configparser
import csv
import sys

ini_path = r"C:\Users\home\AppData\Local\Programs\Python\Python311\kaikei.ini"

config = configparser.ConfigParser()
config.read(ini_path)

seikatsu_csv_path = config['CSVPATH']['SEIKATSU']


print("◇生活費入力◇")
print("日付,　分類, 内容, 購入店, 値段, 備考")

x = input()
x = x.replace('；', ';')
print(x)


row  = x.split(';')
if not (len(row) == 5 or len(row) == 6):
     sys.exit()
if row[-1] == "" and (len(row) == 5 or len(row) == 6):
    sys.exit()


print(row)
with open(seikatsu_csv_path, 'a') as f:
    writer = csv.writer(f)
    writer.writerow(row)
