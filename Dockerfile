# ========================================================
# Python/djangoの実行環境構築
# ========================================================
# ベースイメージはPython3の実行環境
#  - ディレクトリ構成
#  root
#    └bin  boot  dev	etc  home  lib	lib64  media  mnt  opt	proc  root  run  sbin  srv  sys  tmp  usr  var
#    usr
#      └bin  games  include  lib  local  sbin  share  src
FROM python:3.7

# 環境変数:Pythonの標準出力/標準エラー出力をバッファにため込まないための設定	
ENV PYTHONUNBUFFERED 1

# パッケージマネージャーの更新
RUN apt-get -y update

# pipの更新
RUN pip install --upgrade pip

# アプリケーション用と静的ファイル用ディレクトリの作成・作業ディレクトリの指定
RUN mkdir -p /code
WORKDIR /code

# 必要パッケージのインストール
COPY requirements.txt /code/
RUN pip install -r requirements.txt

