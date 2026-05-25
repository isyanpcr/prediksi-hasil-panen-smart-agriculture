from flask import Flask, render_template, request
import pickle
import pandas as pd
import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

with open('model1.pkl', 'rb') as f:
    model = pickle.load(f)

try:
    with open('model.pkl', 'rb') as f:
        xgb_model = pickle.load(f)
except ModuleNotFoundError as e:
    xgb_model = None
    print("PERINGATAN: Modul xgboost belum terinstall. Install dengan 'pip install xgboost' agar prediksi XGBoost aktif.")

def init_db():
    conn = sqlite3.connect('history.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            waktu TEXT,
            crop_id TEXT,
            soil_type TEXT,
            seedling_stage TEXT,
            moi REAL,
            temp REAL,
            humidity REAL,
            result INTEGER
        )
    ''')
    c.execute("PRAGMA table_info(history)")
    columns = [row[1] for row in c.fetchall()]
    if 'model_name' not in columns:
        c.execute("ALTER TABLE history ADD COLUMN model_name TEXT")
    conn.commit()
    conn.close()

def insert_history(data):
    conn = sqlite3.connect('history.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO history (waktu, crop_id, soil_type, seedling_stage, moi, temp, humidity, result, model_name)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data['waktu'], data['crop_id'], data['soil_type'], data['seedling_stage'],
        data['moi'], data['temp'], data['humidity'], data['result'], data['model_name']
    ))
    conn.commit()
    conn.close()

def get_history(limit=20):
    conn = sqlite3.connect('history.db')
    c = conn.cursor()
    c.execute('''
        SELECT waktu, crop_id, soil_type, seedling_stage, moi, temp, humidity, result, model_name
        FROM history ORDER BY id DESC LIMIT ?
    ''', (limit,))
    rows = c.fetchall()
    conn.close()
    return [
        {
            'waktu': row[0],
            'crop_id': row[1],
            'soil_type': row[2],
            'seedling_stage': row[3],
            'moi': row[4],
            'temp': row[5],
            'humidity': row[6],
            'result': row[7],
            'model_name': row[8] if len(row) > 8 else 'RandomForest'
        }
        for row in rows
    ]

init_db()

@app.route('/', methods=['GET'])
def index():
    result = request.args.get('result')
    xgb_result = request.args.get('xgb_result')
    history = get_history()
    try:
        result = int(result) if result is not None and result != "Input tidak valid" else result
    except:
        pass
    try:
        xgb_result = int(xgb_result) if xgb_result is not None and xgb_result != "Input tidak valid" else xgb_result
    except:
        pass
    return render_template('form.html', result=result, xgb_result=xgb_result, history=history)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        crop_id = request.form['crop_id']
        soil_type = request.form['soil_type']
        seedling_stage = request.form['seedling_stage']
        moi = float(request.form['moi'])
        temp = float(request.form['temp'])
        humidity = float(request.form['humidity'])
    except Exception:
        return redirect(url_for('index', result="Input tidak valid"))

    x = pd.DataFrame([{
        'crop ID': crop_id,
        'soil_type': soil_type,
        'Seedling Stage': seedling_stage,
        'MOI': moi,
        'temp': temp,
        'humidity': humidity
    }])

    pred = model.predict(x)[0]
    waktu = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    insert_history({
        'waktu': waktu,
        'crop_id': crop_id,
        'soil_type': soil_type,
        'seedling_stage': seedling_stage,
        'moi': moi,
        'temp': temp,
        'humidity': humidity,
        'result': int(pred),
        'model_name': 'RandomForest'
    })
    return redirect(url_for('index', result=int(pred)))

@app.route('/predict_xgb', methods=['POST'])
def predict_xgb():
    if xgb_model is None:
        return redirect(url_for('index', xgb_result="XGBoost model tidak tersedia. Install modul xgboost."))
    try:
        crop_id = request.form['crop_id_xgb']
        soil_type = request.form['soil_type_xgb']
        seedling_stage = request.form['seedling_stage_xgb']

        moi = float(request.form['moi_xgb'])
        temp = float(request.form['temp_xgb'])
        humidity = float(request.form['humidity_xgb'])
    except Exception:
        return redirect(url_for('index', xgb_result="Input tidak valid"))

    x = pd.DataFrame([{
        'crop ID': crop_id,
        'soil_type': soil_type,
        'Seedling Stage': seedling_stage,
        'MOI': moi,
        'temp': temp,
        'humidity': humidity
    }])

    try:
        pred = xgb_model.predict(x)[0]
    except Exception as e:
        return redirect(url_for('index', xgb_result="Input tidak valid: pastikan model.pkl adalah pipeline dengan preprocessing"))

    waktu = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    insert_history({
        'waktu': waktu,
        'crop_id': crop_id,
        'soil_type': soil_type,
        'seedling_stage': seedling_stage,
        'moi': moi,
        'temp': temp,
        'humidity': humidity,
        'result': int(pred),
        'model_name': 'XGBoost'
    })
    return redirect(url_for('index', xgb_result=int(pred)))

if __name__ == '__main__':
    app.run(debug=True)
