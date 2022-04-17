import csv

csv_file = open("./西知多77出力.csv", "r", encoding="ms932", errors="", newline="" )
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
#リスト形式
#f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
#辞書形式
#f = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

def search_str_from_list(lists,s): #リスト内の一つ一つの中身から特定文字列を探す関数
    sear = False
    for li in lists:
        if s in li:
            sear = True
            break
    return(sear)

def search_str_from_listN(lists,s): #リスト内の一つ一つの中身から特定文字列を探しインデックスを返す
    sear = 0
    count = 0
    for li in lists:
        if s in li:
            sear = count
            break
        count += 1
    return(sear)

def body_divider(body): #bodyの要素細分化 Headerとcase要素の分割
    newbody = []
    n = search_str_from_listN(body,"<data>")
    newbody.append(body[1])
    for i in range(n+1,len(body)-1):
        newbody.append(body[i])
    return(newbody)

def csv_writer(fname,body): #csv作成書き込み関数
    #print(body)
    f = open(fname , 'w')
    writer = csv.writer(f, lineterminator='\n')
    for data in body:
        writer.writerow(data)
    #writer.writerow(['test2', '002'])
    f.close()

import os
new_dir_path = './Divided_csv' #作成するディレクトリ名
if not os.path.exists(new_dir_path): #ディレクトリが存在しない場合作成する
    os.mkdir(new_dir_path)
#os.mkdir(new_dir_path)

header = next(f)
#print(header)
dataname = ""
dataname2 = ""
count = 0
body = []
for row in f:
    if search_str_from_list(row,"name="):
        if dataname != "": #データ名があるときつまり、２回目のname発見時以降
            #print("cav_writer")
            #print(body)
            body = body_divider(body)
            csv_writer(new_dir_path+"/"+dataname+".csv",body) #csvの作成と保管
            #break #テスト用

        body = [] #次のbody作成のための初期化
        
        if search_str_from_list(row,"case="): #さらにケースが含まれる場合
            #print(row)
            dataname2 = row[1].split("=")[1] #リストの文字列からタイトルだけ取得    
            dataname = row[0].split("=")[1] + "_" + dataname2 #リストの文字列からタイトルだけ取得
        else:
            dataname = row[0].split("=")[1] #caseがない場合のタイトルはnameそのまま

        #if len(row) > 1: #caseがある場合
        #    print(dataname) #テスト用
    body.append(row)
    print(count)
    #rowはList
    #row[0]で必要な項目を取得することができる
    #print(row)
    count += 1
    #if count == 100:
    #    break