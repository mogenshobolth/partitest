from flask import Flask, render_template, request, session
from datetime import datetime
import pandas as pd

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\asd]/'

@app.route("/", methods=['POST', 'GET'])
def home():
    df = pd.read_csv('static/data_sample.csv')
    id = '1'
    navid = 1
    navid_prev = 1
    navid_next = 1
    vote = 4
    votes = {}
    rowno = 0
    no_votes = len(df.index)
    test_completed = False
    if request.method == 'POST':
        votes = session['votes']
        id = str(request.form['id'])
        vote = int(request.form['vote'])
        navid = int(request.form['navid'])
        rowno = df[df["id"] == navid].iloc[0].raekkenr
        if rowno == 0:
            navid_prev = navid
        else:
            navid_prev = df[df["raekkenr"] == rowno-1].iloc[0].id
        if rowno+1 == len(df.index):
            navid_next = navid
        else:
            navid_next = df[df["raekkenr"] == rowno+1].iloc[0].id
    else:
        id = str(df.iloc[0].id)
        navid = int(id)
        navid_prev = navid
        navid_next = df.iloc[1].id
    progress_bar = int(rowno/no_votes * 100)
    if navid == int(id) and rowno > 0:
        progress_bar = 100
        test_completed = True
    votes[id] = vote
    session['votes'] = votes
    id = navid
    if str(navid) in votes:
        vote = votes[str(navid)]
    else:
        vote = 4
    row = df[df["id"] == navid].head(1).iloc[0]
    similarity_ALT = calculateSimilarity(votes, df, 'ALT')
    similarity_EL = calculateSimilarity(votes, df, 'EL')
    similarity_SF = calculateSimilarity(votes, df, 'SF')
    similarity_RV = calculateSimilarity(votes, df, 'RV')
    similarity_S = calculateSimilarity(votes, df, 'S')
    similarity_V = calculateSimilarity(votes, df, 'V')
    similarity_KF = calculateSimilarity(votes, df, 'KF')
    similarity_DF = calculateSimilarity(votes, df, 'DF')
    similarity_NB = calculateSimilarity(votes, df, 'NB')
    return render_template(
        "partitest.html",
        vote=vote,
        id=id,
        ministeromraade=row.ministeromraade,
        titel = row.titel,
        resume = row.resume,
        navid_prev = navid_prev,
        navid_next = navid_next,
        date=datetime.now(),
        progress_bar=progress_bar,
        test_completed = test_completed,
        partier = ['ALT','EL', 'SF', 'RV', 'S', 'V', 'KF','DF','NB'],
        partienighed = [similarity_ALT, similarity_EL, similarity_SF, similarity_RV, similarity_S, similarity_V, similarity_KF, similarity_DF, similarity_NB]
    )

def calculateSimilarity(votes, df, party):
    total = 0
    count_similar = 0
    result = 0
    for k, v in votes.items():
        if v == 4:
            continue
        row = df[df["id"] == int(k)]
        if row['stem_' + party].iloc[0] == v:
            count_similar += 1
        total += 1
    if total > 0:
        result = int(count_similar / total * 100)
    return result
