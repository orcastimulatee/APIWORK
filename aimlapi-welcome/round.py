# run_all.py run to get the data result.
import csv
from scorer.scorer import evaluate_documents, muc, b_cubed, ceafe
import result_Ju
import true_result_Ju

def normalize_clusters(raw):
    if isinstance(raw, dict):
        return list(raw.values())
    return raw

metrics = [
    ('muc', muc),
    ('bcub', b_cubed),
    ('ceafe', ceafe),
]
groups = ['dz', 'df', 'cz', 'cf']

with open('all_results.csv', 'w', newline='', encoding='utf-8') as fout:
    writer = csv.writer(fout)
    writer.writerow(['group','fold','metric','recall','precision','f1'])

    for fold in range(1, 14):
        
        raw_key_clusters = getattr(true_result_Ju, f'key_clusters_{fold}')
        key_clusters     = normalize_clusters(raw_key_clusters)

        mention_to_key = getattr(true_result_Ju, f'mention_to_key_entity_{fold}')

        for grp in groups:
            pred_clusters       = getattr(result_Ju, f'pred_clusters_{grp}{fold}')
            mention_to_pred_ent = getattr(result_Ju, f'mention_to_pred_entity_{grp}{fold}')

            for name, fn in metrics:
                r, p, f = evaluate_documents(
                    mention_to_key,
                    pred_clusters,
                    mention_to_pred_ent,
                    key_clusters,      # <--normalised list
                    fn
                )
                writer.writerow([
                    grp, fold, name,
                    f'{r*100:.2f}%', f'{p*100:.2f}%', f'{f*100:.2f}%'
                ])

print("Done! all results seen in: all_results.csv")
