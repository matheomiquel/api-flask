from __main__ import *

prefix = "/truc"
@app.route(prefix + "/", methods=['GET'])
def bijour():
    data = request.data
    return 'The URL for this page is {}'.format(url_for('bijour'))