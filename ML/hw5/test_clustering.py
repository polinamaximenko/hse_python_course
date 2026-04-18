import pandas as pd
import numpy as np
from typing import List
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score

# Тест 1: Проверка загрузки данных
def test_data_loading(df_filepath: str, feature_cols: List):
    df = pd.read_csv(df_filepath)
    assert df is not None
    assert df.shape[0] > 100, "Датасет слишком маленький"
    assert not df[feature_cols].isnull().any().any(), "Есть пропуски в данных"

# Тест 2: Проверка масштабирования
def test_scaling(df_filepath: str, feature_cols: List):
    df = pd.read_csv(df_filepath)
    X = df[feature_cols].dropna()
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    assert np.allclose(X_scaled.mean(axis=0), 0, atol=1e-10)
    assert np.allclose(X_scaled.std(axis=0), 1, atol=1e-10)

# Тест 3: Проверка метрик качества
def test_clustering_quality(df_filepath: str, feature_cols: List, optimal_k: int):
    df = pd.read_csv(df_filepath)
    X = df[feature_cols].dropna()

    kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X)

    silhouette = silhouette_score(X, labels)
    db_score = davies_bouldin_score(X, labels)

    assert silhouette > 0.2, f"Silhouette score {silhouette:.3f} < 0.2"
    assert db_score < 1.5, f"Davies-Bouldin score {db_score:.3f} > 1.5"

# Тест 4: Проверка функции рекомендаций
def test_recommendation_function(df_filepath: str):
    df = pd.read_csv(df_filepath)
    df['cluster'] = pd.read_csv('clusters.csv')['cluster']

    def recommend(item_id, df, n=5):
        cluster = df.loc[item_id, 'cluster']
        candidates = df[df['cluster'] == cluster]
        return candidates.drop(item_id).head(n)

    recs = recommend(0, df)
    assert len(recs) == 5
    assert recs.index[0] != 0
    assert (recs['cluster'] == df.loc[0, 'cluster']).all()

if __name__ == '__main__':
    df_filepath = 'movie_rec.csv'
    feature_cols = ['duration',
                    'imdb_score',
                    'Action',
                    'Adventure',
                    'Animation',
                    'Biography',
                    'Comedy',
                    'Crime',
                    'Drama',
                    'Family',
                    'Fantasy',
                    'History',
                    'Horror',
                    'Music',
                    'Musical',
                    'Mystery',
                    'Romance',
                    'Sci-Fi',
                    'Sport',
                    'Thriller',
                    'War',
                    'Western',
                    'is_english']
    optimal_k = 17
    test_data_loading(df_filepath, feature_cols)
    test_scaling(df_filepath, feature_cols)
    test_clustering_quality(df_filepath, feature_cols, optimal_k)
    test_recommendation_function(df_filepath)

