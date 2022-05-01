# Hello world!
Python3 (flask)のバックエンドテンプレートです。
また、想定する環境は以下の通りです。  
・API server : heroku (https://www.heroku.com)  
・CD/CI hook : githubもしくはgitlab (https://gitlab.com)  
・auth server: Google Firebase Auth (https://firebase.google.com/)  
各サーバーのセットアップは以下のチュートリアルに従ってください。

# flask on Python3の環境構築
## TL;DR
homebrew経由でpython3をインストールしたのち、python3からpipをインストール
brew > python3 > curlでget-pipをダウンロード > pythonでget-pip展開

## Linux/Macにおけるインストール

1. homebrew, python3, pipをインストール  
@ Terminalを開き、以下のコマンドを実行  

``` bash.sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python
export PATH=/usr/local/bin:$PATH
source ~/.bash_profile
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```
2. pipの環境構築  
@ Terminalを開き、README.md(このファイル)があるディレクトリ（Root directoryと言います）まで`cd`を使って移動  
@以下のコマンドを実行

``` bash.sh
pip install -r requirements.txt
```

## Windowsにおけるインストール

1. python3を[インストール](https://pythonlinks.python.jp/ja/index.html "Install Python3")

python3を[こちら](https://pythonlinks.python.jp/ja/index.html "Install Python3")からインストール

2. pipのインストール
コマンドプロンプトもしくはPowershellから以下のコマンドを実行

``` cmd
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
py get-pip.py
```

3. pipの環境構築
@ Terminalを開き、README.md(このファイル)があるディレクトリ（Root directoryと言います）まで`cd`を使って移動  
@　以下のコマンドを実行

``` bash.sh
pip install -r requirements.txt
```
# サーバーをローカルホストで立ち上げる
@ Terminal(or cmd)を開き、README.md(このファイル)があるディレクトリ（Root directoryと言います）まで`cd`を使って移動  
@　以下のコマンドを実行

``` bash.sh
python3 app.py
```
もしくは
``` bash.sh
python app.py
```

ちなみに`flask.run`は相対パスの関係で使用するとModule Errorが大量に出るので使わない。  
（Deployしたときにパスを通さないとエラーが出る）

# デプロイする
## Gitのセットアップ
1. 新しいプロジェクトに全ファイルをコピー
2. 以下のコードで初期化し、必要であれば既存のレポジトリとつなげる
```
git init
git add .
git commit -m "first commit"
```

## Herokuアプリの作成
1. ログイン（作成していない場合はアカウントを作成してください）
```
heroku login
```
! もしブラウザが開くがログインできない場合は
```
heroku login --interactive
```
でログインしてください

2. アプリの作成
```
heroku create
```

3. Pushしてデプロイ
```
git push heroku master
```

超簡単。


# [Optional] IDEのエラー

--> If you stack on the error of not found module error on vscode(pyanalysis)

1. Search "python.analysis.extraPaths" on setting.json
2. Add extrapath



# [Optional] DBサーバー(postgre SQLサーバー)をローカルで立ち上げる
この環境では、localhostではSQL lite、デプロイ先のHerokuではPSQLを立ち上げる用作られています。  
（両インターフェースはSQL Alchemyのormでラップされています）  
ただ、もしローカルでPSQLをテストしたい場合は以下のコードで実行してください。  

```
psql -h "127.0.0.1" -p 5432 -U "<uname>" -d "postgres"
\q
CREATE DATABASE "db.postgresql" OWNER "<uname>";

postgres -D /usr/local/var/postgres

brew services start postgresql

brew services stop postgresql

psql -l

flask db init
flask db migrate
flask db upgrade
``