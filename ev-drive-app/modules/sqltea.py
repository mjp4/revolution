import sqlite3
import time
import threading

def main():
  print "1"
  db = Database("Tea.db")
  print "2"
  db.insert_employee('rpo', 'Rob', 'Riverside')
  db.insert_employee('rpo', 'Rob', 'Riverside')
  db.insert_employee('NL3', 'Nian', 'Riverside')
  print "3"
  db.update_keen('rpo', True)
  db.update_keen('NL3', True)
  print "4"
  print db.select('Riverside', 1)
  print "5"
  #timeout_check = timeout_thread("Tea.db", 2)
  #timeout_check.start()  # 1800000

  time.sleep(10)
  print db.select('Riverside', 1)
  db.destroy()
  print "done"

class Database:
  """
  database object
  """

  def __init__(self, dbname):
    """
    Initializes the database
    """
    self.conn = sqlite3.connect(dbname)
    self.cur = self.conn.cursor()
    try:
      self.cur.execute("CREATE TABLE employees (initials text PRIMARY KEY, name text, office text, keen text, starttime real);")
    except:
      pass
    self.conn.commit()

  def insert_employee(self, initials, name, office):
    try:
      cmd = "INSERT into employees (initials, name, office, keen, starttime) VALUES ("
      #default keenness = "FALSE"
      cmd += "'" + initials + "', '" + name + "', '" + office + "', 'FALSE'," + str(time.time()) + ");"
      self.cur.execute(cmd)
    except sqlite3.IntegrityError:
      cmd = "UPDATE employees SET name = '" + name + "', office = '" + office + "' WHERE initials = '" + initials + "';"
      self.cur.execute(cmd)
    self.conn.commit()


  def select(self, office, time_out_window):
    """
    time_out_window is in seconds
    """
    print "in select"
    print "office: {}".format(office)
    time_out_point = time.time() - time_out_window
    cmd = "SELECT initials FROM employees WHERE office = '" + office + "' AND keen = 'TRUE' AND starttime > " + str(time_out_point) + ";"
    self.cur.execute(cmd)

    rows = self.cur.fetchall()
    print "rows"
    updated_rows = []
    i = 0
    for row in rows:
      updated_rows.append(rows[i][0])
      i += 1
    return updated_rows

  def update_keen(self, initials, keen):
    if keen == True:
      cmd = "UPDATE employees SET keen = 'TRUE' WHERE initials = '" + initials + "';"
      self.cur.execute(cmd)
      cmd = "UPDATE employees SET starttime = " + str(time.time()) + " WHERE initials = '" + initials + "';"
      self.cur.execute(cmd)
      self.conn.commit()
    elif keen == False:
      cmd = "UPDATE employees SET keen = 'FALSE' WHERE initials = '" + initials + "';"
      self.cur.execute(cmd)
      cmd = "UPDATE employees SET starttime = " + str(time.time()) + " WHERE initials = '" + initials + "';"
      self.cur.execute(cmd)
      self.conn.commit()
    else:
      print "You've fucked up the keen field"

  def timeout(self, time_out_window):
    time_out_point = time.time() - time_out_window

    cmd = "UPDATE employees SET keen = 'FALSE', starttime = " + str(time.time()) + " WHERE starttime < " + str(time_out_point) + ";"
    #cmd = "UPDATE employees SET starttime = " + str(time.time()) + " WHERE initials = '" + initials + "';"
    self.cur.execute(cmd)
    self.conn.commit()

  def close(self):
    self.conn.close()

  def drop(self):
    try:
      self.cur.execute("DROP TABLE employees")
    except:
      pass

  def destroy(self):
    self.drop()
    self.close()

class timeout_thread(threading.Thread):
  """
  continuously checks for timeouts
  """
  def __init__(self, db_name, time_out_window):
    threading.Thread.__init__(self)
    self.lock = threading.Lock()
    self.db = Database(db_name)
    self.time_out_window = time_out_window

  def run(self):
    while True:
      time.sleep(1)
      if self.db:
        self.db.timeout(self.time_out_window)
      else:
        self.db.close()
        break

if __name__ == "__main__":
  main()
