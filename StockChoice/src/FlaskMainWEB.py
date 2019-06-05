'''
Created on 2019. 6. 5.

@author: 073860
'''

from flask import Flask
from GETSTOCK import GetHKConsenStock

app = Flask(__name__)

@app.route('/getConsen')
def hello_world():
    print "#### Flask Start ###"
    GetHKConsenStock.main()
    
    return 'Hello Flask'

if __name__ == '__main__':
  app.run()

