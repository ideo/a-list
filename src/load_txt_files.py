import pandas as pd
import pathlib


def read_dir_text_files(data_dir, verbose=True):

    skiplist = ['.DS_Store', "index.txt", "index.csv", "index", "index_0.csv"]

#     articles = {}
    files = []
    texts = []
    p = pathlib.Path(data_dir)
    for article_path in p.glob('*'):
        if article_path.is_dir():
            continue
        fname = article_path.name
        fname = fname.split('.txt')[0]
        if fname in skiplist:
            continue
        txt = article_path.read_text()
        files.append(fname)
        texts.append(txt)
    if verbose:
        print(f"{len(texts)} docs found in {data_dir}")
    return files, texts


def add_files_from_dir(paths, verbose=True):

    all_files, all_docs, all_paths = [], [], []
    for p in paths:
        files, docs = read_dir_text_files(p, verbose=verbose)
        all_files += files
        all_docs += docs
        all_paths +=  ([p.split('/')[-2]] * len(docs)) # repeates the name of the directory for each item

    return all_files, all_docs, all_paths


def assemble_index_files(input_paths, drop_dups=True):
    indexes = []
    for p in input_paths:
        dirname = pathlib.Path(p).name
        index_path = pathlib.Path(f"{p}/index.csv")
        if not index_path.exists():
            print(f"index.csv does not exist in {p}")

        df_index_part = pd.read_csv(index_path)
        # df_index_part['group'] = dirname
        print(p, len(df_index_part))
        indexes.append(df_index_part)


    df_index = pd.concat(indexes, axis=0)
    fnames = [str(f).split('.txt')[0] for f in df_index['filename']]
    df_index['filename'] = fnames
    df_index_a = df_index.drop(columns=['Unnamed: 0'])

    df_index_a['year'] = df_index_a['year'].fillna(0).astype(int)

    new_titles = []
    df_index_a.rename(columns={'title': 'headline'}, inplace=True)
    for i, row in df_index_a.iterrows():
        name = row['name']
        year = row['year']
        new_titles.append(f"{name} ({year})")
    df_index_a['title'] = new_titles

    # df_index_a['year'] = df_index_a['year'].astype(int)
    # Watch out! Duplicates!
    #The how I built this is messy! there's a couple episodes with the same people that then overwrite their files.
    #quickfix is I'm removing them from the index for now. longer fix would be to actually fix things and give them slightly different names

    if drop_dups:
        df_index_a = check_filename_index_conflicts(df_index_a)
    return df_index_a


def check_filename_index_conflicts(df_index):

    # reporting
    before_dedupe = df_index['filename'].value_counts()
    dups = []
    for k, v in before_dedupe.items():
        if v > 1:
            dups.append((k, v))
    if len(dups):
        print(f'{len(dups)} filenames with overlapping index')
        for d in dups:
            print(f"{d[0]}: {d[1]} references")

        print('\nremoving duplicates from index')
        return df_index.drop_duplicates(subset=['filename'], keep="last")

    return df_index