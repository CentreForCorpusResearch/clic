import os
from lxml import etree
from crypt import crypt

import cheshire3

from cheshire3.baseObjects import Session
from cheshire3.server import SimpleServer
from cheshire3.internal import cheshire3Root
from cheshire3.document import StringDocument

session = Session()

serverConfig = os.path.join(cheshire3Root, 'configs', 'serverConfig.xml')
serv = SimpleServer(session, serverConfig)

print cheshire3Root

# db = serv.get_object(session, 'db_dickens')
# session.database = 'db_dickens'
# parser = db.get_object(session, "LxmlParser")
# recStore = db.get_object(session, "recordStore")
#  
# # establish objects for later use
# qf = db.get_object(session, 'defaultQueryFactory')
# df = db.get_object(session, 'defaultDocumentFactory')
#  
#  
# recStore = db.get_object(session, 'recordStore')
#  
# xmlp = db.get_object(session, 'LxmlParser')
#  
# recStore.clear(session)
#  
# db.clear_indexes(session)
# db.begin_indexing(session)
# recStore.begin_storing(session)
# data = "/home/aezros/clic/dbs/dickens/data/"
# df.load(session, data, cache=0 )
#  
# for doc in df:
#     print doc
#     rec = parser.process_document(session, doc)  # [1]
#     recStore.create_record(session, rec)         # [2]
#     db.add_record(session, rec)                  # [3]
#     db.index_record(session, rec)
# recStore.commit_storing(session)
# db.commit_metadata(session)
# db.commit_indexing(session)