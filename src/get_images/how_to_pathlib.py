import os
import sys
import json
import pprint
from pathlib import Path
from mylib.get_json_pathlib import read_json_as_str

def how_to_pathlib():
  print(Path(__file__)) #実行したファイル
  print(Path(__file__).parent) #実行したファイルの親ディレクトリ
  print(Path(__file__).parent.parent) #実行したファイルの親ディレクトリ

if __name__ == '__main__':
    how_to_pathlib()
    
    '''setup.pyでmylibのパスを通している。'''
    root_path = Path(__file__).parent.parent.parent
    images_path = "static/json_data/modified_coordinate_values_json.json"
    directory_path = root_path / images_path
    print(">>directory_path",directory_path)
    json_str = read_json_as_str(directory_path)
    print(json_str)
    
    print(" how_to_pathlib  completed !!")