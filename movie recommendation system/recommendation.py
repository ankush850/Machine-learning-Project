import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


def build_recommender(dataframe, content_columns, name_column):
    dataframe = dataframe.copy()
    for col in content_columns:
        dataframe[col] = dataframe[col].fillna('')
    dataframe['content'] = ''
    for col in content_columns:
        dataframe['content'] = dataframe['content'] + ' ' + dataframe[col].astype(str)

    vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
    tfidf_matrix = vectorizer.fit_transform(dataframe['content'])

    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    indices = pd.Series(dataframe.index, index=dataframe[name_column]).drop_duplicates()

    def recommend(item_name, top_n=5):
        if item_name not in indices:
            return f"⚠️ '{item_name}' not found in dataset."
        idx = indices[item_name]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:top_n+1]
        item_indices = []
        for i in sim_scores:
            item_indices.append(i[0])
        recommendations = dataframe[name_column].iloc[item_indices].tolist()
        output_lines = []
        counter = 1
        for rec in recommendations:
            line = str(counter) + ". " + rec
            output_lines.append(line)
            counter += 1
        return "\n".join(output_lines)

    return recommend


games_df = pd.read_csv("steam.csv")
recommend_game = build_recommender(games_df, ['developer','publisher','release_date'], 'name')

movies_df = pd.read_csv("netflix_titles.csv")
recommend_movie = build_recommender(movies_df, ['director','cast','listed_in','description'], 'title')

print("🎮 Games similar to Counter-Strike:\n")
print(recommend_game("Counter-Strike", 10))

print("\n🎬 Movies similar to Inception:\n")
print(recommend_movie("Inception", 10))
