# What is this?
サーバーへのリクエストが送られてきた場合、リクエストに返答するためのAPIメソッド群を提供するディレクトリです。  

# ルール
## APIは必ずここに記すべし
リクエスト要求を受け付けるモジュールはAPI以下にあり、かつRouteAPIを継承するクラスのみルーティングに追加されます。
## ルートは分割すべし
一つのpyファイル＝一つの役割を意識し、モジュール化を行ってください。
## APIは外部から参照しない
APIは終末ノード（リクエストを送受信するためだけのノード）です。  
循環参照を防ぐため、API内にある関数やクラスは外部モジュールから参照しないでください。  
## 処理内容はhandlerモジュール内に記すべし
APIはユーザーの要求を受け付けるためだけに存在するため、処理内容は全てhandlerに記し、それをAPI内から呼び出すようにしてください。  
## クラスはファイル名（役割）+APIにする
例えばAPI/user.pyモジュールを作成した場合、クラスはUserAPIにしてください。  
これはクラスが競合することを防ぐためです。

#  APIモジュールのコード方法
1. 役割を考え、ファイル名をつける
そのAPIは何を司るAPIなのかを考えファイル名をつけます。
2. ベースのコードを書く
・<modulename>にはファイル名が入ります。  
・RouteAPIを継承します。  
・`__router`を定義し、`resister_route()`で作成したルートを登録してください（オーバーライド）。  
・`__router`にルートを定義し、関数を定義してください。  
・サンプルコードは以下の通りです。

```
from api.base import RouteAPI

class <modulename>API(RouteAPI):
    __router = Blueprint(__name__, __name__)

    @staticmethod
    def resister_route():
        return TesterAPI.__router

    @__router.route("/test", methods=['GET'])
    def api_test():
        return "Hello world"
```

# 認証（Auth）を実装する
## Google Firebase Auth
1. Firebase Authに[アクセス](https://console.firebase.google.com/ "Firebase")
2. ログインし、新規アプリを作成します
3. プロジェクトの概要＞アプリ名＞設定アイコン
4. マイアプリからFirebase SDK snippet、構成をクリック
5. firebaseConfig...の部分をコピー

## authでの設定
1. api/auth/_config.pyを開く
2. pyrebase.initialize_app(...)の中にSDK snippetを代入するよう変更

## コードでの実装
以下のコードを実装

```
from flask.globals import request
from flask_cors.decorator import cross_origin

... cls def ...
@__router.route("/auth/test", methods=['GET'])
@cross_origin(supports_credentials=True)
def ...:
    certificate = AuthManager.get_certificate(request)
    return "Mr. " + certificate.user_info.user.displayName

```
[仕組み]  
flaskからきたリクエストをAuthManagerに投げれば、certificateが返ってくるので、このcertificateを使用して認証情報をやりとりします。  
ヘッダーにcredential tokenを入れておくため、option通信（複雑な通信）判定が行われてしまい、@cross_origin(supports_credentials=True)を入れておかないとlocalhostでrequestを飛ばした時怒られます。  
また、デフォルトで100人までのユーザートークンをキャッシュするようになっていますが、_config.pyで変更できます。