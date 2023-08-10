# Generated by Django 4.2.3 on 2023-08-01 15:55

from django.db import migrations, models
import loan.models
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalLoan',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('principal', models.FloatField(default=10000, validators=[loan.models.validate_principal])),
                ('interest', models.FloatField(default=9)),
                ('months', models.IntegerField(default=0)),
                ('amount', models.FloatField(default=0)),
                ('emi', models.FloatField(default=0)),
                ('status', models.CharField(default='NEW', max_length=12)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('modified_date', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical loan',
                'verbose_name_plural': 'historical loans',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('principal', models.FloatField(default=10000, validators=[loan.models.validate_principal])),
                ('interest', models.FloatField(default=9)),
                ('months', models.IntegerField(default=0)),
                ('amount', models.FloatField(default=0)),
                ('emi', models.FloatField(default=0)),
                ('status', models.CharField(default='NEW', max_length=12)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]