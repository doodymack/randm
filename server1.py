# https://github.com/andrewbeattycourseware/datarepresentation/blob/main/code/Topic10-getlippy/application.py

from flask import Flask, jsonify, abort, request
from votedao import voteDAO

app = Flask(__name__, static_url_path='', static_folder='static')

episodes = [
    {'name':'S1E1: PILOT'},
    {'name':'S1E2: Lawnmower Dog'},
    {'name':'S1E3: Anatomy Park'},
    {'name':'S1E4: M. Night Shaym-Aliens'},
    {'name':'S1E5: Meseeks and Destroy'},
    {'name':'S1E6: Rick Potion #9'},
    {'name':'S1E7: Raising Gazorpazorp'},
    {'name':'S1E8: Rixty Business'},
    {'name':'S1E9: Something Ricked This Way Comes'},
    {'name':'S1E10: Close Rick-counters of the Rick Kind'},
    {'name':'S1E11: Ricksy Business'},
    ]

@app.route('/band', methods=['GET'])
def getAllepisodes():
    return jsonify(episodes)

@app.route('/vote/<episode>', methods=['POST'])
def voteForEpisode(episode):
    ip_addr = request.remote_addr
    data = (episode, ip_addr)
    newid = voteDAO.create(data)

    return jsonify({'id':newid})

@app.route('/vote/<episode>', methods=['GET'])
def getCountForBand(episode):
    count = voteDAO.countvotes(episode)
    return jsonify({episode:count})

@app.route('/vote', methods=['GET'])
def getAllCount():
    allcounts = []
    for band in episodes:
        episode = band['name'] 
        count = voteDAO.countvotes(episode)
        allcounts.append({episode:count})
    return jsonify(allcounts)

@app.route('/vote/all', methods=['delete'])
def deleteAllVote():
    return jsonify({'done':True})



if __name__ == "__main__":
    app.run(debug=True)













































































