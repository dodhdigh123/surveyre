from flask import Flask, render_template, request, redirect, url_for, Response
import sys
application = Flask(__name__)
import database
from dashboard import draw_barplot
from dashboard import draw_pie
from dashboard import draw_simple_barplot
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import time
from IPython.display import IFrame




@application.route("/")
def main():
    house_list=database.load_list()
    housegwan_list=database.loadgwan_list()
    return render_template("main.html",house_list = house_list,housegwan_list = housegwan_list)
     # return render_template("main.html")


@application.route("/haeundae")
def haeundae():
    return render_template("haeundae.html")



@application.route("/gwanganri")
def gwanganri():
    return render_template("gwanganri.html")

@application.route("/Dashboard")
def Dashboard():
    gender = request.args.get("gender")
    age = request.args.get("age")
    visit_count = request.args.get("visit_count")
    transport = request.args.get("transport")
    congestion = request.args.get("congestion")
    satisfaction = request.args.get("satisfaction")
    sculpture = request.args.get("sculpture")
    database.save(gender,age,visit_count,transport,congestion,satisfaction,sculpture)
    
    # 데이터 불러오기
    data3 = pd.read_csv("./database.csv", encoding='utf-8', thousands=',') 

    # 그래프 그리기
    fig, axes = plt.subplots(2, 3, figsize=(20, 10))
    draw_pie(data=data3, column='gender', ax=axes[0, 0], title='성별')
    draw_pie(data=data3, column='satisfaction', ax=axes[0, 1], title='먹거리')
    draw_pie(data=data3, column='congestion', ax=axes[0, 2], title='기대')
    draw_simple_barplot(x='age', data=data3, ax=axes[1, 0], title="나이")
    draw_simple_barplot(x='visit_count', data=data3, ax=axes[1, 1], title="방문 횟수")
    draw_simple_barplot(x='transport', data=data3, ax=axes[1, 2], title="교통 수단")
    # 이미지 저장
    fig.savefig("static/img/duu_image.jpeg")
    
    fig, ax = plt.subplots(figsize=(20, 10))
    draw_pie(data=data3, column='sculpture', ax=ax, title='A/B 테스트')
    fig.savefig("static/img/ab_test.jpeg")
    return render_template("Dashboard.html")

@application.route("/Dashboardgwan")

def Dashboardgwan():
    gender = request.args.get("gender")
    age = request.args.get("age")
    visit_count = request.args.get("visit_count")
    transport = request.args.get("transport")
    congestion = request.args.get("congestion")
    satisfaction = request.args.get("satisfaction")
    sculpture = request.args.get("sculpture")
    database.savegwan(gender,age,visit_count,transport,congestion,satisfaction,sculpture)
    
    # 데이터 불러오기
    data4 = pd.read_csv("./databasegwan.csv", encoding='utf-8', thousands=',') 

    # 그래프 그리기
    fig, axes = plt.subplots(2, 3, figsize=(20, 10))
    draw_pie(data=data4, column='gender', ax=axes[0, 0], title='성별')
    draw_pie(data=data4, column='satisfaction', ax=axes[0, 1], title='먹거리')
    draw_pie(data=data4, column='congestion', ax=axes[0, 2], title='기대')
    draw_simple_barplot(x='age', data=data4, ax=axes[1, 0], title="나이")
    draw_simple_barplot(x='visit_count', data=data4, ax=axes[1, 1], title="방문 횟수")
    draw_simple_barplot(x='transport', data=data4, ax=axes[1, 2], title="교통 수단")
    # 이미지 저장
    fig.savefig("static/img/duugwan_image.jpeg")
    
    fig, ax = plt.subplots(figsize=(20, 10))
    draw_pie(data=data4, column='sculpture', ax=ax, title='A/B 테스트')
    fig.savefig("static/img/ab_testgwan.jpeg")
    return render_template("Dashboardgwan.html")


@application.route("/Dashboardshow")
def Dashboardshow():
    return render_template("Dashboardshow.html", time=time, int=int)

@application.route("/Dashboardshowgwan")
def Dashboardshowgwan():
    return render_template("Dashboardshowgwan.html", time=time, int=int)

# @application.route("/tableau")
# def tableau():
#     return render_template("tableau.html")

@application.route("/big/<int:index>/")
def big(index):
    house_info= database.load_house(index)
    name = house_info["name"]
    types = house_info["type"]
    star = house_info["star"]
    visitor = house_info["visitor"]
    blog = house_info["blog"]
    url =house_info["url"]
    image=house_info["image"]
    return render_template("big.html",name=name,types=types,star=star,visitor=visitor,blog=blog,url =url,image=image)

@application.route("/biggwan/<int:index>/")
def biggwan(index):
    house_info= database.load_housegwan(index)
    name = house_info["name"]
    types = house_info["type"]
    star = house_info["star"]
    visitor = house_info["visitor"]
    blog = house_info["blog"]
    url =house_info["url"]
    image=house_info["image"]
    return render_template("biggwan.html",name=name,types=types,star=star,visitor=visitor,blog=blog,url =url,image=image)





if __name__ == "__main__":
    application.run(host='0.0.0.0')