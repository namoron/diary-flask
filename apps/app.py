from flask import (
    Flask,
    current_app,
    flash,
    g,
    redirect,
    render_template,
    url_for,
    request,
    )
import logging
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
# SECRET_KEYを追加
app.config["SECRET_KEY"]  = "2AZSMss3p5QPbcY2hBsJ"
#ログレベルを設定する
app.logger.setLevel(logging.DEBUG)
#リダイレクトを中断しないようにする
app.config["DEBUG_TB_INSTERCEPT_REDIRECTS"]  = False
# DebugToolbarExtension にアプリケーションをセットする

@app.route("/")
def index():
    return "Hello World!"

@app.route("/resister")
def resister():
    #レスポンスオブジェクトを取得する．
    return render_template("resister.html")

@app.route("/resister/complete",methods=["GET","POST"])
def contact_complete():
    if request.method == "POST":
        # form属性を使ってフォームの値を取得
        date = request.form["date"]
        description  = request.form["description"]
        # photo  = request.form["photo"]
        #入力チェック
        is_valid = True
        
        if not date:
            flash("日付は必須です")
            is_valid = False

        if not description:
            flash("内容は必須です")
            is_valid = False

        if not is_valid:
            return redirect(url_for("resister"))
        # メールを送る

        #問い合わせ完了エンドポイントへリダイレクト
        flash("送信しました．")
        return redirect(url_for("contact_complete"))
    return render_template("contact_complete.html")

@app.route("/search",methods=["GET","POST"])
def search():
    return "search"
 