from __main__ import *
prefix = "/test"
@app.route(prefix + "/", methods=['GET'])
def wesh():
    data = request.data
    return 'The URL for this page is {}'.format(url_for('wesh'))



@app.route(prefix + "/read", methods=['GET'])
def tri():
    data = {}
    test = (model.vga.CUSTOMER.query.all())
    for truc in test:
        del(truc._sa_instance_state)
        print(json.dump())
        #print((truc.__dict__))
#    print(data.__dict__)
    return "bijour"