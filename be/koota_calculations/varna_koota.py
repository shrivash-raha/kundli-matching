# Mapping for Varna Koota
varna_map = {
    1: "Brahmin", 2: "Kshatriya", 3: "Kshatriya", 4: "Vaishya",
    5: "Vaishya", 6: "Shudra", 7: "Shudra", 8: "Shudra",
    9: "Vaishya", 10: "Vaishya", 11: "Brahmin", 12: "Brahmin"
}

varna_score_map = {"Shudra": 1, "Vaishya": 2, "Kshatriya": 3, "Brahmin": 4}

def varna_koota(boy_rashi, girl_rashi):
    boy_varna = varna_score_map[varna_map[boy_rashi]]
    girl_varna = varna_score_map[varna_map[girl_rashi]]
    return 1 if boy_varna >= girl_varna else 0

