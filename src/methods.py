import sqlite3


def get_all_from_table(table_name):
    return [(1, 1),(2,'j','b'), (3, 2)]

def complete_order(order_id, pmt_type_id):
    return (1, 3,'2016-01-21', 5, '2017-01-01')
    
def get_active_customer_order(customer_id):
    return 1

def flush_table(table_name):
    conn = sqlite3.connect('db.sqlite3')    
    c = conn.cursor()
    command = "DROP TABLE IF EXISTS {}".format(table_name)
    c.execute(command)
    conn.commit()
    conn.close()
    
def save_to_db(table, values):
    return 1

