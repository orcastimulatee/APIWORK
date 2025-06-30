#These are all the clusters that LLMs out put during the experiment.

pred_clusters_dz1 = [
    [1, 4, 7, 12, 15, 22, 29, 34, 49, 55],    # Cluster 1: ICH
    [31],                                    # Cluster 2: ELTERN
    [10, 38, 46],                            # Cluster 3: TAUB-GEHÖRLOS
    [18, 25],                                # Cluster 4: SCHULE
    [11],                                    # Cluster 5: GEBÄRDEN
    [39, 59],                                # Cluster 6: VEREIN
    [47],                                    # Cluster 7: PERSON
    [52],                                    # Cluster 8: ALL
    [54],                                    # Cluster 9: JUNG
]

# Mapping each mention ID to its predicted cluster index (0-based)
mention_to_pred_entity_dz1 = {
    1: 0,  4: 0,  7: 0, 12: 0, 15: 0, 22: 0, 29: 0, 34: 0, 49: 0, 55: 0,
    31: 1,
    10: 2, 38: 2, 46: 2,
    18: 3, 25: 3,
    11: 4,
    39: 5, 59: 5,
    47: 6,
    52: 7,
    54: 8,
}

# Predicted clusters as lists of mention IDs (numbers after the “#”)
pred_clusters_df1 = [
    [35, 60, 62],                             # Cluster 0
    [1, 4, 7, 12, 15, 22, 29, 34, 49, 55],    # Cluster 1
    [31],                                     # Cluster 2
    [16, 27],                                 # Cluster 3
    [18, 25],                                 # Cluster 4
    [38, 46, 10],                             # Cluster 5
    [39, 59],                                 # Cluster 6
]

# Mapping each mention ID (the number after “#”) to its predicted cluster index
mention_to_pred_entity_df1 = {
    35: 0,
    60: 0,
    62: 0,
    1:  1,
    4:  1,
    7:  1,
    12: 1,
    15: 1,
    22: 1,
    29: 1,
    34: 1,
    49: 1,
    55: 1,
    31: 2,
    16: 3,
    27: 3,
    18: 4,
    25: 4,
    38: 5,
    46: 5,
    10: 5,
    39: 6,
    59: 6,
}

# Predicted clusters as lists of mention IDs (numbers after “#”)
pred_clusters_dz2 = [
    [55, 79, 85, 95, 129],                                  # Cluster 1: Speaker
    [54, 69, 89, 113],                                      # Cluster 2: Youth
    [78, 117],                                              # Cluster 3: Adults
    [60, 62, 68, 71, 84],                                   # Cluster 4: Indexed Entities
    [87, 114, 122],                                         # Cluster 5: Groups
    [110],                                                  # Cluster 6: Deaf Community
    [59, 64, 76, 81, 86, 98, 125, 80, 103, 126, 66, 119],   # Cluster 7: Activities/Objects
]

# Mapping each mention ID to its predicted cluster index (0-based)
mention_to_pred_entity_dz2 = {
    55:  0,  79:  0,  85:  0,  95:  0, 129:  0,
    54:  1,  69:  1,  89:  1, 113:  1,
    78:  2, 117:  2,
    60:  3,  62:  3,  68:  3,  71:  3,  84:  3,
    87:  4, 114:  4, 122:  4,
    110: 5,
    59:  6,  64:  6,  76:  6,  81:  6,  86:  6,  98:  6, 125: 6,
    80:  6, 103:  6, 126:  6,  66:  6, 119:  6,
}

# Predicted clusters as lists of mention IDs (numbers after “#”)
pred_clusters_df2 = [
    [60],   # Cluster 0
    [55],   # Cluster 1
    [62],   # Cluster 2
    [68],   # Cluster 3
    [71],   # Cluster 4
    [79],   # Cluster 5
    [84],   # Cluster 6
    [85],   # Cluster 7
    [95],   # Cluster 8
    [129],  # Cluster 9
]

# Mapping each mention ID to its predicted cluster index
mention_to_pred_entity_df2 = {
    60:  0,
    55:  1,
    62:  2,
    68:  3,
    71:  4,
    79:  5,
    84:  6,
    85:  7,
    95:  8,
    129: 9,
}

# Predicted clusters as lists of mention IDs
pred_clusters_dz3 = [
    [135, 147],  # Cluster 1: First-Person Speaker
    [138, 148],  # Cluster 2: Other Entities (Member, Knee)
]

# Mapping each mention ID to its predicted cluster index
mention_to_pred_entity_dz3 = {
    135: 0,
    147: 0,
    138: 1,
    148: 1,
}

# Predicted clusters as lists of mention IDs (numbers after “#”)
pred_clusters_df3 = [
    [135, 147],  # Cluster 0: The signer (first person)
    [137],       # Cluster 1: The duration of ten years
    [143],       # Cluster 2: The activity of bowling
]

# Mapping each mention ID to its predicted cluster index
mention_to_pred_entity_df3 = {
    135: 0,
    147: 0,
    137: 1,
    143: 2,
}

# Predicted clusters as lists of mention IDs (numbers after “#”)
pred_clusters_dz4 = [
    [153, 157, 164, 167, 171, 177, 179, 181, 188, 193, 199],  # Cluster 0: Signer (ICH1/ICH2)
    [155, 158],                                               # Cluster 1: Hamburg (place)
    [161, 162, 163],                                          # Cluster 2: German Championship (event)
    [172],                                                    # Cluster 3: Limit/GRENZE
    [174],                                                    # Cluster 4: Start signal/STARTSCHUSS
    [184],                                                    # Cluster 5: Goal/ZIEL
    [186],                                                    # Cluster 6: Others/ZUSAMMEN-PERSON
    [213],                                                    # Cluster 7: Success/ERFOLG
    [212],                                                    # Cluster 8: Place/PLATZ (ranking)
]

# Mapping each mention ID to its predicted cluster index
mention_to_pred_entity_dz4 = {
    153: 0, 157: 0, 164: 0, 167: 0, 171: 0, 177: 0, 179: 0, 181: 0, 188: 0, 193: 0, 199: 0,
    155: 1, 158: 1,
    161: 2, 162: 2, 163: 2,
    172: 3,
    174: 4,
    184: 5,
    186: 6,
    213: 7,
    212: 8,
}

# Predicted clusters as lists of mention IDs (numbers after “#”)
pred_clusters_df4 = [
    [153, 157, 164, 167, 171, 177, 179, 181, 188, 193, 199],  # Cluster 0: Signer (ICH variants)
    [155, 158],                                               # Cluster 1: Hamburg (place)
    [156, 159, 165],                                          # Cluster 2: Dort / Dorthin-gehen (place & movement)
    [160, 166, 169, 219, 222, 228],                          # Cluster 3: Schwimmen (activity)
    [162],                                                    # Cluster 4: Deutsch (language descriptor)
    [163],                                                    # Cluster 5: Meisterschaft (event)
    [184],                                                    # Cluster 6: Ziel (finish line)
    [212],                                                    # Cluster 7: Platz (ranking)
    [213],                                                    # Cluster 8: Erfolg (conceptual entity)
]

# Mapping each mention ID to its predicted cluster index
mention_to_pred_entity_df4 = {
    153: 0, 157: 0, 164: 0, 167: 0, 171: 0, 177: 0, 179: 0, 181: 0, 188: 0, 193: 0, 199: 0,
    155: 1, 158: 1,
    156: 2, 159: 2, 165: 2,
    160: 3, 166: 3, 169: 3, 219: 3, 222: 3, 228: 3,
    162: 4,
    163: 5,
    184: 6,
    212: 7,
    213: 8,
}

# Predicted clusters as lists of mention IDs (numbers after “#”)
pred_clusters_dz5 = [
    [546, 553, 562],                      # Cluster 0: Speaker B
    [238, 242, 245, 257, 259, 587, 589],  # Cluster 1: Speaker A
    [247, 581],                           # Cluster 2: Water
    [574],                                # Cluster 3: Land
    [251],                                # Cluster 4: Sport
    [240, 272],                           # Cluster 5: Competition
    [246, 571],                           # Cluster 6: Fun/Enjoyment
    [265, 266, 267],                      # Cluster 7: Private/Free time
]

# Mapping each mention ID to its predicted cluster index (0-based)
mention_to_pred_entity_dz5 = {
    546: 0, 553: 0, 562: 0,
    238: 1, 242: 1, 245: 1, 257: 1, 259: 1, 587: 1, 589: 1,
    247: 2, 581: 2,
    574: 3,
    251: 4,
    240: 5, 272: 5,
    246: 6, 571: 6,
    265: 7, 266: 7, 267: 7,
}

# Predicted clusters as lists of mention IDs (numbers after “#”)
pred_clusters_df5 = [
    [248, 582, 585],                         # Cluster 0: Index referring to an entity
    [546, 553, 562],                         # Cluster 1: Listener or addressee (you)
    [238, 559, 572, 573, 577, 242, 245, 257],# Cluster 2: The speaker (I)
    [259, 587, 589],                         # Cluster 3: The speaker in a different context (I2)
    [247, 581],                              # Cluster 4: Water
    [567, 240, 272],                         # Cluster 5: Competition context
    [554, 558, 563, 255, 268],               # Cluster 6: Swimming
    [557, 570, 564, 243],                    # Cluster 7: Back-and-forth movement/action
]

# Mapping each mention ID to its predicted cluster index (0-based)
mention_to_pred_entity_df5 = {
    248: 0, 582: 0, 585: 0,
    546: 1, 553: 1, 562: 1,
    238: 2, 559: 2, 572: 2, 573: 2, 577: 2, 242: 2, 245: 2, 257: 2,
    259: 3, 587: 3, 589: 3,
    247: 4, 581: 4,
    567: 5, 240: 5, 272: 5,
    554: 6, 558: 6, 563: 6, 255: 6, 268: 6,
    557: 7, 570: 7, 564: 7, 243: 7,
}

# Predicted clusters as lists of mention IDs (numbers after “#”)
pred_clusters_cz1 = [
    [1, 4, 7, 12, 15, 22, 29, 34, 49, 55],  # Cluster 0: First Person Pronoun
    [31],                                   # Cluster 1: Parents
    [10, 38, 46],                           # Cluster 2: Deaf/Deaf People
    [47],                                   # Cluster 3: Person/People
    [39, 59],                               # Cluster 4: Club/Association
]

# Mapping each mention ID to its predicted cluster index (0-based)
mention_to_pred_entity_cz1 = {
    1: 0,  4: 0,  7: 0, 12: 0, 15: 0, 22: 0, 29: 0, 34: 0, 49: 0, 55: 0,
    31: 1,
    10: 2, 38: 2, 46: 2,
    47: 3,
    39: 4, 59: 4,
}

# Predicted clusters as lists of mention IDs (numbers after “#”)
pred_clusters_cf1 = [
    [1, 4, 7, 12, 15, 22, 29, 34, 49, 55],  # Cluster 0: the speaker
    [31, 35, 60, 62],                       # Cluster 1: the speaker's parents
    [18, 25],                               # Cluster 2: school
    [39, 59],                               # Cluster 3: deaf club
]

# Mapping each mention ID to its predicted cluster index (0-based)
mention_to_pred_entity_cf1 = {
    1: 0,  4: 0,  7: 0, 12: 0, 15: 0, 22: 0, 29: 0, 34: 0, 49: 0, 55: 0,
    31: 1,  35: 1, 60: 1, 62: 1,
    18: 2,  25: 2,
    39: 3,  59: 3,
}

# Predicted clusters as lists of mention IDs (numbers after “#”)
pred_clusters_cz2 = [
    [55, 79, 85, 95],     # Cluster 0: ICH (I/me)
    [54, 69, 89, 113],    # Cluster 1: JUNG (young/youth)
    [59],                 # Cluster 2: VEREIN (club/association)
    [68],                 # Cluster 3: JUGENDLEITER (youth leader)
    [78, 117],            # Cluster 4: ERWACHSENE (adult)
    [110],                # Cluster 5: TAUB-GEHÖRLOS (deaf)
    [129],                # Cluster 6: WIR (we)
    [124],                # Cluster 7: ZUG (train)
    [122],                # Cluster 8: MASSE-PERSON (group of people)
]

# Mapping each mention ID to its predicted cluster index (0-based)
mention_to_pred_entity_cz2 = {
    55:  0,  79:  0,  85:  0,  95:  0,
    54:  1,  69:  1,  89:  1, 113:  1,
    59:  2,
    68:  3,
    78:  4, 117:  4,
    110: 5,
    129: 6,
    124: 7,
    122: 8,
}

# Predicted clusters as lists of mention IDs (numbers after “#”)
pred_clusters_cf2 = [
    [55, 79, 85, 95],   # Cluster 0: I / me
    [60],               # Cluster 1: previously mentioned entity
    [62],               # Cluster 2: currently mentioned entity
    [68],               # Cluster 3: youth leader
    [71],               # Cluster 4: another mentioned entity
    [78, 117],          # Cluster 5: adults
    [84],               # Cluster 6: another mentioned entity
    [87],               # Cluster 7: everyone
    [113],              # Cluster 8: youth / young people
    [114],              # Cluster 9: all
    [129],              # Cluster 10: we
]

# Mapping each mention ID to its predicted cluster index (0-based)
mention_to_pred_entity_cf2 = {
    55:  0,  79:  0,  85:  0,  95:  0,
    60:  1,
    62:  2,
    68:  3,
    71:  4,
    78:  5, 117: 5,
    84:  6,
    87:  7,
    113: 8,
    114: 9,
    129: 10,
}

# Predicted clusters as lists of mention IDs (numbers after “#”)
pred_clusters_cz3 = [
    [135, 147],  # Cluster 0: I / me
    [137],       # Cluster 1: ten years
    [138],       # Cluster 2: member
    [148],       # Cluster 3: knee
]

# Mapping each mention ID to its predicted cluster index (0-based)
mention_to_pred_entity_cz3 = {
    135: 0,
    147: 0,
    137: 1,
    138: 2,
    148: 3,
}

# Predicted clusters as lists of mention IDs (numbers after “#”)
pred_clusters_cf3 = [
    [135, 147],      # Cluster 0: the speaker
    [136, 139, 143], # Cluster 1: bowling
    [137],           # Cluster 2: ten years
    [138],           # Cluster 3: member
    [148],           # Cluster 4: knee
]

# Mapping each mention ID to its predicted cluster index (0-based)
mention_to_pred_entity_cf3 = {
    135: 0,
    147: 0,
    136: 1,
    139: 1,
    143: 1,
    137: 2,
    138: 3,
    148: 4,
}

# Predicted clusters as lists of mention IDs (numbers after “#”)
pred_clusters_cz4 = [
    [153, 157, 164, 167, 171, 177, 179, 181, 188, 193, 199],  # Cluster 0: ICH (I)
    [155, 158],                                              # Cluster 1: HAMBURG (Hamburg)
    [156, 159],                                              # Cluster 2: DORT (There)
    [160, 166, 169, 219, 222, 228],                          # Cluster 3: SCHWIMMEN (Swimming)
    [191, 215],                                              # Cluster 4: $INDEX1 (This/That)
    [192, 202, 214, 229],                                    # Cluster 5: FERTIG (Finished/Done)
    [151, 175, 203, 208],                                    # Cluster 6: $GEST-OFF (Gesture Off)
    [168, 170],                                              # Cluster 7: $PROD (Product/Production)
    [226, 227],                                              # Cluster 8: ZEIT (Time)
]

# Mapping each mention ID to its predicted cluster index (0-based)
mention_to_pred_entity_cz4 = {
    153: 0, 157: 0, 164: 0, 167: 0, 171: 0, 177: 0, 179: 0, 181: 0, 188: 0, 193: 0, 199: 0,
    155: 1, 158: 1,
    156: 2, 159: 2,
    160: 3, 166: 3, 169: 3, 219: 3, 222: 3, 228: 3,
    191: 4, 215: 4,
    192: 5, 202: 5, 214: 5, 229: 5,
    151: 6, 175: 6, 203: 6, 208: 6,
    168: 7, 170: 7,
    226: 8, 227: 8,
}

# Predicted clusters as lists of mention IDs (numbers after “#”)
pred_clusters_cf4 = [
    [153, 157, 164, 167, 171, 177, 179, 181, 188, 193, 199],  # Cluster 0
    [155, 156, 158, 159],                                    # Cluster 1
    [162],                                                   # Cluster 2
    [163],                                                   # Cluster 3
    [184],                                                   # Cluster 4
    [186],                                                   # Cluster 5
    [191],                                                   # Cluster 6
    [215],                                                   # Cluster 7
]

# Mapping each mention ID to its predicted cluster index (0-based)
mention_to_pred_entity_cf4 = {
    153: 0, 157: 0, 164: 0, 167: 0, 171: 0, 177: 0, 179: 0, 181: 0, 188: 0, 193: 0, 199: 0,
    155: 1, 156: 1, 158: 1, 159: 1,
    162: 2,
    163: 3,
    184: 4,
    186: 5,
    191: 6,
    215: 7,
}

# Predicted clusters as lists of mention IDs (numbers after “#”)
pred_clusters_cz5 = [
    [546, 553, 562],                      # Cluster 0: DU1 (you)
    [238, 242, 245, 572, 573, 577, 257],  # Cluster 1: ICH1 (I)
    [554, 563, 255, 268],                 # Cluster 2: SCHWIMMEN1 (swimming)
    [240, 567, 272],                      # Cluster 3: KAMPF1A (competition)
    [247, 581],                           # Cluster 4: WASSER1 (water)
    [267],                                # Cluster 5: FREIZEIT1B (leisure)
    [246, 571],                           # Cluster 6: SPASS1 (fun)
    [557, 564, 243, 570],                 # Cluster 7: HIN-UND-HER1 (back-and-forth)
    [551, 237, 236],                      # Cluster 8: ALT (age)
    [584, 586],                           # Cluster 9: FLEISSIG1 (diligent)
    [258, 262, 269],                      # Cluster 10: GERN1 (like)
    [552, 273],                           # Cluster 11: SCHLUSS1 (end)
    [251],                                # Cluster 12: SPORT4B (sport)
    [265],                                # Cluster 13: PRIVAT1A (private)
    [248, 254, 585],                      # Cluster 14: $INDEX1 (index)
    [560, 578, 583],                      # Cluster 15: $PROD (product)
]

# Mapping each mention ID to its predicted cluster index (0-based)
mention_to_pred_entity_cz5 = {
    546: 0, 553: 0, 562: 0,
    238: 1, 242: 1, 245: 1, 572: 1, 573: 1, 577: 1, 257: 1,
    554: 2, 563: 2, 255: 2, 268: 2,
    240: 3, 567: 3, 272: 3,
    247: 4, 581: 4,
    267: 5,
    246: 6, 571: 6,
    557: 7, 564: 7, 243: 7, 570: 7,
    551: 8, 237: 8, 236: 8,
    584: 9, 586: 9,
    258: 10, 262: 10, 269: 10,
    552: 11, 273: 11,
    251: 12,
    265: 13,
    248: 14, 254: 14, 585: 14,
    560: 15, 578: 15, 583: 15,
}

# Predicted clusters as lists of mention IDs (numbers after “#”)
pred_clusters_cf5 = [
    [546, 553, 562],                                        # Cluster 0: You
    [238, 242, 245, 257, 259, 559, 572, 573, 577, 587, 589],# Cluster 1: I
    [0, 4, 248, 582, 585],                                  # Cluster 2: Index
]

# Mapping each mention ID to its predicted cluster index (0-based)
mention_to_pred_entity_cf5 = {
    546: 0, 553: 0, 562: 0,
    238: 1, 242: 1, 245: 1, 257: 1, 259: 1, 559: 1, 572: 1, 573: 1, 577: 1, 587: 1, 589: 1,
    0:   2, 4:   2, 248: 2, 582: 2, 585: 2,
}
