import re


def comments_validator(content):
    # コメントの形式を検証する関数
    # 正規表現を使用して、指定された形式に一致するかどうかをチェックする
    pattern = r"^(M|DM|S|DS)\d{1,2}-\d{1,2}[\s　].*$"
    if not re.match(pattern, content):
        # コンテンツが指定されたパターンに一致しない場合はFalseを返す
        return False
    # 一致する場合はTrueを返す
    return True
