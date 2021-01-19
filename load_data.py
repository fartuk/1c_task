import pandas as pd


def taiga_to_df(dir_path, rubric_list=[]):
    meta_df = pd.read_csv('{}/newmetadata.csv'.format(dir_path))
    if len(rubric_list) > 0:
        meta_df = meta_df[meta_df['textrubric'].apply(lambda x: True if x in rubric_list else False)]
    text_arr = []
    for text_id in meta_df['textid'].values:
        with open('{}/texts/{}.txt'.format(dir_path, text_id)) as f:
            text = f.read()
            text_arr.append(text)

    df = pd.DataFrame()
    df['text'] = text_arr
        
    return df


def chat_to_df(dir_path):
    meta = pd.read_csv('{}/newmetadata.csv'.format(dir_path), sep='\t')
    meta = meta[meta['languages']=='ru']
    meta['filepath'] = meta['filepath'].apply(lambda x: '{}/{}'.format(x.split(' - ')[0].strip(), x))

    text_arr = []
    for text_path in meta['filepath']:
        try:
            with open('{}/texts/{}'.format(dir_path, text_path)) as f:
                text = ' '.join(pd.read_csv('{}/texts/{}'.format(dir_path, text_path), sep='	', header=None)[:-3][3].values)
                text = text.replace('- ', '')
                text = text.replace('<i>', '')
                text = text.replace('</i>', '')
                text_arr.append(text)
        except:
            None
            
    df = pd.DataFrame()
    df['text'] = text_arr
    
    return df