from flask import Flask  # 載入模組
from flask import request
from flask import redirect
from flask import render_template
import json

# 建立Application物件
# 設定靜態檔案的路徑處理 #圖片也是用靜態
app = Flask(
    __name__,
    static_folder="accountLogin",  # 靜態檔案的資料匣名稱
    static_url_path="/"  # 靜態對應的網址名稱改成空白
    #所有的static資料下的檔案,都對應到網址路徑 /static/檔案名稱
)


# 使用get方法處理網站路徑的對應函式
@app.route("/")  # 使用POST方式處理
def index():
    return render_template("index.html")


# 使用get方法處理caluculate按鈕寫法
@app.route("/caluculate", methods=["POST"])
def caluculate():
    #接收 GET的方法Query String
    # math = request.args.get("math", "")
    math=request.form["math"]
    math = int(math)  # 轉為數字
    result = 0
    for n in range(1, math+1):
        result += n
    return render_template("error.html")


app.run(port=3000)
