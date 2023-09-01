from generic_app.models import *

class Quarter(UploadModelMixin, CalculatedModelMixin, Model):
    
    id = AutoField(primary_key=True)
    quarter_id = TextField()
    date = DateTimeField()
    
    def update(self):
        """ Every quarter, the financial data from the wind parks is uploaded and consolidated. This includes actual and forecasted cashflows. """
        pass

    defining_fields = ['quarter_id', 'date']

    def get_selected_key_list(key):
        
        if key == 'quarter_id':
            # Define objects that will initialize the field quarter_id e.g.
            # return Class.objects.all()
            pass

        if key == 'date':
            # Define objects that will initialize the field date e.g.
            # return Class.objects.all()
            pass

    def calculate(self):
        pass
