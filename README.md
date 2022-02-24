# mineSVLC
マインクラフトサーバー作成補助ツール  
  
製作途中のためバグ多いです  
[ダウンロード](https://github.com/tikitiki0370/mineSVLC/releases/tag/v0.0.2)
何かありましたらtwitterまで  
[@niwaniwa_tikinn](https://twitter.com/niwaniwa_tikinn)

# exeファイルから利用する際の注意点
ダウンロード数が少ないためchromeにダウンロードを止められる場合があります(このファイルは一般的に...)  
矢印ボタンから継続をクリックすることでダウンロードすることができます  

証明書をつけてないため初回起動する際windowsにブロックされます(Windows によってpcが...)  
詳細情報をクリックし実行を押すことで実行できます

規約等は同梱のREADME.txtをごらんください

# 使い方  
起動にはMinecraft公式ランチャーを利用することが必要です  

後日記載
## サーバー
サーバーを構築するためのタブになります  
### プロジェクト
**ファイル名**  
> **必須項目**になります  
> 名前に *temp* は利用できません(利用すると消されます)  
  
### サーバー設定
**バージョン**  
> **必須項目**になります  
> すべてのバージョンが表示されますが古いバージョンではサーバープロパティ等の設定が利用できません(ダウンロード自体は可能) 
   
**サーバープロパティ**
> data/sv_propertiesの中のファイルを参照します
> 設定しない場合はコピーしません(サーバー起動時に標準で生成されるものを利用)  
  
**メモリ**
> **必須項目**になります  
> 左側で最低値 右側で最高値を設定します
> batファイルを自動生成する際に利用されます  
  
**jvm引数**
> 現在利用できません  
  
**ワールドファイル**  
> 利用するワールドフォルダを選択します
> 選択したフォルダはworldとしてコピーされます(コピー元は変更されません)  
  
**ops**
> data/opsの中のファイルを参照します  
> 設定しない場合はコピーしません(サーバー起動時に標準で生成されるものを利用)  
  
**whitelist**
> data/whitelistの中のファイルを参照します  
> 設定しない場合はコピーしません(サーバー起動時に標準で生成されるものを利用)  
## プロパティ
プロパティタブの使い方を記載

## ホワイトリスト
ホワイトリストタブの使い方を記載

## OPリスト
OPリストタブの使い方を記載
  
