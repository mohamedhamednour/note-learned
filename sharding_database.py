from django.db import connections, transaction
from yourapp.models import User  # نموذج المستخدم

NUM_SHARDS = 4

def get_shard(user_id):
    return user_id % NUM_SHARDS

def migrate_users():
    # نسحب المستخدمين من shard_0
    old_db = 'shard_0'
    cursor_old = connections[old_db].cursor()
    
    cursor_old.execute('SELECT id, username, email FROM yourapp_user')
    rows = cursor_old.fetchall()
    
    for row in rows:
        user_id, username, email = row
        shard_id = get_shard(user_id)
        new_db = f'shard_{shard_id}'

        # ندخل المستخدم في قاعدة البيانات الجديدة
        with transaction.atomic(using=new_db):
            cursor_new = connections[new_db].cursor()
            cursor_new.execute(
                'INSERT INTO yourapp_user (id, username, email) VALUES (%s, %s, %s)',
                [user_id, username, email]
            )
    print('Migration completed.')
