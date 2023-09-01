from generic_app.models import *

from generic_app.submodels.windparkconsolidator.models.accounts.Account import Account
class Transaction(UploadModelMixin, CalculatedModelMixin, Model):
    
    id = AutoField(primary_key=True)
    transaction_id = TextField()
    account = ForeignKey(to=Account, on_delete=CASCADE)
    amount = FloatField()
    date = DateTimeField()
    
    def update(self):
        pass

    defining_fields = ['transaction_id', 'account', 'amount', 'date']

    def get_selected_key_list(key):
        
        if key == 'transaction_id':
            # Define objects that will initialize the field transaction_id e.g.
            # return Class.objects.all()
            pass

        if key == 'account':
            # Define objects that will initialize the field account e.g.
            # return Class.objects.all()
            pass

        if key == 'amount':
            # Define objects that will initialize the field amount e.g.
            # return Class.objects.all()
            pass

        if key == 'date':
            # Define objects that will initialize the field date e.g.
            # return Class.objects.all()
            pass

    def calculate(self):
        pass
