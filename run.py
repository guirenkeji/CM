# -*- coding: UTF-8 -*- 

from configmanage import create_configmanage_app
from configmanage.cmconfig import *
from configmanage import mesoscollet
from configmanage import marathoncollet

app = create_configmanage_app()

if __name__ == '__main__':
#     app.debug = DEBUG
#     app.run(host= HOST,port=PORT)
      mesoscollet.create()
      marathoncollet.marathoncollet()