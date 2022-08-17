import pandas as pd
import numpy as np


from sklearn.metrics.pairwise import cosine_similarity


df=pd.read_csv("webtoon_total_final.csv")
df = df[['title','score', 'genre']]
df.genre = df.genre.str.strip('['']')


tmp = pd.get_dummies(df.genre)


def col_change(df):
    for col in df.columns:
        if ',' in col:
            col_sep = col.split(', ')
            df[col_sep[0]] = df[col_sep[0]] + df[col]
            df[col_sep[1]] = df[col_sep[1]] + df[col]
            df.drop(columns=[f'{col}'], inplace=True)
    return df
 
 
col_change(tmp)


genre_df = col_change(pd.get_dummies(df.genre))
df = pd.concat([df.title, df.score, genre_df], axis=1)

df.columns = df.columns.str.strip('\'')


score = genre_df.to_numpy()

def genre_model(title_list):
    local_score = np.append(score, genres(title_list), axis=0)
    cosine_similar = cosine_similarity(local_score, local_score)
    cosine_similar_data = pd.DataFrame(cosine_similar)

    genre_user = cosine_similar_data.tail(1).T.sort_values(by=cosine_similar_data.columns[-1], ascending=False)
    max_score = genre_user.values[1][0]
    
    max_index = list(genre_user[(genre_user.values) == max_score].index)

    if df.shape[0] in max_index:
        max_index.remove(df.shape[0])

    sorted_df = df.loc[max_index].sort_values(by='score', ascending=False)

    if len(max_index) < 10:
        return sorted_df
    
    else:
        return sorted_df[:10]
def one_genre(title):
    g_row = df[df.title == title]
    genres = g_row[df.columns[2:]]
    return genres.values

def genres(title_list):
    genre_list = [0]*9
    for title in title_list:
        genre_list = genre_list + one_genre(title)
    return genre_list
    
    
