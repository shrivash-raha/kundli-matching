moon_lords = {
    1: "Mars", 2: "Venus", 3: "Mercury", 4: "Moon",
    5: "Sun", 6: "Mercury", 7: "Venus", 8: "Mars",
    9: "Jupiter", 10: "Saturn", 11: "Saturn", 12: "Jupiter"
}

# Friendships between planets (includes friends, neutrals, enemies)
friend_table = {
    "Sun":     {"friends": ["Moon", "Mars", "Jupiter"], "neutrals": ["Mercury"], "enemies": ["Venus", "Saturn"]},
    "Moon":    {"friends": ["Sun", "Mercury"], "neutrals": ["Mars", "Jupiter", "Venus", "Saturn"], "enemies": []},
    "Mars":    {"friends": ["Sun", "Moon", "Jupiter"], "neutrals": ["Venus", "Saturn"], "enemies": ["Mercury"]},
    "Mercury": {"friends": ["Sun", "Venus"], "neutrals": ["Mars", "Jupiter", "Saturn"], "enemies": ["Moon"]},
    "Jupiter": {"friends": ["Sun", "Moon", "Mars"], "neutrals": ["Saturn"], "enemies": ["Mercury", "Venus"]},
    "Venus":   {"friends": ["Mercury", "Saturn"], "neutrals": ["Mars", "Jupiter"], "enemies": ["Sun", "Moon"]},
    "Saturn":  {"friends": ["Mercury", "Venus"], "neutrals": ["Jupiter"], "enemies": ["Sun", "Moon", "Mars"]}
}

def get_relationship(lord1, lord2):
    if lord2 in friend_table[lord1]["friends"]:
        return "friend"
    if lord2 in friend_table[lord1]["neutrals"]:
        return "neutral"
    if lord2 in friend_table[lord1]["enemies"]:
        return "enemy"
    return None

def graha_maitri_koota(boy_rashi, girl_rashi):
    lord1 = moon_lords[boy_rashi]
    lord2 = moon_lords[girl_rashi]

    if lord1 == lord2:
        return 5

    rel1_to_2 = get_relationship(lord1, lord2)
    rel2_to_1 = get_relationship(lord2, lord1)

    if rel1_to_2 == "friend" and rel2_to_1 == "friend":
        return 5
    if (rel1_to_2 == "friend" and rel2_to_1 == "neutral") or \
       (rel1_to_2 == "neutral" and rel2_to_1 == "friend"):
        return 4
    if rel1_to_2 == "neutral" and rel2_to_1 == "neutral":
        return 3
    if (rel1_to_2 == "friend" and rel2_to_1 == "enemy") or \
       (rel1_to_2 == "enemy" and rel2_to_1 == "friend"):
        return 1
    if (rel1_to_2 == "neutral" and rel2_to_1 == "enemy") or \
       (rel1_to_2 == "enemy" and rel2_to_1 == "neutral"):
        return 0.5
    if rel1_to_2 == "enemy" and rel2_to_1 == "enemy":
        return 0
    
    return 0 # Default case










# moon_lords = {
#     1: "Mars", 2: "Venus", 3: "Mercury", 4: "Moon",
#     5: "Sun", 6: "Mercury", 7: "Venus", 8: "Mars",
#     9: "Jupiter", 10: "Saturn", 11: "Saturn", 12: "Jupiter"
# }

# # Friendships between planets
# friend_table = {
#     "Sun": ["Moon", "Mars", "Jupiter"],
#     "Moon": ["Sun", "Mercury"],
#     "Mars": ["Sun", "Moon", "Jupiter"],
#     "Mercury": ["Sun", "Venus"],
#     "Jupiter": ["Sun", "Moon", "Mars"],
#     "Venus": ["Mercury", "Saturn"],
#     "Saturn": ["Mercury", "Venus"]
# }

# def graha_maitri_koota(boy_rashi, girl_rashi):
#     lord1 = moon_lords[boy_rashi]
#     lord2 = moon_lords[girl_rashi]

#     if lord1 == lord2:
#         return 5
#     if lord2 in friend_table.get(lord1, []) and lord1 in friend_table.get(lord2, []):
#         return 5
#     elif lord2 in friend_table.get(lord1, []) or lord1 in friend_table.get(lord2, []):
#         return 3
#     else:
#         return 0
