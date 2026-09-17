from flask import Flask, render_template, request
import pyautogui as auto

from datetime import date


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/commitar", methods = ['POST'])
def commitar():
    hoje = date.today().strftime("%d/%m/%Y")
    repositorio = None
    if request.method == "POST":
        repositorio = request.form.get("repositorio","")
    if repositorio:
        auto.PAUSE = 1
        auto.hotkey("win","r")
        auto.write("cmd")
        auto.press("enter")
        auto.write(f"cd {repositorio}")
        auto.press("enter")
        auto.write("git add .")
        auto.press("enter")
        auto.write(f'git commit -m "Commit do dia {hoje}"')
        auto.press("enter")
        auto.write("git push")
        auto.press("enter")
        auto.sleep(3)
        auto.write("exit")
        auto.press("enter")
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)