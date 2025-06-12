from flask import Flask,render_template, request
import os
from dotenv import load_dotenv
import psycopg2
from psycopg2 import OperationalError

# 載入 .env 檔案
load_dotenv()
conn_string = os.getenv('RENDER_DATABASE')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html.jinja2")

@app.route("/classes",defaults={'course_types':'一般課程'})
@app.route("/classes/<course_types>")
def classes(course_types):
    # name = "Robert"
    # weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    print(course_types)
    conn = psycopg2.connect(conn_string)
    with conn.cursor() as cur:
        sql = "SELECT DISTINCT 課程類別 FROM 進修課程"
        cur.execute(sql)
        temps = cur.fetchall()
        print('temps= ',temps)
        kinds = [kind[0] for kind in temps]
        print('kinds = ',kinds)
        kinds.reverse()
        print('kinds reverse =  ',kinds)
        
        # sql_course = f"""
        # SELECT
        #     "課程名稱",
        #     "老師",
        #     "進修人數",
        #     "報名開始日期",
        #     "報名結束日期",
        #     "課程內容",
        #     "進修費用"
        # FROM
        #     "進修課程"
        # WHERE
        #     "課程類別" = '{course_types}'
        # LIMIT 6;
        # """
        
        sql_course = f"""
        SELECT
            "群組",
             "課程名稱",
             "進修人數",
             "進修時數",
             "進修費用",
             "上課時間",
             "課程開始日期"
        FROM
            "進修課程"
        WHERE
            "課程類別" = '{course_types}'
        LIMIT 100;
        """
        
        cur.execute(sql_course)
        course_data = cur.fetchall()
        print(course_data)
        
        page = request.args.get('page', default=1, type=int)
        per_page = 6
        total = len(course_data)
        total_pages = total // per_page + 1
        start = (page - 1) * per_page
        end = start + per_page
        items = course_data[start:end]
        

    return render_template("classes.html.jinja2", kinds = kinds,course_data=items, page = page, total_pages = total_pages)

@app.route("/new")
def new():
    try:
        conn = psycopg2.connect(conn_string)
        with conn.cursor() as cur:
            sql = """SELECT * FROM public.最新訊息
                     ORDER BY 上版日期 desc"""
            cur.execute(sql)
        # 取得所有資料
            rows = cur.fetchall()
            
        
    except OperationalError as e:
        print("連線失敗")
        print(e)
        return render_template("error.html.jinja2",error_message="資料庫錯誤"),500
    except:
        return render_template("error.html.jinja2",error_message="不知名錯誤"),500
    conn.close()
    return render_template("new.html.jinja2",rows=rows)

@app.route("/traffic")
def traffic():
    return render_template("traffic.html.jinja2")

@app.route("/contact")
def contact():
    return render_template("contact.html.jinja2")

