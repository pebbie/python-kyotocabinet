from kyotocabinet import *
import sys

# create the database object
db = DB()

# open the database
if not db.open("casket.kch", DB.OWRITER | DB.OCREATE):
    print >>sys.stderr, "open error: " + str(db.error())

# store records
if not db.set("foo", "hop") or \
        not db.set("bar", "step") or \
        not db.set("baz", "jump"):
    print >>sys.stderr, "set error: " + str(db.error())

# retrieve records
value = db.get("foo")
if value:
    print value
else:
    print >>sys.stderr, "get error: " + str(db.error())

# traverse records
cur = db.cursor()
cur.jump()
while True:
    rec = cur.get(True)
    if not rec: break
    print rec[0] + ":" + rec[1]
cur.disable()

# close the database
if not db.close():
    print >>sys.stderr, "close error: " + str(db.error())
