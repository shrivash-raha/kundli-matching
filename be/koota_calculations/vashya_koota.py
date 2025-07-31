# Vashya mapping for Rashi
vashya_map = {
    1: "Chatushpad", 2: "Chatushpad", 3: "Manav", 4: "Jalchar",
    5: "Vanchar", 6: "Manav", 7: "Chatushpad", 8: "Keet",
    9: "Manav", 10: "Jalchar", 11: "Manav", 12: "Jalchar"
}

# Vashya (controllable) relationships
# Key is the controller, Value is the list of controlled
vashya_rules = {
    "Manav": ["Chatushpad", "Jalchar", "Keet"],
    "Vanchar": ["Manav", "Jalchar", "Keet", "Chatushpad"], # Simha (Vanchar) controls all
    "Jalchar": [], # Controls none
    "Chatushpad": [], # Controls none
    "Keet": [] # Controls none
}

def vashya_koota(boy_rashi, girl_rashi):
    boy_vashya = vashya_map.get(boy_rashi)
    girl_vashya = vashya_map.get(girl_rashi)

    if boy_vashya == girl_vashya:
        return 2
    
    score = 0
    # Check if boy's rashi controls girl's rashi
    if girl_vashya in vashya_rules.get(boy_vashya, []):
        score += 1
    # Check if girl's rashi controls boy's rashi
    if boy_vashya in vashya_rules.get(girl_vashya, []):
        score += 1
        
    return score

