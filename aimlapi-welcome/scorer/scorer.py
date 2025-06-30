import sys
from collections import Counter
import numpy as np
from scipy.optimize import linear_sum_assignment
"https://github.com/ns-moosavi/coval"
#kk
def f1(p_num, p_den, r_num, r_den, beta=1):
    p = 0 if p_den == 0 else p_num / float(p_den)
    r = 0 if r_den == 0 else r_num / float(r_den)
    return (0 if p + r == 0
            else (1 + beta * beta) * p * r / (beta * beta * p + r))

class Evaluator:
    def __init__(self, metric, beta=1):
        self.p_num = 0
        self.p_den = 0
        self.r_num = 0
        self.r_den = 0
        self.metric = metric
        self.beta = beta

    def update(self, mention_to_key_entity, pred_clusters, mention_to_pred_entity, key_clusters):

        if self.metric == ceafe:
            pn, pd, rn, rd = self.metric(pred_clusters, key_clusters)
        else:
            pn, pd = self.metric(pred_clusters, mention_to_key_entity)
            rn, rd = self.metric(key_clusters, mention_to_pred_entity)
        self.p_num += pn
        self.p_den += pd
        self.r_num += rn
        self.r_den += rd

    def get_f1(self):
        return f1(self.p_num,
                self.p_den,
                self.r_num,
                self.r_den,
                beta=self.beta)

    def get_recall(self):
        return 0 if self.r_num == 0 else self.r_num / float(self.r_den)

    def get_precision(self):
        return 0 if self.p_num == 0 else self.p_num / float(self.p_den)


def evaluate_documents(mention_to_key_entity, pred_clusters, mention_to_pred_entity, key_clusters, metric):
    evaluator = Evaluator(metric)
    evaluator.update(mention_to_key_entity, pred_clusters, mention_to_pred_entity, key_clusters)
    return (evaluator.get_recall(), evaluator.get_precision(),
            evaluator.get_f1())


def b_cubed(clusters, mention_to_gold):
    num, den = 0, 0

    for c in clusters:
        gold_counts = Counter()
        correct = 0
        for m in c:
            if m in mention_to_gold:
                gold_counts[mention_to_gold[m]] += 1
        for c2 in gold_counts:
            correct += gold_counts[c2] * gold_counts[c2]

        num += correct / float(len(c))
        den += len(c)

    return num, den

def muc(clusters, mention_to_gold):
    tp, p = 0, 0
    for c in clusters:
        p += len(c) - 1
        tp += len(c)
        linked = set()
        for m in c:
            if m in mention_to_gold:
                linked.add(mention_to_gold[m])
            else:
                tp -= 1
        tp -= len(linked)
    return tp, p

def phi4(c1, c2):
    return 2 * len([m for m in c1 if m in c2]) / float(len(c1) + len(c2))

def phi3(c1, c2):
    return len([m for m in c1 if m in c2])

def ceafe(clusters, gold_clusters):
    clusters = [c for c in clusters]
    scores = np.zeros((len(gold_clusters), len(clusters)))
    for i in range(len(gold_clusters)):
        for j in range(len(clusters)):
            scores[i, j] = phi4(gold_clusters[i], clusters[j])
    row_ind, col_ind = linear_sum_assignment(-scores)
    similarity = scores[row_ind, col_ind].sum()
    return similarity, len(clusters), similarity, len(gold_clusters)


def main():
    
    allmetrics = [('muc', muc),('bcub', b_cubed), ('ceafe', ceafe)]

    mention_to_key_entity = sys.argv[0]
    pred_clusters = sys.argv[1]
    mention_to_pred_entity = sys.argv[2]
    key_clusters = sys.argv[3]

    conll = 0
    conll_subparts_num = 0

    for name, metric in allmetrics:
        
        recall, precision, f1 = evaluate_documents(mention_to_key_entity, pred_clusters, mention_to_pred_entity, key_clusters, metric)
        
        if name in ["muc", "bcub", "ceafe"]:
            conll += f1
            conll_subparts_num += 1

        print(name.ljust(10), 'Recall: %.2f' % (recall * 100),
                ' Precision: %.2f' % (precision * 100),
                ' F1: %.2f' % (f1 * 100))

    if conll_subparts_num == 3:
        conll = (conll / 3) * 100
        print('CoNLL score: %.2f' % conll)


if __name__ == '__main__':
    
    # ground truth from the json file
    mention_to_key_entity = {"m1": 0, "m2": 1, "m3":1, "m4":2, "m5":2, "m6":2} 
    key_clusters = [["m1"], ["m2", "m3"], ["m4", "m5", "m6"]]
    
    # resolved entities by LLM
    pred_clusters = [["m1"], ["m4", "m5"]]
    # resolved mentions with their entity ids
    mention_to_pred_entity = {"m1":0, "m4":2, "m5":2}
    
    sys.argv = [mention_to_key_entity, pred_clusters, mention_to_pred_entity, key_clusters]
    main()


"""@InProceedings{moosavi2019minimum,
    author = { Nafise Sadat Moosavi, Leo Born, Massimo Poesio and Michael Strube},
    title = {Using Automatically Extracted Minimum Spans to Disentangle Coreference Evaluation from Boundary Detection},
    year = {2019},
    booktitle = {Proceedings of the 57th Annual Meeting of
		the Association for Computational Linguistics (Volume 1: Long Papers)},
    publisher = {Association for Computational Linguistics},
    address = {Florence, Italy},
}"""