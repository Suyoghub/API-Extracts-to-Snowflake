import pandas as pd
import requests

url = "https://api.themoviedb.org/3/discover/movie"
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmODdiZWVmMmFkZDMwNTdjMTBjZDBiMWU3NzBhOTgzZSIsIm5iZiI6MTcyMjE0MTE2MS4yNDEwMDQsInN1YiI6IjY2YTU0MGI5MTgyNjk2NGJhN2M2Mjg3MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.5iZCvaHsSkRuYtgPjaxaT5NKdZd33ATXuHFHZzlp-b0",
    "accept": "application/json"
}
params = {
    "include_adult": "false",
    "include_video": "false",
    "language": "en-US",
    "sort_by": "vote_average.desc",
    "without_genres": "99,10755",
    "vote_count.gte": 200
}
df = pd.DataFrame()

for i in range(1, 20):
    params["page"] = i
    response = requests.get(url, headers=headers, params=params)
    formatted_response = response.json()
    temp_df = pd.DataFrame(formatted_response['results'])[['id', 'title', 'overview', 'release_date', 'popularity', 'vote_average', 'vote_count']]
    df = pd.concat([df, temp_df], ignore_index=True)

# df.header.upper_case()
df.to_csv('toprated_movies.csv',encoding='utf-8', index=False)



