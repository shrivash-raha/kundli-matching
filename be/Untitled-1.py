
bhakoot_score_table = {
    1: 7, 2: 0, 3: 7, 4: 7, 5: 0, 6: 0, 7: 0, 8: 0, 9: 7, 10: 0, 11: 7
}

def bhakoot_koota(boy_rashi, girl_rashi):
    diff = abs(boy_rashi - girl_rashi)
    if diff > 6:
        diff = 12 - diff
    return bhakoot_score_table.get(diff, 0)

#####################

gana_map = {
    # 1 to 27 Nakshatra Index
    1: "Deva", 2: "Manushya", 3: "Rakshasa", 4: "Manushya", 5: "Rakshasa", 6: "Deva",
    7: "Rakshasa", 8: "Rakshasa", 9: "Deva", 10: "Manushya", 11: "Rakshasa", 12: "Manushya",
    13: "Rakshasa", 14: "Manushya", 15: "Deva", 16: "Rakshasa", 17: "Rakshasa", 18: "Deva",
    19: "Manushya", 20: "Rakshasa", 21: "Deva", 22: "Rakshasa", 23: "Rakshasa", 24: "Deva",
    25: "Manushya", 26: "Manushya", 27: "Deva"
}

def gana_koota(boy_nak, girl_nak):
    g1 = gana_map[boy_nak]
    g2 = gana_map[girl_nak]

    if g1 == g2:
        return 6
    if (g1 == "Deva" and g2 == "Manushya") or (g1 == "Manushya" and g2 == "Deva"):
        return 5
    if (g1 == "Manushya" and g2 == "Rakshasa"):
        return 1
    if (g1 == "Rakshasa" and g2 == "Manushya"):
        return 0
    if (g1 == "Rakshasa" and g2 == "Deva"):
        return 1
    if (g1 == "Deva" and g2 == "Rakshasa"):
        return 0
    return 0
######################

moon_lords = {
    1: "Mars", 2: "Venus", 3: "Mercury", 4: "Moon",
    5: "Sun", 6: "Mercury", 7: "Venus", 8: "Mars",
    9: "Jupiter", 10: "Saturn", 11: "Saturn", 12: "Jupiter"
}

# Friendships between planets
friend_table = {
    "Sun": ["Moon", "Mars", "Jupiter"],
    "Moon": ["Sun", "Mercury"],
    "Mars": ["Sun", "Moon", "Jupiter"],
    "Mercury": ["Sun", "Venus"],
    "Jupiter": ["Sun", "Moon", "Mars"],
    "Venus": ["Mercury", "Saturn"],
    "Saturn": ["Mercury", "Venus"]
}

def graha_maitri_koota(boy_rashi, girl_rashi):
    lord1 = moon_lords[boy_rashi]
    lord2 = moon_lords[girl_rashi]

    if lord1 == lord2:
        return 5
    if lord2 in friend_table.get(lord1, []) and lord1 in friend_table.get(lord2, []):
        return 5
    elif lord2 in friend_table.get(lord1, []) or lord1 in friend_table.get(lord2, []):
        return 3
    else:
        return 0


############################

adi_nadi = {1,6,7,12,13,18,19,24,25}
madhya_nadi = {2,5,8,11,14,17,20,23,26}
antya_nadi = {3,4,9,10,15,16,21,22,27}

def get_nadi(nak):
    if nak in adi_nadi: return "Adi"
    if nak in madhya_nadi: return "Madhya"
    if nak in antya_nadi: return "Antya"
    return None

def nadi_koota(boy_nak, girl_nak):
    return 0 if get_nadi(boy_nak) == get_nadi(girl_nak) else 8
#############################

# Tara Koota
def tara_koota(boy_nakshatra, girl_nakshatra):
    # Count from boy to girl
    from_boy = (girl_nakshatra - boy_nakshatra + 27) % 27 + 1
    # Count from girl to boy
    from_girl = (boy_nakshatra - girl_nakshatra + 27) % 27 + 1

    boy_to_girl_rem = from_boy % 9
    girl_to_boy_rem = from_girl % 9

    score = 0
    # Auspicious tara groups are 1, 2, 4, 6, 8, 9 (or 0 for 9)
    # Inauspicious are 3, 5, 7
    if boy_to_girl_rem not in [3, 5, 7]:
        score += 1.5
    if girl_to_boy_rem not in [3, 5, 7]:
        score += 1.5
        
    return score

#######################

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

#########################

# Vashya mapping for Rashi (simplified groups)
vashya_groups = {
    1: "Chatushpad", 2: "Chatushpad", 3: "Manav", 4: "Jalchar",
    5: "Vanchar", 6: "Manav", 7: "Vanchar", 8: "Keet",
    9: "Chatushpad", 10: "Jalchar", 11: "Manav", 12: "Jalchar"
}

# Simplified Vashya compatibility (Group to Group → Score)
vashya_score = {
    ("Manav", "Manav"): 2,
    ("Chatushpad", "Chatushpad"): 2,
    ("Jalchar", "Jalchar"): 2,
    ("Vanchar", "Vanchar"): 2,
    ("Keet", "Keet"): 2,
    # Partial matches
    ("Manav", "Chatushpad"): 1,
    ("Chatushpad", "Manav"): 1,
    ("Vanchar", "Keet"): 1,
    ("Keet", "Vanchar"): 1,
}

def vashya_koota(boy_rashi, girl_rashi):
    bg = (vashya_groups[boy_rashi], vashya_groups[girl_rashi])
    return vashya_score.get(bg, 0)

##########################

yoni_map = {
    1: "Ashwa", 2: "Gaja", 3: "Mesh", 4: "Sarpa", 5: "Swah", 6: "Mushaka", 7: "Go",
    8: "Mahisha", 9: "Vyaghra", 10: "Mriga", 11: "Sarpa", 12: "Simha", 13: "Mriga",
    14: "Nakul", 15: "Singha", 16: "Shwan", 17: "Vanara", 18: "Go", 19: "Mahisha",
    20: "Ashwa", 21: "Simha", 22: "Vyaghra", 23: "Mriga", 24: "Sarpa", 25: "Shwan",
    26: "Gaja", 27: "Nakul"
}

# Complete Yoni compatibility table (match → 4, enemy → 0, neutral/partial → 2)
compatible_pairs = {
    # Same Yoni
    ("Ashwa", "Ashwa"): 4,
    ("Gaja", "Gaja"): 4,
    ("Mesh", "Mesh"): 4,
    ("Sarpa", "Sarpa"): 4,
    ("Swah", "Swah"): 4,
    ("Mushaka", "Mushaka"): 4,
    ("Go", "Go"): 4,
    ("Mahisha", "Mahisha"): 4,
    ("Vyaghra", "Vyaghra"): 4,
    ("Mriga", "Mriga"): 4,
    ("Simha", "Simha"): 4,
    ("Nakul", "Nakul"): 4,
    ("Shwan", "Shwan"): 4,
    ("Vanara", "Vanara"): 4,
    # Enemies (0 points)
    ("Ashwa", "Gaja"): 0, ("Gaja", "Ashwa"): 0,
    ("Mesh", "Sarpa"): 0, ("Sarpa", "Mesh"): 0,
    ("Swah", "Mushaka"): 0, ("Mushaka", "Swah"): 0,
    ("Go", "Simha"): 0, ("Simha", "Go"): 0,
    ("Mahisha", "Vyaghra"): 0, ("Vyaghra", "Mahisha"): 0,
    ("Mriga", "Nakul"): 0, ("Nakul", "Mriga"): 0,
    ("Shwan", "Vanara"): 0, ("Vanara", "Shwan"): 0,
    # Partial/Neutral (2 points)
    ("Ashwa", "Mesh"): 2, ("Mesh", "Ashwa"): 2,
    ("Gaja", "Mahisha"): 2, ("Mahisha", "Gaja"): 2,
    ("Sarpa", "Vyaghra"): 2, ("Vyaghra", "Sarpa"): 2,
    ("Swah", "Go"): 2, ("Go", "Swah"): 2,
    ("Mushaka", "Mriga"): 2, ("Mriga", "Mushaka"): 2,
    ("Simha", "Vyaghra"): 2, ("Vyaghra", "Simha"): 2,
    ("Nakul", "Shwan"): 2, ("Shwan", "Nakul"): 2,
    ("Vanara", "Go"): 2, ("Go", "Vanara"): 2,
    # Default for all other pairs not listed
}

def yoni_koota(boy_nak, girl_nak):
    a1 = yoni_map[boy_nak]
    a2 = yoni_map[girl_nak]
    if a1 == a2:
        return 4
    pair = (a1, a2)
    rev = (a2, a1)
    return compatible_pairs.get(pair) or compatible_pairs.get(rev) or 2  # default 2

