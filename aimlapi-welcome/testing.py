import re

def extract_labels_from_unit(unit):
    """
    根据单位字符串，返回 (label_A, label_B)
    规则：
    - 如果单位里有 '【#XXX'，表示A和B都标记了XXX -> (XXX, XXX)
    - 如果单位里只有 '#XXX'（但没有 '【#'），表示只有B标注 -> (None, XXX)
    - 如果单位没有任何标签，返回 (None, None)
    """
    # 找所有【#XXX
    labels_both = re.findall(r'【#([A-Z0-9]+)\*?', unit)
    # 找所有单独的 #XXX，但前面不是【#
    labels_b_only = re.findall(r'(?<!【)#([A-Z0-9]+)\*?', unit)
    
    if labels_both:
        # 假设只有一个共同标签，取第一个
        label = labels_both[0]
        return (label, label)
    elif labels_b_only:
        label = labels_b_only[0]
        return (None, label)
    else:
        return (None, None)

# 测试一下：
units = [
    '【#ICH1',
    '#SCHULE3',
    'AUFWACHSEN1A',
    '【#ICH2',
    '$GEST-OFF^',
    'GEBÄRDEN1A*'
]

for u in units:
    a, b = extract_labels_from_unit(u)
    print(f"Unit: {u} -> A: {a}, B: {b}")
