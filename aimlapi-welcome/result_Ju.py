
mention_to_pred_entity_df1 = {
    2: 0, 5: 0, 8: 0, 13: 0, 16: 0, 23: 0, 30: 0,
    19: 1, 26: 1,
}

pred_clusters_df1 = [
    [2, 5, 8, 13, 16, 23, 30],   # Entity 1: I
    [19, 26],                   # Entity 3: school
]

mention_to_pred_entity_df2 = {
    37: 0, 52: 0, 58: 0,
    35: 1, 36: 1,
    41: 2, 42: 2, 49: 2, 62: 2,
    43: 3, 47: 3, 69: 3,
    45: 4,
    46: 5, 68: 5,
    50: 6, 55: 6,
    39: 7, 44: 7,
}

pred_clusters_df2 = [
    [37, 52, 58],                # Entity 1: I
    [35, 36],                    # Entity 3: permission
    [41, 42, 49, 62],            # Entity 4: deaf association
    [43, 47, 69],                # Entity 5: swimming
    [45],                        # Entity 6: there
    [46, 68],                    # Entity 7: training
    [50, 55],                    # Entity 8: people
    [39, 44],                    # Entity 21: boarding/entering
]

mention_to_pred_entity_df3 = {
    82: 0, 88: 0, 98: 0,
    72: 1, 92: 1, 116: 1,
    75: 2, 78: 2, 99: 2, 109: 2, 115: 2,
    79: 3, 83: 3, 84: 3, 89: 3, 106: 3, 101: 3, 129: 3, 128: 3,
    81: 4, 120: 4,
    113: 5,
}


pred_clusters_df3 = [
    [82, 88, 98],                      # Entity 1: I
    [72, 92, 116],                    # Entity 2: young
    [75, 78, 99, 109, 115],           # Entity 3: together
    [79, 83, 84, 89, 106, 101, 129, 128],  # Entity 5: entertainment/fun
    [81, 120],                        # Entity 6: adults
    [113],                            # Entity 13: Deaf community
]

mention_to_pred_entity_df4 = {
    138: 0, 150: 0,
    139: 1, 142: 1, 146: 1,
}

pred_clusters_df4 = [
    [138, 150],                # Entity 1: I
    [139, 142, 146],           # Entity 2: bowling
]

mention_to_pred_entity_df5 = {
    160: 0, 167: 0, 174: 0, 184: 0, 191: 0, 196: 0, 202: 0,
    156: 0, 170: 0, 180: 0, 182: 0,

    158: 1, 161: 1, 159: 1, 162: 1,

    163: 2, 169: 2, 172: 2, 222: 2, 225: 2, 231: 2,
    164: 2, 166: 2,
}

pred_clusters_df5 = [
    [160, 167, 174, 184, 191, 196, 202, 156, 170, 180, 182],  # Entity 1: 'I'
    [158, 161, 159, 162],                                    # Entity 2: 'Hamburg'
    [163, 169, 172, 222, 225, 231, 164, 166],                # Entity 3: 'Swimming' (competition)
]

mention_to_pred_entity_df6 = {
    235: 0, 242: 0, 260: 0,           # Speaker A ("you")
    251: 1, 257: 1,                   # Speaker B ("I")
    252: 2, 256: 2, 261: 2,           # Swimming
    255: 2, 262: 2,                   # Swimming back and forth
    254: 2, 263: 2, 264: 2,           # Exhausting
    253: 2,                          # Alone
    259: 2,                          # No desire (likely linked to swimming)
}

pred_clusters_df6 = [
    [235, 242, 260],                 # Entity 1: Speaker A (referred to as "you")
    [251, 257],                      # Entity 2: Speaker B (referred to as "I")
    [252, 256, 261, 255, 262, 254, 263, 264, 253, 259],  # Entity 3: Swimming-related activity
]

mention_to_pred_entity_df7 = {
    268: 0, 276: 0, 297: 0, 307: 0, 309: 0,         # Speaker A
    282: 1, 283: 1, 287: 1, 301: 1, 303: 1, 305: 1,  # Speaker B
    266: 2, 270: 2, 322: 2,                         # Fight
    278: 3, 291: 3,                                 # Water
    272: 4,                                         # Training
    298: 5, 318: 5,                                 # Swimming
}

pred_clusters_df7 = [
    [268, 276, 297, 307, 309],          # Entity 1: Speaker A ("I", self-reference, INDEX)
    [282, 283, 287, 301, 303, 305],     # Entity 2: Speaker B ("I", self-reference, INDEX)
    [266, 270, 322],                    # Entity 3: Fight/Struggle
    [278, 291],                         # Entity 4: Water
    [272],                              # Entity 5: Training
    [298, 318],                         # Entity 6: Swimming
]

mention_to_pred_entity_df8 = {
    327: 0, 331: 0, 341: 0, 344: 0,  # training
    328: 1, 330: 1, 345: 1,          # swimming
    349: 2, 351: 2,                  # I/me (speaker)
}

pred_clusters_df8 = [
    [327, 331, 341, 344],          # Entity 1: training (swim training sessions)
    [328, 330, 345],               # Entity 2: swimming (activity)
    [349, 351],                   # Entity 4: I / me (speaker)
]

mention_to_pred_entity_df9 = {
    362: 0, 384: 0,                          # I/me (speaker A)
    357: 1, 358: 1, 360: 1, 364: 1, 377: 1, 391: 1,  # bowling (activity)
    368: 2, 369: 2, 376: 2,                  # association/club (bowling related)
    366: 3, 390: 3, 392: 3,                  # competition
    363: 4, 374: 4, 375: 4, 379: 4,          # activity/active participation
}

pred_clusters_df9 = [
    [362, 384],                               # entity 1: I/me (speaker A)
    [357, 358, 360, 364, 377, 391],          # entity 2: bowling (activity)
    [368, 369, 376],                         # entity 3: association/club (bowling related)
    [366, 390, 392],                         # entity 4: competition
    [363, 374, 375, 379],                    # entity 5: activity/active participation
]

mention_to_pred_entity_df10 = {
    # Participants/Speakers
    397: 0, 399: 0, 398: 0, 401: 0, 403: 0, 412: 0, 443: 0, 400: 0, 408: 0,
    # Group/Collective
    404: 1, 449: 1, 457: 1, 440: 1, 461: 1,
    # Activities
    424: 2, 441: 2, 426: 2, 450: 2, 452: 2,
    # Sports/Competitions
    417: 3, 445: 3, 413: 3, 447: 3,
    # Transportation
    414: 4, 446: 4, 429: 4,
    # List Items
    423: 5, 424: 5, 425: 5, 426: 5, 427: 5, 428: 5, 429: 5, 431: 5, 432: 5, 436: 5, 437: 5, 438: 5,
}


pred_clusters_df10 = [
    # Entity: Participants/Speakers
    [397, 399, 398, 401, 403, 412, 443, 400, 408],
    # Entity: Group/Collective
    [404, 449, 457, 440, 461],
    # Entity: Activities
    [424, 441, 426, 450, 452],
    # Entity: Sports/Competitions
    [417, 445, 413, 447],
    # Entity: Transportation
    [414, 446, 429],
    # Entity: List Items (grouped by their list markers)
    [423, 424, 425, 426, 427, 428, 429, 431, 432, 436, 437, 438]
]

mention_to_pred_entity_df11 = {
    # entity 1: 'I' (speaker A)
    496: 0,
    503: 0,
    508: 0,
    # entity 4: 'entertainment/conversation'
    473: 1,
    486: 1
}

pred_clusters_df11 = [
    # entity 1: 'I' (speaker A)
    [496, 503, 508],
    # entity 4: 'entertainment/conversation'
    [473, 486]
]

mention_to_pred_entity_df12 = {
    # entity 1: Speaker A (the signer)
    517: 0,
    521: 0,
    546: 0,
    549: 0,
    566: 0,
    581: 0,
    535: 0,
    527: 0,
    # entity 3: Sign language (Gebärden)
    512: 1,
    518: 1,
    533: 1,
    537: 1,
    579: 1,
    # entity 4: Fingerspelling (Fingeralphabet)
    548: 2,
    558: 2,
    563: 2,
    572: 2,
    577: 2,
    # entity 6: Lecturer/Teacher role
    513: 3,
    519: 3,
    538: 3,
    580: 3
}

pred_clusters_df12 = [
    # entity 1: Speaker A (the signer)
    [517, 521, 546, 549, 566, 581, 535, 527],
    # entity 3: Sign language (Gebärden)
    [512, 518, 533, 537, 579],
    # entity 4: Fingerspelling (Fingeralphabet)
    [548, 558, 563, 572, 577],
    # entity 6: Lecturer/Teacher role
    [513, 519, 538, 580]
]

mention_to_pred_entity_df13 = {
    584: 0,
    596: 0,
    601: 0
}

pred_clusters_df13 = [
    # entity 1: 'I' (speaker referring to themselves)
    [584, 596, 601]
]

##DEEP SEEK ZERO SHOT

mention_to_pred_entity_dz1 = {
    # entity 1: First-Person (Speaker)
    2: 0,
    5: 0,
    8: 0,
    13: 0,
    16: 0,
    23: 0,
    30: 0,
    # entity 3: Deaf Identity / Signing
    11: 1,
    12: 1,
    # entity 4: School
    19: 2,
    26: 2
}


pred_clusters_dz1 = [
    # entity 1: First-Person (Speaker)
    [2, 5, 8, 13, 16, 23, 30],
    # entity 3: Deaf Identity / Signing
    [11, 12],
    # entity 4: School
    [19, 26]
]

mention_to_pred_entity_dz2 = {
    # entity 1: Speaker (1st Person)
    37: 0,
    52: 0,
    58: 0,
    # entity 4: Club (Verein)
    42: 1,
    62: 1
}

pred_clusters_dz2 = [
    # entity 1: Speaker (1st Person)
    [37, 52, 58],
    # entity 4: Club (Verein)
    [42, 62]
]

mention_to_pred_entity_dz3 = {
    # entity 1: Speaker
    82: 0,
    88: 0,
    98: 0,
    # entity 3: Young People / Children
    72: 1,
    92: 1,
    116: 1,
    # entity 4: Adults
    81: 2,
    120: 2,
    # entity 6: General Group (All)
    90: 3,
    117: 3,
    # entity 7: Deaf/Hard of Hearing Community
    113: 4,
    # entity 8: Entertainment/Activities
    79: 5,
    84: 5,
    89: 5,
    101: 5,
    128: 5
}

pred_clusters_dz3 = [
    # entity 1: Speaker (First Person Singular)
    [82, 88, 98],
    # entity 3: Young People / Children
    [72, 92, 116],
    # entity 4: Adults
    [81, 120],
    # entity 6: General Group (All)
    [90, 117],
    # entity 7: Deaf/Hard of Hearing Community
    [113],
    # entity 8: Entertainment/Activities
    [79, 84, 89, 101, 128]
]

pred_clusters_dz4 = [
    # entity 1: First-Person Speaker (Ich / I)
    [138, 150]
]

mention_to_pred_entity_dz4 = {
    138: 0,
    150: 0
}

pred_clusters_dz5 = [
    # entity 1: Signer
    [160, 167, 174, 184, 191, 196, 202, 156, 170, 180, 182],
    # entity 2: Hamburg
    [158, 161, 159, 162, 168],
    # entity 3: Swimming
    [163, 172, 169, 222, 225, 231],
    # entity 4: Competition
    [164, 166, 165, 175, 177, 187, 215]
]

mention_to_pred_entity_dz5 = {
    # entity 1: Signer
    160: 0,
    167: 0,
    174: 0,
    184: 0,
    191: 0,
    196: 0,
    202: 0,
    156: 0,
    170: 0,
    180: 0,
    182: 0,
    # entity 2: Hamburg
    158: 1,
    161: 1,
    159: 1,
    162: 1,
    168: 1,
    # entity 3: Swimming
    163: 2,
    172: 2,
    169: 2,
    222: 2,
    225: 2,
    231: 2,
    # entity 4: Competition
    164: 3,
    166: 3,
    165: 3,
    175: 3,
    177: 3,
    187: 3,
    215: 3
}


mention_to_pred_entity_dz6 = {
    # entity 1: Speaker A
    251: 0,
    257: 0,
    # entity 2: Speaker B
    235: 1,
    242: 1,
    260: 1,
    # entity 3: Swimming actions
    252: 2,
    256: 2,
    261: 2,
    # entity 4: Motion - back and forth
    255: 3,
    262: 3
}
pred_clusters_dz6 = [
    # entity 1: Speaker A
    [251, 257],
    # entity 2: Speaker B
    [235, 242, 260],
    # entity 3: Swimming actions
    [252, 256, 261],
    # entity 4: Motion - back and forth
    [255, 262]
]
mention_to_pred_entity_dz7 = {
    # Entity 1: Speaker A
    268: 0,
    276: 0,
    307: 0,
    282: 0,
    283: 0,
    287: 0,
    303: 0,
    305: 0,
    309: 0,
    # Entity 3: KAMPF
    266: 1,
    270: 1,
    322: 1,
    # Entity 6: WASSER
    278: 2,
    291: 2,
    # Entity 7: SCHWIMMEN
    298: 3,
    318: 3
}
pred_clusters_dz7 = [
    # Entity 1: Speaker A
    [268, 276, 307, 282, 283, 287, 303, 305, 309],
    # Entity 3: KAMPF
    [266, 270, 322],
    # Entity 6: WASSER
    [278, 291],
    # Entity 7: SCHWIMMEN
    [298, 318]
]
mention_to_pred_entity_dz8 = {
    # 1. Training
    327: 0,
    331: 0,
    341: 0,
    344: 0,
    # 2. Swimming
    328: 1,
    330: 1,
    345: 1,
    # 9. Speaker (I/my)
    349: 2,
    351: 2,
}

pred_clusters_dz8 = [
    # entity 1: Training
    [327, 331, 341, 344],
    # entity 2: Swimming
    [328, 330, 345],
    # entity 9: Speaker (I/my)
    [349, 351]
]

pred_clusters_dz9 = [
    # entity 1: Bowling (KEGELN1)
    [357, 358, 360, 364, 377, 391],
    # entity 2: Speaker A (ICH)
    [362, 384],
    # entity 3: Association (VERBAND)
    [368, 369]
]

mention_to_pred_entity_dz9 = {
    357: 0,
    358: 0,
    360: 0,
    364: 0,
    377: 0,
    391: 0,
    362: 1,
    384: 1,
    368: 2,
    369: 2
}
pred_clusters_dz10 = [
    # entity 1: Speaker A ("I")
    [412, 443],
    # entity 2: Group ("all")
    [404, 440, 449, 457],
    # entity 3: "Mit"
    [397, 399],
    # entity 4: "Kampf"
    [413, 447],
    # entity 5: "Kegeln"
    [424, 441]
]

mention_to_pred_entity_dz10 = {
    412: 0,
    443: 0,
    404: 1,
    440: 1,
    449: 1,
    457: 1,
    397: 2,
    399: 2,
    413: 3,
    447: 3,
    424: 4,
    441: 4
}
pred_clusters_dz11 = [
    # entity 6: Alcoholic Drinks
    [475, 477],
    # entity 9: Speaker A (self)
    [496, 503, 508]
]

mention_to_pred_entity_dz11 = {
    475: 0,
    477: 0,
    496: 1,
    503: 1,
    508: 1
}
pred_clusters_dz12 = [
    # entity 1: Speaker A (the signer)
    [517, 521, 546, 549, 566, 581, 541, 543, 552, 557, 559],
    # entity 2: Sign Language (Gebärden)
    [512, 518, 533, 537, 579],
    # entity 3: Teacher/Dozent
    [513, 519, 538, 580],
    # entity 4: Finger Alphabet (Fingeralphabet)
    [548, 558, 563, 572, 577]
]

mention_to_pred_entity_dz12 = {
    # Speaker A (the signer)
    517: 0, 521: 0, 546: 0, 549: 0, 566: 0, 581: 0,
    541: 0, 543: 0, 552: 0, 557: 0, 559: 0,
    # Sign Language (Gebärden)
    512: 1, 518: 1, 533: 1, 537: 1, 579: 1,
    # Teacher/Dozent
    513: 2, 519: 2, 538: 2, 580: 2,
    # Finger Alphabet (Fingeralphabet)
    548: 3, 558: 3, 563: 3, 572: 3, 577: 3
}
pred_clusters_dz13 = [
    # entity 1: Speaker (A)
    [584, 596, 601],
]

mention_to_pred_entity_dz13 = {
    # Speaker (A)
    584: 0, 596: 0, 601: 0,
}


pred_clusters_cz1 = [
    [2, 5, 8, 13, 16, 23, 30],  # Cluster 1: "I" or "me"
]

mention_to_pred_entity_cz1 = {
    2: 0,
    5: 0,
    8: 0,
    13: 0,
    16: 0,
    23: 0,
    30: 0,
}
pred_clusters_cz2 = [
    [37, 52, 58],   # Cluster 1: "I"
    [41, 49],       # Cluster 2: "deaf community"
    [42, 62],       # Cluster 3: "club/association"
]

mention_to_pred_entity_cz2 = {
    37: 0, 52: 0, 58: 0,    # Cluster 1 entity id = 0
    41: 1, 49: 1,           # Cluster 2 entity id = 1
    42: 2, 62: 2,           # Cluster 3 entity id = 2
}

pred_clusters_cz3 = [
    [72, 92, 116],     # Cluster 2: "young people"
    [81, 120],         # Cluster 3: "adults"
    [82, 88, 98],      # Cluster 4: "I" (first-person speaker)
]

mention_to_pred_entity_cz3 = {
    72: 0, 92: 0, 116: 0,    # young people -> entity 0
    81: 1, 120: 1,           # adults -> entity 1
    82: 2, 88: 2, 98: 2,     # "I" -> entity 2
}

pred_clusters_cz4 = [
    [138, 150],  # Cluster 1: "ICH1" and "ICH2", same speaker
]

mention_to_pred_entity_cz4 = {
    138: 0,
    150: 0,
}

mention_to_pred_entity_cz5 = {
    156: 0, 160: 0, 167: 0, 170: 0, 180: 0, 182: 0, 184: 0, 191: 0, 196: 0, 202: 0,  # entity 0: I (speaker)
    158: 1, 161: 1,                                                                # entity 1: Hamburg (location)
    159: 2, 162: 2,                                                                # entity 2: Dortmund (location)
    163: 3, 172: 3, 225: 3, 231: 3                                                 # entity 3: Swimming (activity)
}

pred_clusters_cz5 = [
    [156, 160, 167, 170, 180, 182, 184, 191, 196, 202],  # entity 0: I (speaker)
    [158, 161],                                          # entity 1: Hamburg (location)
    [159, 162],                                          # entity 2: Dortmund (location)
    [163, 172, 225, 231]                                 # entity 3: Swimming (activity)
]
mention_to_pred_entity_cz6 = {
    235: 0, 242: 0, 260: 0,  # entity 0: "you" (DU1*)
    251: 1, 257: 1,          # entity 1: "I" (ICH1)
    252: 2, 256: 2, 261: 2,  # entity 2: "swimming" (SCHWIMMEN1)
}

pred_clusters_cz6 = [
    [235, 242, 260],          # entity 0: "you"
    [251, 257],               # entity 1: "I"
    [252, 256, 261],          # entity 2: "swimming"
]
mention_to_pred_entity_cz7 = {
    266: 0, 270: 0, 322: 0,                     # entity 0: "KAMPF1A" (Kampf)
    268: 1, 276: 1, 282: 1, 283: 1, 287: 1, 307: 1,  # entity 1: "ICH1" (Speaker A)
    278: 2, 291: 2,                             # entity 2: "WASSER1" (water)
    298: 3, 318: 3,                             # entity 3: "SCHWIMMEN1" (swimming)
    303: 4, 305: 4, 309: 4                      # entity 4: "ICH2" (Speaker A variant)
}

pred_clusters_cz7 = [
    [266, 270, 322],        # Kampf
    [268, 276, 282, 283, 287, 307],  # ICH1
    [278, 291],             # Wasser
    [298, 318],             # Schwimmen
    [303, 305, 309],        # ICH2
]

mention_to_pred_entity_cz8 = {
    327: 0, 331: 0, 341: 0, 344: 0,    # entity 0: TRAINING1 (training)
    328: 1, 330: 1, 345: 1,            # entity 1: SCHWIMMEN1 (swimming)
    349: 2,                           # entity 2: MEIN1 (my)
    351: 3                            # entity 3: ICH2 (I)
}

pred_clusters_cz8 = [
    [327, 331, 341, 344],  # training
    [328, 330, 345],       # swimming
    [349],                 # my
    [351]                  # I
]

mention_to_pred_entity_cz9 = {
    357: 0, 358: 0, 360: 0, 364: 0, 377: 0, 391: 0,   # KEGELN1 (bowling activity)
    362: 1, 384: 1,                                    # ICH (Speaker A)
    368: 2, 369: 2,                                    # VERBAND (association/organization)
    367: 3, 385: 3, 395: 3,                            # PUNKT (point/score)
    386: 4, 387: 4, 396: 4,                            # SPIELEN (playing)
    390: 5                                             # WETTKAMPF (competition)
}

pred_clusters_cz9 = [
    [357, 358, 360, 364, 377, 391],  # bowling activity
    [362, 384],                      # Speaker A (ICH)
    [368, 369],                     # association/organization
    [367, 385, 395],                # point/score
    [386, 387, 396],                # playing
    [390]                          # competition
]
mention_to_pred_entity_cz10 = {
    397: 0, 399: 0,                    # MIT1A (with/together)
    398: 1, 401: 1, 403: 1,           # HÖREND1A (hearing people)
    412: 2, 443: 2,                   # ICH1 (I / speaker)
    417: 3,                          # MEISTERSCHAFT1 (championship)
    424: 4, 441: 4,                   # KEGELN1 (bowling)
    404: 5, 449: 5, 457: 5,           # ALLE1A (everyone/all)
    413: 6, 447: 6,                   # KAMPF1A (fight/competition)
    423: 7, 425: 7, 427: 7, 431: 7, 436: 7,  # $LIST1 (list items)
    450: 8,                          # WETTKAMPF2 (competition)
    461: 9                           # KAMERAD1 (comrade)
}

pred_clusters_cz10 = [
    [397, 399],                         # MIT1A
    [398, 401, 403],                   # HÖREND1A
    [412, 443],                       # ICH1
    [417],                           # MEISTERSCHAFT1
    [424, 441],                       # KEGELN1
    [404, 449, 457],                   # ALLE1A
    [413, 447],                       # KAMPF1A
    [423, 425, 427, 431, 436],         # $LIST1
    [450],                          # WETTKAMPF2
    [461]                           # KAMERAD1
]
mention_to_pred_entity_cz11 = {
    496: 0, 503: 0, 508: 0,  # ICH2#496, ICH1#503, ICH1#508 — same "I" entity (Speaker A)
}

pred_clusters_cz11 = [
    [496, 503, 508],  # cluster for "I" entity (Speaker A)
]

mention_to_pred_entity_cz12 = {
    512: 0, 518: 0, 533: 0, 537: 0, 579: 0,          # GEBÄRDEN1A (sign language)
    513: 1, 519: 1, 538: 1,                          # DOZENT1 (lecturer)
    517: 2, 521: 2, 541: 2, 543: 2, 546: 2, 549: 2, 552: 2, 557: 2, 559: 2, 566: 2, 581: 2,  # ICH1 & ICH2 (Speaker A)
    548: 3, 558: 3, 563: 3, 572: 3, 577: 3,          # FINGERALPHABET1 (fingerspelling)
    527: 4,                                          # MEIN1 (Speaker A's)
    535: 5,                                          # DU1 (Speaker B)
    580: 6,                                          # LEHRER5 (teacher)
}

pred_clusters_cz12 = [
    [512, 518, 533, 537, 579],       # sign language
    [513, 519, 538],                 # lecturer
    [517, 521, 541, 543, 546, 549, 552, 557, 559, 566, 581],  # Speaker A (ICH1, ICH2)
    [548, 558, 563, 572, 577],       # fingerspelling
    [527],                          # Speaker A's (MEIN1)
    [535],                          # Speaker B (DU1)
    [580],                          # teacher (LEHRER5)
]
mention_to_pred_entity_cz13 = {
    584: 0, 596: 0, 601: 0,    # ICH2 (Speaker A)
}

pred_clusters_cz13 = [
    [584, 596, 601],           # Speaker A (ICH2)
]
mention_to_pred_entity_cf1 = {
    2: 0, 5: 0, 8: 0, 13: 0, 16: 0, 23: 0, 30: 0,   # Entity 0: ICH (I)
    19: 1, 26: 1                                    # Entity 1: SCHULE (school)
}
pred_clusters_cf1 = [
    [2, 5, 8, 13, 16, 23, 30],    # Entity 0: ICH (I)
    [19, 26]                     # Entity 1: SCHULE (school)
]
mention_to_pred_entity_cf2 = {
    37: 0, 52: 0, 58: 0,                      # Entity 0: I (the speaker)
    42: 1, 62: 1,                             # Entity 1: Deaf club
    41: 2, 49: 2,                             # Entity 2: Deaf or hard of hearing people
    43: 3, 47: 3, 69: 3,                      # Entity 3: Swimming
    68: 4                                     # Entity 4: Training
}
pred_clusters_cf2 = [
    [37, 52, 58],             # Entity 0: I (the speaker)
    [42, 62],                 # Entity 1: Deaf club
    [41, 49],                 # Entity 2: Deaf or hard of hearing people
    [43, 47, 69],             # Entity 3: Swimming
    [68]                      # Entity 4: Training
]
mention_to_pred_entity_cf3 = {
    82: 0, 88: 0, 98: 0,                      # Entity 0: I
    72: 1, 92: 1, 116: 1,                     # Entity 1: Young people
    81: 2, 120: 2                             # Entity 2: Adults
}
pred_clusters_cf3 = [
    [82, 88, 98],             # Entity 0: I
    [72, 92, 116],            # Entity 1: Young people
    [81, 120]                 # Entity 2: Adults
]
mention_to_pred_entity_cf4 = {
    138: 0, 150: 0,                      # Entity 0: Ich (I)
    139: 1, 142: 1, 146: 1               # Entity 1: Kegeln (Bowling)
}
pred_clusters_cf4 = [
    [138, 150],                         # Entity 0: Ich (I)
    [139, 142, 146]                     # Entity 1: Kegeln (Bowling)
]
mention_to_pred_entity_cf5 = {
    156: 0, 160: 0, 167: 0, 170: 0, 174: 0, 180: 0, 182: 0, 184: 0, 191: 0, 196: 0, 202: 0,  # Entity 0: I (speaker)
    158: 1, 161: 1,                                                       # Entity 1: Hamburg
    163: 2, 169: 2, 172: 2, 222: 2, 225: 2, 231: 2,                                         # Entity 2: Swimming
    166: 3,                                                                                # Entity 3: Championship
    165: 4,                                                                                # Entity 4: German
    164: 5, 177: 5, 187: 5                                                                 # Entity 5: Race
}
pred_clusters_cf5 = [
    [156, 160, 167, 170, 174, 180, 182, 184, 191, 196, 202],  # Entity 0: I (speaker)
    [158, 161,],                               # Entity 1: Hamburg
    [163, 169, 172, 222, 225, 231],                          # Entity 2: Swimming
    [166],                                                  # Entity 3: Championship
    [165],                                                  # Entity 4: German
    [164, 177, 187]                                          # Entity 5: Race
]
mention_to_pred_entity_cf6 = {
    235: 0, 242: 0, 251: 0, 260: 0,        # Entity 0: Speaker A (as "you" or "I")
    257: 1,                                # Entity 1: Speaker B (as "I")
    252: 2, 256: 2, 261: 2                 # Entity 2: Swimming
}
pred_clusters_cf6 = [
    [235, 242, 251, 260],  # Entity 0: Speaker A
    [257],                # Entity 1: Speaker B
    [252, 256, 261]       # Entity 2: Swimming
]
mention_to_pred_entity_cf7 = {
    268: 0, 276: 0, 307: 0, 309: 0,           # Entity 0: Speaker A
    282: 1, 283: 1, 287: 1, 303: 1, 305: 1,   # Entity 1: Speaker B
    266: 2, 270: 2, 322: 2,                   # Entity 2: Kampf (Fight)
    278: 3, 291: 3                            # Entity 3: Wasser (Water)
}
pred_clusters_cf7 = [
    [268, 276, 307, 309],              # Entity 0: Speaker A
    [282, 283, 287, 303, 305],         # Entity 1: Speaker B
    [266, 270, 322],                   # Entity 2: Kampf (Fight)
    [278, 291]                         # Entity 3: Wasser (Water)
]
mention_to_pred_entity_cf8 = {
    327: 0, 331: 0, 341: 0, 344: 0,        # Entity 0: #TRAINING
    328: 1, 330: 1, 345: 1,                # Entity 1: SCHWIMMEN (Swimming)
    349: 2,                                # Entity 2: #MEIN (My)
    351: 3                                 # Entity 3: #ICH (I)
}
pred_clusters_cf8 = [
    [327, 331, 341, 344],    # Entity 0: #TRAINING
    [328, 330, 345],         # Entity 1: SCHWIMMEN (Swimming)
    [349],                  # Entity 2: #MEIN (My)
    [351]                   # Entity 3: #ICH (I)
]
mention_to_pred_entity_cf9 = {
    362: 0, 384: 0,                        # Entity 0: Ich (I)
    357: 1, 358: 1, 360: 1, 364: 1, 377: 1, 391: 1,  # Entity 1: Kegeln (Bowling)
    368: 2, 369: 2,                      # Entity 2: Verband (Association)
    390: 3                              # Entity 3: Wettkampf (Competition)
}
pred_clusters_cf9 = [
    [362, 384],                         # Entity 0: Ich (I)
    [357, 358, 360, 364, 377, 391],    # Entity 1: Kegeln (Bowling)
    [368, 369],                        # Entity 2: Verband (Association)
    [390]                             # Entity 3: Wettkampf (Competition)
]
mention_to_pred_entity_cf10 = {
    398: 0, 401: 0, 403: 0,                   # Entity 0: Hearing People
    423: 1, 425: 1, 427: 1, 431: 1, 436: 1, 438: 1,  # Entity 1: List Reference
    424: 2, 441: 2,                           # Entity 2: Kegeln (Bowling)
    404: 3, 440: 3, 449: 3, 457: 3,           # Entity 3: All
    412: 4, 443: 4,                           # Entity 4: I (Speaker A)
    413: 5, 447: 5                            # Entity 5: Competition
}
pred_clusters_cf10 = [
    [398, 401, 403],                          # Entity 0: Hearing People
    [423, 425, 427, 431, 436, 438],           # Entity 1: List Reference
    [424, 441],                              # Entity 2: Kegeln (Bowling)
    [404, 440, 449, 457],                    # Entity 3: All
    [412, 443],                             # Entity 4: I (Speaker A)
    [413, 447]                              # Entity 5: Competition
]

mention_to_pred_entity_cf11 = {
    487: 0,       # Entity 0: Wir (We)
    496: 1, 503: 1, 508: 1   # Entity 1: Ich (I)
}
pred_clusters_cf11 = [
    [487],            # Entity 0: Wir (We)
    [496, 503, 508]   # Entity 1: Ich (I)
]
mention_to_pred_entity_cf12 = {
    512: 4, 513: 4, 518: 4, 519: 4, 537: 4, 538: 4, 579: 4, 580: 4,  # Entity 4: sign language teacher related
    517: 0, 521: 0, 541: 0, 543: 0, 546: 0, 549: 0, 552: 0, 557: 0, 559: 0, 566: 0, 581: 0,  # Entity 0: Speaker A
    535: 1,  # Entity 1: Addressee DU
    527: 2, 528: 2,  # Entity 2: Speaker A's life partner
    548: 5, 558: 5, 563: 5, 572: 5, 577: 5,  # Entity 5: Finger alphabet
    564: 6, 567: 6, 571: 6  # Entity 6: Practicing/exercising
}
pred_clusters_cf12 = [
    [517, 521, 541, 543, 546, 549, 552, 557, 559, 566, 581],  # Entity 0: Speaker A
    [535],  # Entity 1: Addressee DU
    [527, 528],  # Entity 2: Speaker A's life partner
    [512, 513, 518, 519, 537, 538, 579, 580],  # Entity 4: Sign language teacher related
    [548, 558, 563, 572, 577],  # Entity 5: Finger alphabet
    [564, 567, 571]  # Entity 6: Practicing/exercising
]
mention_to_pred_entity_cf13 = {
    584: 0, 596: 0, 601: 0,      # Entity 0: 'Ich' (I)
    
}
pred_clusters_cf13 = [
    [584, 596, 601],     # Entity 0: 'Ich' (I)
]
