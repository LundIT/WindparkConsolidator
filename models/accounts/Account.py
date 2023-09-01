from generic_app.models import *

class Account(Model):
    
    id = AutoField(primary_key=True)
    account_id = TextField()
    account_name = TextField()
    