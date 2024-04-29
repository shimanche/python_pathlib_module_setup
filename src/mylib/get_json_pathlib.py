from pathlib import Path

def read_json_as_str(json_file):
    """
    指定されたJSONファイルを文字列として読み取り、その内容を返す関数。

    Args:
        json_file (str): JSONファイルのパス。

    Returns:
        str: JSONファイルの中身を文字列として返す。
    """
    json_file_path = Path(json_file)
    with json_file_path.open() as f:
        json_str = f.read()
    return json_str


if __name__ == "__main__":
    root_path = Path(__file__).parent.parent.parent
    images_path = "static/json_data/modified_coordinate_values_json.json"
    directory_path = root_path / images_path
    print(">>directory_path",directory_path)
    json_str = read_json_as_str(directory_path)
    print(json_str)
