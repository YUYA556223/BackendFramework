# What is this?
データベースを制御するためのディレクトリです。  

# 環境について
テスト環境：SQLite（ファイルとして保存されるので確認しやすい）  
本番環境（heroku）：PostgreSQL  
ORM：SQL Alchemy

# ディレクトリ構成について
### models
実際に保存されるデータモデルが入っています。以下のサンプルコードに従ってください。  

```
from sqlalchemy import Column, Integer, String, Sequence
from db.models import DB


class <modulename>Model(DB.Base):
    __tablename__ = __name__
    # ID (Primary key)
    id = Column(String, primary_key=True)
```

・modulenameに自身のファイル名（大文字スタート）を入れてください  
・DB.Baseを継承してください  
・__tablename__にはデフォルトで自身のクラス名が入るようになっています。  
　（もちろんクラスの名前は同じ名前を使わないようにしてください。）  
・カラムはColumnインスタンスで定義してください。  
・デフォルトの環境でdata.dbにデータが保存されます。

### handlers
データベースのハンドリングを行います。  
外部から参照するのはこの部分です。  
プログラマ・フレンドリーなコード群を提供してください。（そのままmodelを返す、というようなことはせず、内部を展開し、プログラマが扱いやすいデータ群を提供してください。）

### [optional]clsmodels
db.handlerにおいて、ネストしたクラスを返したい場合に使用してください。  
例えば、単にIDを返すだけでなく、ユーザーに関連する多くの情報を返したい場合などがこれに該当します。

# ルール
## 正規化を忘れない
modelは第3正規形に直してください。最低でも第1正規形にはしてください。  
その代わりhandlerで扱い形に整形し、プログラマが扱いやすい形に直します。

## modelsには処理を書かない
modelsにはデータベースの定義のみを書くようにしてください。  
処理部分はdb.handlersに記載してください。

## handlersには全体の処理を書かない
全体の処理を書くのはルート内のhandlerです。db.handlerにはデータベースの処理のみ記載してください。

## clsmodelsは正規化されていないモデルを格納してOK
加工された後のデータですので、ネストしたクラスなどで問題ありません。  
プログラマ・フレンドリーなデータ構造を定義してください。