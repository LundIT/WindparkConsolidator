from generic_app.models import *

from generic_app.submodels.windparkconsolidator.uploads.quarters.Quarter import Quarter
class Report(CalculatedModelMixin, Model):
    
    id = AutoField(primary_key=True)
    report_id = TextField()
    quarter = ForeignKey(to=Quarter, on_delete=CASCADE)
    file = FileField()
    
    defining_fields = ['report_id', 'quarter', 'file']

    def get_selected_key_list(key):
        
        if key == 'report_id':
            # Define objects that will initialize the field report_id e.g.
            # return Class.objects.all()
            pass

        if key == 'quarter':
            # Define objects that will initialize the field quarter e.g.
            # return Class.objects.all()
            pass

        if key == 'file':
            # Define objects that will initialize the field file e.g.
            # return Class.objects.all()
            pass

    def calculate(self):
        """ After the data is consolidated, a report is generated. This report is an Excel file that contains the consolidated transactions. The file is then saved in the 'file' field of the Report model. """
        pass
