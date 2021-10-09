from django.db import models
from django.forms import ModelForm

# Create your models here.


# here we define the database tables
class DatabaseModel(models.Model):
    # define the table's columns and their types
    col_str = models.CharField(max_length=20)
    col_num = models.FloatField()
    col_date = models.DateField()

    class Meta:
        # db_table tells Django which MySQL table to use in the database
        db_table = "sample_tbl"
