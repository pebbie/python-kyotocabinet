from kyotocabinet import *
import sys

# define the functor
def dbproc(db):

  # store records
  db['foo'] = b'step';   # string is fundamental
  db[u'bar'] = 'hop';    # unicode is also ok
  db[3] = 'jump';        # number is also ok

  # retrieve a record value
  print db['foo']

  # update records in transaction
  def tranproc():
      db['foo'] = 2.71828
      return True
  db.transaction(tranproc)

  # multiply a record value
  def mulproc(key, value):
      return float(value) * 2
  db.accept('foo', mulproc)

  # traverse records by iterator
  for key in db:
      print "%s:%s" % (key, db[key])

  # upcase values by iterator
  def upproc(key, value):
      return value.upper()
  db.iterate(upproc)

  # traverse records by cursor
  def curproc(cur):
      cur.jump()
      def printproc(key, value):
          print "%s:%s" % (key, value)
          return Visitor.NOP
      while cur.accept(printproc):
          cur.step()
  db.cursor_process(curproc)

# process the database by the functor
DB.process(dbproc, 'casket.kch')
