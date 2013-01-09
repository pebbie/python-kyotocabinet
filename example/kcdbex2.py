from kyotocabinet import *
import sys

# create the database object
db = DB()

# open the database
if not db.open("casket.kch", DB.OREADER):
    print >>sys.stderr, "open error: " + str(db.error())

# define the visitor
class VisitorImpl(Visitor):
    # call back function for an existing record
    def visit_full(self, key, value):
        print "%s:%s" % (key, value)
        return self.NOP
    # call back function for an empty record space
    def visit_empty(self, key):
        print >>sys.stderr, "%s is missing" % key
        return self.NOP
visitor = VisitorImpl()

# retrieve a record with visitor
if not db.accept("foo", visitor, False) or \
        not db.accept("dummy", visitor, False):
    print >>sys.stderr, "accept error: " + str(db.error())

# traverse records with visitor
if not db.iterate(visitor, False):
    print >>sys.stderr, "iterate error: " + str(db.error())

# close the database
if not db.close():
    print >>sys.stderr, "close error: " + str(db.error())
