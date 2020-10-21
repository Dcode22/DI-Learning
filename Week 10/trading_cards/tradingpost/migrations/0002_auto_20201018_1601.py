# Generated by Django 3.1.2 on 2020-10-18 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tradingpost', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mlb_id', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='card',
            name='team_id',
        ),
        migrations.RemoveField(
            model_name='card',
            name='team_name',
        ),
        migrations.AlterField(
            model_name='card',
            name='player_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AddField(
            model_name='card',
            name='team',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tradingpost.team'),
            preserve_default=False,
        ),
    ]