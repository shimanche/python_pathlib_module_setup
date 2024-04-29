import os
import sys
import json
import pprint



def modified_crop_images(filename, strData):
    print("!!__name___ : is     ",__name__)
    print("crop_images(filename, strData)のstrData:type => ",type(strData))
    dictData = json.loads(strData)
    # pprint.pprint({"dictData" : dictData})
    getcwd_path = os.path.join(os.getcwd())    
    pprint.pprint({"関数内のgetcwd_path":getcwd_path})

    if __name__ == '__main__':
        print("こちらは、__name_が__main__の時。つまり直接実行れた時。rootを設定し、rootに一旦戻って、そこから目的のフォルダを探索する")
        root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    else:
        print("こちらは、モジュールで実行れた時。モジュールを呼び出した元の場所から目的のフォルダを探索する")
        root_path = os.path.join(os.getcwd())

    images_path = os.path.join(root_path, "static/images")  
    print("images_path => ",images_path)




if __name__ == '__main__':
    print("★root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))の検証")
    root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    print("sys.pathはモジュールを読み込む際に、どこからモジュールを探しに行くかという起点になる。")
    print("直接起動する場合は相対 import はつかえないのでエラーになります")
    print("--直接pythonでこのコードを実行した場合の-sys.path-----")
    pprint.pprint(sys.path)
    print("このように、実行した場所がsys.pathとなる。")
    print("appendでrootディレクトリを追加してみる（アンチパターンかも）。")    
    sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
    print("-このようにrootディレクトリを追加-append---sys.path-----")
    pprint.pprint(sys.path)
    print("-以上のようにするとimportする際に、絶対パス（rootを起点に）で読み込んでくれる--------")
    print("getcwdは実行された場所に依存する。直接実行した場合はその場所を示す。")
    getcwd_path = os.path.join(os.getcwd())    
    pprint.pprint({"root_path":root_path})    
    pprint.pprint({"getcwd_path":getcwd_path})
    
    filename = "filename"
    str_path = "static/json_data"    
    file_path = os.path.join(root_path,str_path,"modified_coordinate_values_json.json")
    print("with open path =>", file_path)
    with open(file_path, "r") as file:
        data_str = file.read()  # ファイルを文字列として読み込む
    print("type => ",type(data_str))
    # print(data_str)    
    modified_crop_images(filename,data_str)
    print(" get_image_path completed !!")