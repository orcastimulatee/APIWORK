import pandas as pd

# set parameters.
dialogue_folds = {6, 7, 9, 10, 11}
monologue_folds = {1, 2, 3, 4, 5, 8, 12, 13}
target_groups = {'cz', 'cf', 'df', 'dz'}

# GET CSV
df = pd.read_csv('all_results.csv')

# clean the data
for col in ['recall', 'precision', 'f1']:
    df[col] = df[col].str.rstrip('%').astype(float)

# add dialogue/monologue
df['type'] = df['fold'].apply(lambda x: 'dialogue' if x in dialogue_folds else 'monologue')

# classification
results = {}

for group in target_groups:
    group_df = df[df['group'] == group]
    for t in ['dialogue', 'monologue']:
        type_df = group_df[group_df['type'] == t]
        avg_recall = type_df['recall'].mean()
        avg_precision = type_df['precision'].mean()
        avg_f1 = type_df['f1'].mean()
        results[(group, t)] = {
            'avg_recall': round(avg_recall, 2),
            'avg_precision': round(avg_precision, 2),
            'avg_f1': round(avg_f1, 2)
        }

# rusult
for group in target_groups:
    for t in ['dialogue', 'monologue']:
        data = results.get((group, t), {})
        print(f"{group.upper()} - {t.capitalize()}: Recall = {data.get('avg_recall', 0):.2f}%, "
            f"Precision = {data.get('avg_precision', 0):.2f}%, F1 = {data.get('avg_f1', 0):.2f}%")
