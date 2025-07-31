yoni_map = {
    1: "Ashwa", 2: "Gaja", 3: "Mesha", 4: "Sarpa", 5: "Shwan", 6: "Marjara", 7: "Mushaka",
    8: "Go", 9: "Mahisha", 10: "Vyaghra", 11: "Mriga", 12: "Vanara", 13: "Nakula",
    14: "Simha", 15: "Go", 16: "Mahisha", 17: "Vyaghra", 18: "Mriga", 19: "Vanara",
    20: "Nakula", 21: "Simha", 22: "Ashwa", 23: "Gaja", 24: "Mesha", 25: "Sarpa",
    26: "Shwan", 27: "Marjara"
}

# Define sworn enemy pairs. All other pairs are scored based on friendship level.
sworn_enemies = {
    ("Go", "Vyaghra"), ("Gaja", "Simha"), ("Ashwa", "Mahisha"),
    ("Shwan", "Mriga"), ("Sarpa", "Nakula"), ("Mushaka", "Marjara"),
    ("Mesha", "Vanara")
}

def is_enemy(yoni1, yoni2):
    return (yoni1, yoni2) in sworn_enemies or (yoni2, yoni1) in sworn_enemies

def yoni_koota(boy_nak, girl_nak):
    yoni_boy = yoni_map.get(boy_nak)
    yoni_girl = yoni_map.get(girl_nak)

    if yoni_boy == yoni_girl:
        return 4  # Same Yoni: Perfect match
    
    if is_enemy(yoni_boy, yoni_girl):
        return 0  # Sworn Enemies: No match
    
    # For simplicity, many systems classify non-enemy, non-same pairs with varying scores.
    # A common simplified approach is:
    # Friendly: 3, Neutral: 2, Enemy: 1.
    # Without a full table, we can assign a neutral score for non-enemy, non-identical pairs.
    # A more detailed implementation would require a full compatibility matrix.
    # Let's use a simplified but common scoring:
    # Same: 4, Enemy: 0, Friendly (not same, not enemy): 3, Neutral: 2, Inimical: 1
    # For this implementation, we will assume non-enemy and non-same are "Friendly".
    
    # A common simplification is to check if they are just enemies (1 point) vs sworn enemies (0 points)
    # This file lacks that distinction, so we will treat any non-sworn-enemy pair as neutral.
    return 2 # Neutral score for other pairs
