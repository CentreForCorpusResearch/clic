import os
import operator

from cheshire3.baseObjects import Session
from cheshire3.document import StringDocument
from cheshire3.internal import cheshire3Root
from cheshire3.server import SimpleServer

# FIXME make relative
cheshirePath = os.path.join('HOME', '/home/cheshire')

class Clusters(object):

    def __init__(self):
        # TODO compare with concordance init
        self.session = Session()
        self.session.database = 'db_dickens'
        # TODO read this config
        self.serv = SimpleServer(self.session,
                            os.path.join(cheshire3Root, 'configs', 'serverConfig.xml')
                            )
        self.db = self.serv.get_object(self.session, self.session.database)
        self.qf = self.db.get_object(self.session, 'defaultQueryFactory')
        self.resultSetStore = self.db.get_object(self.session, 'resultSetStore')
        self.idxStore = self.db.get_object(self.session, 'indexStore')
        self.logger = self.db.get_object(self.session, 'clusterLogger') ## added to dbs/dickens/config.xml

    def list_clusters(self, idxName, Materials):
        # TODO activate logging
        #self.logger.log(10, 'CREATING CLUSTERS FOR RS: {0} in {1}'.format(idxName, Materials))
        session = self.session
        db = self.db

        clauses = []
        for Material in Materials:
            if Material in ['dickens', 'ntc']:
                MatIdx = 'subCorpus-idx'
            else:
                MatIdx = 'book-idx'
            clauses.append('c3.{0} = "{1}"'.format(MatIdx, Material))

        query = self.qf.get_query(session,
                                       ' or '.join(clauses)
                                       )
        print query
        # TODO is db.search different from query we used before?
        results = db.search(session, query)

        idx = db.get_object(session, idxName)
        facets = idx.facets(session, results)
        # FIXME do not use built_in names
        dict = {}
        for x in facets:
            dict[x[0]] = x[1][2]

        cluster_list = []
        for term, freq in dict.iteritems():
            if freq >= 2:
                prop = (float(freq)/float(len(dict))) * 100
                cluster_list.append(['', term, freq, str(prop)[:5]])  ## add empty array node at beginning (see Pete email 23.04.14)

        cluster_list.sort(key=operator.itemgetter(2), reverse=True)

        if len(cluster_list) <= 5000:
            return cluster_list
        else:
            # TODO make this a round number
            return cluster_list[0:4999]