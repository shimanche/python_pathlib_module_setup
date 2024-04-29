# python_pathlib_module_setup
## 仮想環境の構築
 python3 -m venv venv
 source venv/bin/activate

# モジュールのパスの通し方
## setup.pyの作成
  自作モジュールのパスを通すもの。
  setup.py内に自作モジュールとして読み込みたいパスを記述する
##　pip install -e .
  pip install -e .を実行して、setup.pyを有効化する（多分）

##　使用例
　how_to_pathlib.pyの記述の通り、
  from mylib.get_json_pathlib import read_json_as_str
  として、モジュールを読み込むことができる。
  setup.pyに、srcを起点として、
      package_data={
        "get_images": ["*.py, component/*.py"],
        "mylib": ["*.py"]
    },
  を記述しているため。

#　フォルダパスの通し方
  ## 関数の引数にディレクトリのパスを渡す
  　 read_json_as_str(directory_path)のように引数にディレクトリのパスを渡すような関数にしておく
    （関数内にディレクトリのパスをハードコーディングしない）
  ## pathlibを使ったディレクトリの設定方法
    if __name__ == '__main__':
      root_path = Path(__file__).parent.parent.parent
      images_path = "static/json_data/modified_coordinate_values_json.json"
      directory_path = root_path / images_path
    のようにして、一旦実行したいコードからparentで遡ってroot_pathを取得する。
    続いて、目的のディレクトリのパスをルートから記述する。
    それらをpathlibの機能で結合する。
    このようにして、絶対パス（directory_path）を生成して、
    関数に絶対パスを引数として渡す。read_json_as_str(directory_path)
    このようにすることで、この関数を実行したいコードのディレクトリを起点として、
    ルートを設定（変更）するだけで良い。

