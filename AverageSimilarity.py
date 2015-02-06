import sys
import dill

# note: the version in my notebook uses movie name, not ID
def average_similarity(movie_id_1, movie_id_2, svd, n=5):
    NUM_MOVIES = 3883
    
    if movie_id_1 == movie_id_2:
        similar = svd.similar(movie_id_1, n=NUM_MOVIES)[1:]
        return [lookup_name(movie[0]) for movie in similar][:n+1]
    try:
        similar_1 = svd.similar(movie_id_1, n=NUM_MOVIES)[1:]
        similar_2 = svd.similar(movie_id_2, n=NUM_MOVIES)[1:]
    except:
        return ["Error in computing average similarity."]
    
    # construct dictionary of average ratings
    norm_1 = similar_1[0][1]
    norm_2 = similar_2[0][1]
    average = {}
    similar_1 = dict(similar_1)
    similar_2 = dict(similar_2)
    # delete the original movies themselves from each other dictionary
    similar_1.pop(movie_id_2)
    similar_2.pop(movie_id_1)
    
    for movie_id, rating in similar_1.items():
        average[movie_id] = (rating/norm_1 + similar_2[movie_id]/norm_2)/2

    # return names of the highest ranking movies
    top_n = sorted(average.items(), key=lambda x: x[1], reverse=True)[:n+1]
    d = dill.load(open("static/d.dill"))
    return [d[movie[0]].title() for movie in top_n]
