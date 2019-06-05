'''
Created on 2019. 6. 5.

@author: 073860
'''

import threading
from flask import Flask
from GETSTOCK import GetHKConsenStock
from GETSTOCK import STATES

app = Flask(__name__)

@app.route('/getstock')
def getStock():
    
    if(STATES.starting==0):
        STATES.starting=1
        print "=== [ Get Stock List Method Start ] ==="
        t = threading.Thread(target=GetHKConsenStock.main)
        #GetHKConsenStock.main()
        t.start()
        return '=== [ Get Stock List Method Start ] ==='
    
    else:
        print "=== [ Get Stock List is Already Started ] ==="
        return ' Get Stock List is Already Started '

if __name__ == '__main__':
    print "### Flask Server Start ###"
    app.run()

