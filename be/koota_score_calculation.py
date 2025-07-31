
# from rashi_nakshatra_index import analyze_person_kundli

from koota_calculations.bhakoot_koota import bhakoot_koota
from koota_calculations.gana_koota import gana_koota
from koota_calculations.graha_maitri_koota import graha_maitri_koota
from koota_calculations.nadi_koota import nadi_koota
from koota_calculations.varna_koota import varna_koota
from koota_calculations.vashya_koota import vashya_koota
from koota_calculations.tara_koota import tara_koota
from koota_calculations.yoni_koota import yoni_koota

def guna_milan_kootas(boy, girl):

    score = {}
    score["Varna"] = varna_koota(boy["rashi_index"], girl["rashi_index"])
    score["Vashya"] = vashya_koota(boy["rashi_index"], girl["rashi_index"])
    score["Tara"] = tara_koota(boy["nakshatra_index"], girl["nakshatra_index"])
    score["Yoni"] = yoni_koota(boy["nakshatra_index"], girl["nakshatra_index"])
    score["Graha Maitri"] = graha_maitri_koota(boy["rashi_index"], girl["rashi_index"])
    score["Gana"] = gana_koota(boy["nakshatra_index"], girl["nakshatra_index"])
    score["Bhakoot"] = bhakoot_koota(boy["rashi_index"], girl["rashi_index"])
    score["Nadi"] = nadi_koota(boy["nakshatra_index"], girl["nakshatra_index"])

    total = sum(score.values())
    return score, total


# boy = {
#     "dob": "1995-01-01",
#     "tob": "00:00",
#     "place": "Delhi"
# }
# girl ={
#     "dob": "2000-01-01",
#     "tob": "00:00",
#     "place": "Delhi"
# }

# boy_index = analyze_person_kundli(boy["dob"], boy["tob"], boy["place"])
# girl_index = analyze_person_kundli(girl["dob"], girl["tob"], girl["place"])

# score, total = guna_milan_kootas(boy_index, girl_index)


# print("Breakdown:", score)
# print("Total Score:", total, "/ 36")

