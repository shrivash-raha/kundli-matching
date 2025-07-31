gana_map = {
    # 1 to 27 Nakshatra Index
    1: "Deva", 2: "Manushya", 3: "Rakshasa", 4: "Manushya", 5: "Rakshasa", 6: "Deva",
    7: "Rakshasa", 8: "Rakshasa", 9: "Deva", 10: "Manushya", 11: "Rakshasa", 12: "Manushya",
    13: "Rakshasa", 14: "Manushya", 15: "Deva", 16: "Rakshasa", 17: "Rakshasa", 18: "Deva",
    19: "Manushya", 20: "Rakshasa", 21: "Deva", 22: "Rakshasa", 23: "Rakshasa", 24: "Deva",
    25: "Manushya", 26: "Manushya", 27: "Deva"
}

def gana_koota(boy_nak, girl_nak):
    g1 = gana_map.get(boy_nak)
    g2 = gana_map.get(girl_nak)

    if g1 == g2:
        return 6  # Perfect match
    
    if (g1 == "Deva" and g2 == "Manushya") or (g1 == "Manushya" and g2 == "Deva"):
        return 6  # Good match
    
    if g1 == "Deva" and g2 == "Rakshasa":
        return 1  # Poor match
    
    if g1 == "Rakshasa" and g2 == "Deva":
        return 0  # Very poor match
        
    if (g1 == "Manushya" and g2 == "Rakshasa") or (g1 == "Rakshasa" and g2 == "Manushya"):
        return 0  # Incompatible
        
    return 0
