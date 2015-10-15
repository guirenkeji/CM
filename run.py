# -*- coding: UTF-8 -*- 

from configmanage import create_configmanage_app
from configmanage.cmconfig import *

app = create_configmanage_app()

if __name__ == '__main__':
    app.debug = DEBUG
    app.run(host= HOST,port=PORT)
