import pandas as pd 


df = pd.read_csv("all_results.csv") 

for col in ['precision', 'recall', 'f1']:
    df[col] = df[col].str.rstrip('%').astype(float)


df['group_short'] = df['group'].str[:2]


results = []


for group in sorted(df['group_short'].unique()):
    group_df = df[df['group_short'] == group]

    avg_metrics = {}
    for metric in ['muc', 'bcub', 'ceafe']:
        metric_df = group_df[group_df['metric'] == metric]
        avg_precision = metric_df['precision'].mean()
        avg_recall = metric_df['recall'].mean()
        avg_f1 = metric_df['f1'].mean()
        avg_metrics[metric] = {
            'precision': avg_precision,
            'recall': avg_recall,
            'f1': avg_f1
        }

    # 
    conll_precision = (avg_metrics['muc']['precision'] +
                       avg_metrics['bcub']['precision'] +
                       avg_metrics['ceafe']['precision']) / 3
    conll_recall = (avg_metrics['muc']['recall'] +
                    avg_metrics['bcub']['recall'] +
                    avg_metrics['ceafe']['recall']) / 3
    conll_f1 = (avg_metrics['muc']['f1'] +
                avg_metrics['bcub']['f1'] +
                avg_metrics['ceafe']['f1']) / 3

    results.append({
        'group': group.upper(),
        'MUC_P': avg_metrics['muc']['precision'],
        'MUC_R': avg_metrics['muc']['recall'],
        'MUC_F1': avg_metrics['muc']['f1'],
        'B3_P': avg_metrics['bcub']['precision'],
        'B3_R': avg_metrics['bcub']['recall'],
        'B3_F1': avg_metrics['bcub']['f1'],
        'CEAFe_P': avg_metrics['ceafe']['precision'],
        'CEAFe_R': avg_metrics['ceafe']['recall'],
        'CEAFe_F1': avg_metrics['ceafe']['f1'],
        'CoNLL_P': conll_precision,
        'CoNLL_R': conll_recall,
        'CoNLL_F1': conll_f1
    })

results_df = pd.DataFrame(results)
pd.set_option('display.float_format', '{:.2f}'.format)
print(results_df)


results_df.to_csv("coref_metric_summary.csv", index=False)
