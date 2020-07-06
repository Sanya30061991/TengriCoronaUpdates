import sqlite3

dart = sqlite3.connect('db.db')
con = dart.cursor()

def db_out():
    con.execute('SELECT * from `users`')
    r = con.fetchall()
    return r

def db_get(exp,eql):
    con.execute(f"SELECT * from `users` WHERE {exp}='{eql}'")
    r = con.fetchone()
    return r

def db_get_all(exp,eql):
    con.execute(f"SELECT * from `users` WHERE {exp}='{eql}'")
    r = con.fetchall()
    return r

def db_update(exp,eql,st1,val1,st2='',val2='',st3='',val3='',st4='',val4=''):
    if st2=='' and val2=='':
        con.execute(f'UPDATE `users` SET \'{st1}\'=\'{val1}\' WHERE {exp}=\'{eql}\'')
        dart.commit()
    elif st3=='' and val3=='':
        con.execute(f'UPDATE `users` SET \'{st1}\'=\'{val1}\',\'{st2}\'=\'{val2}\' WHERE {exp}=\'{eql}\'')
        dart.commit()
    elif st4=='' and val4=='':
        con.execute(f'UPDATE `users` SET \'{st1}\'=\'{val1}\',\'{st2}\'=\'{val2}\',\'{st3}\'=\'{val3}\' WHERE {exp}=\'{eql}\'')
        dart.commit()
    else:
        con.execute(f'UPDATE `users` SET \'{st1}\'=\'{val1}\',\'{st2}\'=\'{val2}\',\'{st3}\'=\'{val3}\',\'{st4}\'=\'{val4}\' WHERE {exp}=\'{eql}\'')
        dart.commit()

def db_insert(exp1,exp2='FALSE',exp3='english'):
    con.execute(f'INSERT into `users` (\'tel_id\',\'sub\',\'lang\') VALUES (\'{exp1}\',\'{exp2}\',\'{exp3}\')')
    dart.commit()
