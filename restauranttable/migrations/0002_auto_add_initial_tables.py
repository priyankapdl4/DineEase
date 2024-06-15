from django.db import migrations

def create_initial_tables(apps, schema_editor):
    Table = apps.get_model('restauranttable', 'Table')
    tables = [
        {'number': 1, 'seats': 4},
        {'number': 2, 'seats': 2},
        {'number': 3, 'seats': 6},
        {'number': 4, 'seats': 4},
        {'number': 5, 'seats': 2},
        {'number': 6, 'seats': 4},
        
    ]
    for table in tables:
        Table.objects.create(number=table['number'], seats=table['seats'])

class Migration(migrations.Migration):

    dependencies = [
        ('restauranttable', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_tables),
    ]
