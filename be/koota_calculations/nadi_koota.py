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
