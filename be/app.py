from flask import Flask, request, jsonify
from flask_cors import CORS
from koota_score_calculation import guna_milan_kootas
from rashi_nakshatra_index import analyze_person_kundli

app = Flask(__name__)
CORS(app)

@app.route("/api/match", methods=["POST"])
def match_kundli():
    data = request.get_json()

    girl = data["girl"]
    boy = data["boy"]

    girl_data = analyze_person_kundli(girl["dob"], girl["tob"], girl["place"])
    boy_data = analyze_person_kundli(boy["dob"], boy["tob"], boy["place"])

    score, total = guna_milan_kootas(boy_data, girl_data)

    return jsonify({
        "girl": girl_data,
        "boy": boy_data,
        "scores": score,
        "total_score": total
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
