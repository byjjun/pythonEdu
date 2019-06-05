'''
Created on 2019. 6. 5.

@author: 073860
'''

from flask import Flask
from GETSTOCK import GetHKConsenStock

app = Flask(__name__)

@app.route('/getstock')
def hello_world():
    
    print "=== [ Get Stock Method Start ] ==="
    GetHKConsenStock.main()
    
    return 'Get Stock Complete'

if __name__ == '__main__':
    print "### Flask Server Start ###"
    app.run()

