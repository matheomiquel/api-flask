from flask import Flask, request, abort, jsonify, url_for
import json
app = Flask(__name__)

from __init__ import *



#import controller
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/vga'
db = SQLAlchemy(app)
import model
import controller
data = {}

# import declared routes
test = (model.vga.CUSTOMER.query.all())
for truc in test:
    del(truc._sa_instance_state)
    data[truc] = ((truc.__dict__))
print(data)
#db.session.query(User).all()
#print(*test, sep = ", ")  
#import test

if __name__ == "__main__":
    app.run(debug=True)
