bhakoot_score_table = {
    1: 7, 2: 0, 3: 7, 4: 7, 5: 0, 6: 0, 7: 0, 8: 0, 9: 7, 10: 0, 11: 7
}

def bhakoot_koota(boy_rashi, girl_rashi):
    diff = abs(boy_rashi - girl_rashi)
    if diff > 6:
        diff = 12 - diff
    return bhakoot_score_table.get(diff, 0)
