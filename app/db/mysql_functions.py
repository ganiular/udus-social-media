from app.db import get_db

def get_user_by_email(email, cur):
    cur.execute(
        'select * from user where email=%s limit 1',
        (email,))
    return cur.fetchone()

def register_user(record, cur):
    fields = ''
    places_holder = ''
    for key in record:
        fields += key + ','
        places_holder += '%s,'
    cur.execute(
        f'insert into user({fields[:-1]}) values({places_holder[:-1]})',
        tuple(record.values())
    )
