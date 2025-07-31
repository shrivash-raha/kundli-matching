def tara_koota(boy_nakshatra, girl_nakshatra):
    # Count from boy's nakshatra to girl's nakshatra
    from_boy = (girl_nakshatra - boy_nakshatra + 27) % 27
    # Count from girl's nakshatra to boy's nakshatra
    from_girl = (boy_nakshatra - girl_nakshatra + 27) % 27

    # Tara is inauspicious if the remainder when divided by 9 is 3, 5, or 7
    # Note: We use modulo on the count, not the nakshatra number itself.
    # The result of modulo will be 0-8. Inauspicious positions are 2, 4, 6.
    boy_to_girl_tara = from_boy % 9
    girl_to_boy_tara = from_girl % 9

    score = 3.0
    if boy_to_girl_tara in [2, 4, 6]: # Corresponds to 3rd, 5th, 7th Tara
        score -= 1.5
    if girl_to_boy_tara in [2, 4, 6]: # Corresponds to 3rd, 5th, 7th Tara
        score -= 1.5
        
    return score




# def tara_koota(boy_nakshatra, girl_nakshatra):
#     # Tara position (1-indexed)
#     tara_pos = (girl_nakshatra - boy_nakshatra) % 9
#     if tara_pos == 0:
#         tara_pos = 9

#     if tara_pos in [1, 4, 6, 7, 8, 9]:
#         return 3
#     elif tara_pos in [3, 5]:
#         return 1.5
#     elif tara_pos == 2:
#         return 0


# # Tara Koota
# def tara_koota(boy_nakshatra, girl_nakshatra):
#     tara_index = (girl_nakshatra - boy_nakshatra) % 9
#     return 0 if tara_index in [1, 3, 6, 8] else 3

