from pathlib import Path

def get_sorted_files(directory, pattern="*"):
    """
    指定されたディレクトリからファイルを取得する関数。

    Args:
        directory (str): ディレクトリのパス。
        pattern (str): ファイル名のパターン。デフォルトは全てのファイルを取得する設定。

    Returns:
        list: ファイルのパスのリスト。
    """
    directory_path = Path(directory)
    files = directory_path.glob(pattern)
    file_list = [file.name for file in files if file.is_file()]
    sorted_fileList = sorted(file_list)  # ファイル名を名前順にソート    
    return sorted_fileList
  
def get_sorted_filenames(directory, pattern="*"):
    """
    指定されたディレクトリからファイル名を取得し、拡張子を除いたファイル名のリストを名前順にソートして返す関数。

    Args:
        directory (str): ディレクトリのパス。
        pattern (str): ファイル名のパターン。デフォルトは全てのファイルを取得する設定。

    Returns:
        list: 拡張子を除いたファイル名のリストを名前順にソートしたもの。
    """
    directory_path = Path(directory)
    files = directory_path.glob(pattern)
    filenames = [file.stem for file in files if file.is_file()]  # .stemで拡張子を除いたファイル名を取得
    sorted_filenames = sorted(filenames)  # ファイル名を名前順にソート
    return sorted_filenames

if __name__ == "__main__":
    root_path = Path(__file__).parent.parent.parent
    images_path = "static/images"
    directory_path = root_path / images_path
    print(">>directory_path",directory_path)
    files = get_sorted_files(directory_path, "*.jpg")  # .jpgファイルを取得する例
    files = get_sorted_filenames(directory_path, "*.jpg")  # .jpgファイルを取得する例

    for file in files:
        print(file)
