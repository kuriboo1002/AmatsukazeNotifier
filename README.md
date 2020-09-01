
# AmatsukazeNotifier

![Screenshot](https://user-images.githubusercontent.com/39271166/88943606-a877c300-d2c6-11ea-8323-7914f78f50e0.png)

Amatsukaze から LINE や Twitter（ツイート・DM）に通知を送れるツールです。

## About・Feature

[Amatsukaze](https://github.com/nekopanda/Amatsukaze) のバッチファイル実行機能を使い、


- LINE (LINE Notify)
- Twitter (ツイート)
- Twitter (ダイレクトメッセージ)

に Amatsukaze の各通知を送信できる Python 製ツールです。tsukumijima氏の[EDCBNotifier](https://github.com/tsukumijima/EDCBNotifier)を元に制作しました。

Amatsukaze のバッチファイル実行機能を利用しているため、変換処理の実行前後に通知を送る事が可能です。

たとえば、Amatsukaze でエンコードが開始された旨を通知したり、実行結果の一部の情報を送信するといった事が可能です。

LINE への通知は LINE Notify を使って送信します。  
LINE Notify はアプリケーションからの通知を指定したユーザーやグループで受信することができるサービスです。  
通知メッセージは LINE Notify の公式アカウントから受信できます（一度使ってみたほうが早いかも）。

Twitter への通知はツイートでの通知に加え、ダイレクトメッセージでの送信も可能です。  
ダイレクトメッセージは自分宛てに送ることも、DM を送信できる他のアカウントに送ることもできます。  
たとえば、録画通知用の Twitter アカウントを作ってメインアカウントと相互フォローになり、録画通知用のアカウントからメインアカウント宛てに通知を送ることもできます。

通知できるイベントは、

- 変換を開始したとき (実行前_AmatsukazeNotifier.bat が実行されたとき)
- 変換が成功したとき (処理完了状態で実行後_AmatsukazeNotifier.bat が実行されたとき)
- 変換が失敗したとき (処理失敗状態で実行後_AmatsukazeNotifier.bat が実行されたとき)

の 3つです。

それぞれのイベントは、個別に通知するかどうかを設定できます。  
EDCBNotifierを導入している場合は、録画終了の通知後ほぼノータイムで変換開始の通知が送信されることになるので、頻繁に送られて煩いという場合には変換開始のイベントだけ通知しないようにすることも可能です。

通知するメッセージは 3 つのイベントごとに自由に変更できます。  
設定ファイルは Python スクリプトなので、Python の知識があればメッセージをより高度にカスタマイズすることもできそうです。  
基本的にはEDCBNotifierに準拠したマクロとなっていますが、AmatsukazeNotifierでは使えないものが多くある他、独自のマクロもあります。

## Setup

### 1. ダウンロード・配置

<img src="https://user-images.githubusercontent.com/39271166/88381578-a357d700-cde1-11ea-9f5a-12f559af093a.png" width="400px">

 \[Code] メニュー内の \[Download Zip] をクリックし、AmatsukazeNotifier をダウンロードします。  
または、[こちら](https://github.com/nukemiri/AmatsukazeNotifier/archive/master.zip) のリンクからでもダウンロードできます。

ダウンロードできたら解凍し、

- EDCBNotifier フォルダ
- bat

を Amatsukaze 本体 (Amatsukaze.vbs) があるフォルダに配置します。  
また、requirements.txt は今後の作業で利用するので、取っておいてください。

### 2. Python のインストール

EDCBNotifier の実行には Python (Python3) が必要です 。動作確認は Python 3.7 系と Python 3.8 系で行っています。

すでに Python3 がインストールされている場合はスキップしても構いませんが、**すでに Python2 がインストールされている場合は別途 Python3 をインストールしてください。**  
（Python2 と Python3 は半分別物で、このうち Python2 は 2020 年 1 月でサポートが終了しています）

![Screenshot](https://user-images.githubusercontent.com/39271166/88384104-c042d900-cde6-11ea-89f3-a1341b5d998e.png)

[非公式 Python ダウンロードリンク](https://pythonlinks.python.jp/ja/index.html) から、Python3 のインストーラーをダウンロードします。  
とくにこだわりがないのであれば、**一番上にある Windows (64bit) 用 Python 3.8 の最新版 ( 2020 年 7 月現在の最新は 3.8.5 ) をダウンロードしてください。**  

[Python 公式サイト](https://www.python.org/downloads/windows/) からもダウンロードできますが、わかりにくいので前述のサイトからダウンロードすることをおすすめします。  
Python 公式サイトにも大きいダウンロードボタンがありますが、これは罠です…（OS のビットに関わらず 32bit の インストーラーがダウンロードされる）  

もし OS が 32bit の方は Windows (32bit) 用をダウンロードしてください（ほとんどいないと思うけど…）。  
**Windows10 では Microsoft Store からもインストールすることができますが、安定していない上にストアアプリの制限の影響で正常に動かないことがあるため、非推奨です。**

<img src="https://user-images.githubusercontent.com/39271166/88402926-be890d80-ce06-11ea-87fd-59c80cbd046e.png" width="600px">

ダウンロードが終わったらインストーラーを実行します。
 \[Install Now] と \[Custom Install] がありますが、 \[Custom Install] の方をクリックしてください。  
このとき、**必ず \[Add Python 3.8 to PATH] にチェックを入れてから進んでください。**

 \[Option Features] は特にこだわりがなければそのまま進みます。  

<img src="https://user-images.githubusercontent.com/39271166/88402933-c3e65800-ce06-11ea-912f-e46151231e97.png" width="600px">

 \[Advanced Options] は ** \[Install for all users] にチェックを入れます**（これで AppData 以下に配置されなくなる）。  
デフォルトでは AppData 以下にユーザーインストールする設定になっていますが、他のユーザーから見れないほかパスが長くなっていろいろ面倒だと思うので、私はおすすめしません。  

 \[Install for all users] にチェックを入れると \[Customize install location] が C:\Program Files\Python38 になりますが、**これも C:\Program Files 以外に変更します。**  
これは C:\Program Files 以下にインストールしてしまうと pip でのライブラリのインストールに毎回管理者権限を求められてしまい面倒なためです。  
私は C:\Applications\Python\Python3.8 にインストールしていますが、とりあえず C:\Program Files 以下と C:\Users 以下でなければよいでしょう（別バージョンを入れることも考え Python\Python3.8 のような階層にしておくのがおすすめ）。

 \[Install] をクリックするとインストールが開始されます。  
 \[Setup was successful] という画面が表示されればインストール完了です。  
試しにコマンドプロンプトや PowerShell から `python -V` と実行してみましょう。

### 3. 依存ライブラリのインストール

EDCBNotifier が必要とする colorama・jaconv・requests・twitter の各ライブラリを pip でインストールします。  

**コマンドプロンプトや PowerShell を開き、`pip install -r (ダウンロードした EDCBNotifier\requirements.txt)` と実行します。**  
または単に `pip install -r colorama jaconv requests twitter` としても構いません。

エラーなくインストールできれば OK です。

### 4. 設定ファイルの作成

Amatsukaze 内に配置した AmatsukazeNotifier フォルダ内の config.default.py は、設定ファイルのひな形になるファイルです。  
config.default.py を config.py にコピーしてください（コピーしておかないと設定が読み込めず動きません）。

リネームでもかまいませんが、設定をミスったときのために config.default.py は取っておくことを推奨します。

### 5. Amatsukaze の再起動

Amatsukaze/bat/ に追加した .bat ファイルはAmatsukazeに自動で認識され、頭に "実行前_"と付くものは実行前バッチとして、"実行後_"と付くものは実行後バッチとして登録が可能になります。
プロファイルタブから使用するプロファイルを選んで実行前バッチと実行後バッチの項目に 実行前_AmatsukazeNotifier.bat と 実行後_AmatsukazeNotifier.bat を登録して適用してください。


これでインストールは完了です。

## Usage

AmatsukazeNotifier の設定は AmatsukazeNotifier フォルダ内の config.py にて行います。  
LINE Notify へ通知する場合は LINE Notify のアクセストークンが、Twitter へ通知する場合は Twitter API アプリが必須になります。  
LINE Notify のアクセストークンの作成には LINE へのログインが、Twitter API アプリの作成には Twitter の開発者アカウントがそれぞれ必要です。 

### 1. 設定

config.py を<u>文字コード UTF-8 (BOM 無し)・改行コード LF で編集・保存できるエディタで</u>編集します。  
メモ帳は Windows10 1903 以前のものでは UTF-8 (BOM 無し)・LF で保存できなかったり、またシンタックスハイライトもないため避けてください。  
できれば VSCode などのシンタックスハイライトや lint のあるエディタでの編集を推奨します。

**通知タイプ** (NOTIFY_TYPE) では、LINE (LINE Notify)・Tweet (ツイート)・DirectMessage (ダイレクトメッセージ) から通知するものを選択します。  
デフォルト … 全てに通知する (`['LINE', 'Tweet', 'DirectMessage']`)

**通知を行うイベント** (NOTIFY_EVENT) では、通知するイベントのオン・オフを設定できます。  
ここで設定したイベントだけが通知されます。たとえば頻度の多い PostNotify だけ通知しない設定も可能です。  
デフォルト … 全てオン (`['PostEncStart', 'PostEncSuccess', 'PostEncFailed']`)

**通知時に同時に送信する画像** (NOTIFY_IMAGE) では、通知時に同時に送信する画像を指定できます。   
None に設定した場合は画像を送信しません。画像サイズが大きすぎると送れない場合があるので注意してください（使う機会がない気も…）  
デフォルト … 画像を送信しない (`None`)

**ダイレクトメッセージの宛先** (NOTIFY_DIRECTMESSAGE_TO) では、ダイレクトメッセージで通知する場合に通知を送るアカウントをスクリーンネーム (ID) で指定します。  
@ はつけないでください。予め宛先のアカウントと DM が送信できる状態になっていないと送れません。None に設定した場合は自分宛てに送信します。  
デフォルト … 自分宛てに送信する (`None`)

**ログをファイルに保存するか** (NOTIFY_LOG) では、ログをファイルに保存（出力）するかどうかを設定します。  
True に設定した場合は、ログを config.py と同じフォルダの EDCBNotifier.log に保存します。前回のログは上書きされます。また、コンソールへログを出力しなくなります。  
False に設定した場合は、ログを保存しません。通常通りコンソールにログを出力します。  
デフォルト … ログをファイルに保存しない (`False`)

このほか、config.py 内のコメントも参考にしてください。   
保存する際は 文字コード UTF-8 (BOM 無し)・改行コード LF で保存します（ CR+LF になったり BOM 付きにならないように注意）。

### 2. 通知するメッセージを編集する

通知イベントごとにメッセージを編集できます。  
通知するメッセージの設定は config.py の \[メッセージ] セクションにあります。

基本的にマクロの形式は EDCBNotifier に準拠していますが、使えないものが多くある他、独自のマクロもあります。
また、実行後バッチのみで使用可能なマクロもあります

使用可能マクロ一覧

- \$HashTag\$ … 放送局名から取得したハッシュタグ (ハッシュタグは utils.py の get_hashtag() メソッドで定義) 
- \$NotifyName\$ … \$NofityID\$ から取得した更新通知タイプ（\$NofityID\$ = 1 … EPGデータ更新 2 … 予約情報更新 3 … 録画結果情報更新）
- \$ServiceNameHankaku\$ … \$ServiceName\$（放送局名）の英数字を半角に変換したもの
- \$TitleHankaku\$ … \$Title\$（番組タイトル）の英数字を半角に変換したもの
- \$Title2Hankaku\$ … \$Title2\$（番組タイトル・[]で囲まれている部分を削除したもの）の英数字を半角に変換したもの
- \$TimeYYYY\$ … 実行時刻の上2桁付き西暦年 (ex: 2020 (年))  \$TimeYY\$ … 実行時刻の上2桁なし西暦年 (ex: 20 (年))
- \$TimeMM\$ … 実行時刻の2桁固定の月 (ex: 07 (月))  \$TimeM\$ … 実行時刻の月 (ex: 7 (月))
- \$TimeDD\$ … 実行時刻の2桁固定の日 (ex: 09 (日))  \$TimeD\$ … 実行時刻の日 (ex: 9 (日))
- \$TimeW\$ … 実行時刻の曜日 (ex: 火 (曜日))
- \$TimeHH\$ … 実行時刻の2桁固定の時 (24時間) (ex: 06 (時))  \$TimeH\$ … 実行時刻の日 (ex: 6 (時))
- \$TimeII\$ … 実行時刻の2桁固定の分 (ex: 08 (分))  \$TimeI\$ … 実行時刻の分 (ex: 8 (分))
- \$TimeSS\$ … 実行時刻の2桁固定の秒 (ex: 02 (秒))  \$TimeS\$ … 実行時刻の分 (ex: 2 (秒))

Python の辞書 (dict) 形式で格納しているので、改行を入れる場合は文字列内に \n と入力してください。文字列は + で連結できます。  

また、PostEncSuccess と PostEncFailed 用にエラーメッセージを設定できます。

Amatsukazeからエラーが出力された際には[エラー: DRCSマッピングのない文字 127件]や[エラー: キャンセルされました]の様な文字列をメッセージの最後に追加します。
エラーがなかった場合には追加されません。
このエラーメッセージも config.py の ErrorMessage でマクロで自由にカスタマイズする事が可能です。
エラーメッセージを使用しない場合は ErrorMessage = ''のように何も入力しないでください。

デフォルトのように絵文字も送信できます（ただ新しい絵文字だと端末側で表示できなかったりするので注意）。  
カスタマイズしたい方は、お好みの通知メッセージへ変更してみてください。

### 3. LINE Notify

LINE Notify へ通知しない場合は必要ありませんが、後述する Twitter の開発者アカウントを作成する手順よりもはるかに簡単なので、やっておくことをおすすめします（さほど手間もかかりません）。

[LINE Notify](https://notify-bot.line.me/ja/) にアクセスし、右上の \[ログイン] から LINE へログインします（いつも使っているアカウントで構いません）。  
ログインできたら、右上のメニューから \[マイページ] に移動します。

![Screenshot](https://user-images.githubusercontent.com/39271166/88371969-06407280-cdd0-11ea-9e70-ed5b796d79e0.png)

下の方にある「アクセストークンの発行(開発者向け)」へ行き、 \[トークンを発行する] をクリックします。

![Screenshot](https://user-images.githubusercontent.com/39271166/88370184-81a02500-cdcc-11ea-8147-772f3ceb9662.png)

トークン名は LINE Notify で通知が送られてきたときに \[EDCBNotifier] のように付加される文字列です（ LINE Notify 全体でユニークである必要はないらしい）。  
通知を送信するトークルームは \[1:1 で LINE Notify から通知を受ける] か、任意のグループ LINE を選択してください。  
ここでは「1:1 で LINE Notify から通知を受ける」（現在ログインしているアカウントに届く）を選択します。 

![Screenshot](https://user-images.githubusercontent.com/39271166/88371432-fbd1a900-cdce-11ea-8e9f-2067360c32b9.png)

 \[発行する] をクリックするとアクセストークンが発行されるので、 \[コピー] をクリックしてクリップボードにコピーします。  
アクセストークンはこの画面を閉じると二度と表示されない（一度解除し同じ内容でもう一度発行することはできるがアクセストークンは変わる）ので、どこかにメモしておくと良いでしょう。

![Screenshot](https://user-images.githubusercontent.com/39271166/88371444-fecc9980-cdce-11ea-8293-b9a8bf765422.png)

画面を閉じると LINE Notify と設定したトークルームが連携されているはずです。

最後に config.py を開き、先程クリップボードにコピーしたアクセストークンを \[LINE Notify] セクションの **LINE_ACCESS_TOKEN** に設定します。

これで、LINE Notify に通知を送信できる状態になりました！ 


### 4. Twitter (ツイート・ダイレクトメッセージ)

Twitter へ通知する場合は Twitter へ開発者登録を申請し、開発者アカウントを取得しておく必要があります（Twitter Developer アプリケーションの作成に Twitter の開発者アカウントが必要なため）。  
ただ、悪用する人が多かったため今から登録するのはちょっと面倒になっています。これでも最近若干緩和されたらしいけど…

さすがに手順までは説明しきれないので、開発者申請の手順が解説されている記事を貼っておきます（[記事1](https://digitalnavi.net/internet/3072/)・[記事2](https://www.itti.jp/web-direction/how-to-apply-for-twitter-api/)）。  

すでにツイートさせたいアカウントとは別のアカウントで開発者アカウントになっている場合、必ずしも別途録画通知用の Bot アカウントを開発者アカウントにする必要はありません。  
Twitter API を使うためには後述する Consumer Key・Consumer Secret・Access Token・Access Token Secret の 4 つが必要ですが、このうち Twitter Developers でアプリ作成後に生成できる Access Token・Access Token Secret は開発者アカウントをしたアカウントのものが表示されます。  
裏を返せば、予め開発者アカウントで Consumer Key・Consumer Secret を作成・取得し、ツイートさせたい Twitter アカウントとアプリ連携して Access Token・Access Token Secret が取得できれば、開発者登録をしたアカウント以外でも録画通知用のアカウントにできる、とも言えます。

EDCBNotifierの作者tsukumijima氏のツールである、[Twitter API のアクセストークンを確認するやつ](https://tools.tsukumijima.net/twittertoken-viewer/) を使うと、EDCBNotifier のようなアプリ連携を実装していないツールでも Access Token・Access Token Secret を取得できます（極論、これを使わなくても作成した Consumer Key・Consumer Secret で録画通知用のアカウントとアプリ連携して Access Token・Access Token Secret を取得できれば可能です）。  

[Twitter Developers](https://developer.twitter.com/en/apps) にアクセスし、右上の \[Create App] から Twitter Developer アプリケーションの作成画面に移動します（ここで言う Twitter Developer アプリケーション（以下 Twitter API アプリ）は Twitter API を使うプロジェクトのような意味です）。  
Twitter API アプリを作成すると、Twitter API を使うために必要な Consumer Key・Consumer Secret を取得できます。   
すでに Twitter API アプリを作成している場合は飛ばすこともできますが、via が被るので新しく作ってもいいと思います。開発者登録のときとは異なり、審査はありません。

![ScreenShot](https://user-images.githubusercontent.com/39271166/88845529-444df400-d21f-11ea-89db-4243e077e622.png)

#### App name（必須・重複不可らしい）

ここの名前がツイートの via として表示されます。  
いわゆる「独自 via 」と呼ばれるものです。後で変えることもできるので、好きな via にしましょう。

（例）EDCBNotifier@（自分の TwitterID ）  
（例）Twitter for （自分の Twitter 名）  

#### Application description（必須）

（例）EDCBNotifier@example から録画通知をツイートするためのアプリケーションです。

#### Website URL（必須）

利用用途的に自分以外は見ない部分なので、適当に設定しておきましょう。  
ただし、http://127.0.0.1/ は設定できないようです。

（例）https://example.com/  
（例）https://(自分のサイトのドメイン)/

#### Enable Sign in with Twitter

開発者登録をしたアカウント以外で利用する場合はチェックを入れてください。

#### Callback URLs

開発者登録をしたアカウント以外で利用する場合、アプリ連携をした後にリダイレクトされるコールバック URL を指定してください（複数設定できます）。  
[Twitter API のアクセストークンを確認するやつ](https://tools.tsukumijima.net/twittertoken-viewer/) を使う場合は `https://tools.tsukumijima.net/twittertoken-viewer/` を設定します。

#### Terms of service URL

無記入で OK です。

#### Privacy policy URL

無記入で OK です。

#### Organization name

無記入で OK です。

#### Organization website URL

無記入で OK です。

#### Tell us how this app will be used（必須）  

（例）このアプリケーションは、EDCBNotifier から通知をツイートするためのアプリケーションです。  
　　　このアプリケーションは、テレビの録画予約の追加・変更、録画の開始・終了をツイートやダイレクトメッセージで通知します。

#### （英語・こちらをコピペ）

（例）This application is for tweeting notifications from EDCBNotifier.   
　　　This application notifies you of the addition/change of TV recording reservation and the start/end of recording by tweet or directmessage.

記入し終えたら \[Create] をクリックし、Twitter API アプリを作成します。

ダイレクトメッセージを送信するため Permissions タブに移動し、\[Edit] をクリックします。

![ScreenShot](https://user-images.githubusercontent.com/39271166/88842998-5f1e6980-d21b-11ea-93ec-80e9caeb2754.png)

**Access permission** を **Read, write, and Direct Messages** に設定し、\[Save] で保存します。  
こうすることでツイートの読み取り・ツイートの書き込みなどに加え、ダイレクトメッセージを送信できるようになります。  
Permissions を変更すると今までに取得した Access Token・Access Token Secret が無効になります。注意してください。

![ScreenShot](https://user-images.githubusercontent.com/39271166/88842886-2f6f6180-d21b-11ea-8265-b2a67653e674.png)

Keys and tokens タブに移動し、API Key と API Key Secret をクリップボードにコピーします。  
API Key が Consumer Key 、API Key Secret が Consumer Secret にあたります。  

![ScreenShot](https://user-images.githubusercontent.com/39271166/88843951-de606d00-d21c-11ea-8b77-9ecdad694470.png)

開発者登録したアカウントで利用する場合は、**Access token & access token secret** の横の \[Generate]をクリックし、Access Token・Access Token Secret を生成します。  
Access Token・Access Token Secret が表示されるので、クリップボードにコピーします。
このとき、Access Token・Access Token Secret は一度だけ表示されます。どこかにメモしておくとよいでしょう。  

開発者登録したアカウント以外で利用する場合は、自力でアプリ連携して Access Token・Access Token Secret を取得するか、録画通知用にしたいアカウントにログインした状態で [Twitter API のアクセストークンを確認するやつ](https://tools.tsukumijima.net/twittertoken-viewer/) に Consumer Key・Consumer Secret を入力し、Access Token・Access Token Secret をクリップボードにコピーしてください。

最後に config.py を開き、先程クリップボードにコピーしたアクセストークン等を \[Twitter API] セクションの **TWITTER_CONSUMER_KEY・TWITTER_CONSUMER_SECRET・TWITTER_ACCESS_TOKEN・TWITTER_ACCESS_TOKEN_SECRET** にそれぞれ設定します。

これで Twitter にツイートやダイレクトメッセージで通知を送信できる状態になりました！ 


これで設定は完了です！お疲れさまでした！   
なにか不具合や要望などあれば [Issues](https://github.com/nukemiri/AmatsukazeNotifier/issues) か [Twitter](https://twitter.com/mochiken0625) までお願いします。 

## License
[MIT Licence](LICENSE.txt)
