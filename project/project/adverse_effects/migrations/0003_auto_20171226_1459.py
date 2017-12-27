# Generated by Django 2.0 on 2017-12-26 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverse_effects', '0002_auto_20171226_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.RemoveField(
            model_name='adverseeffect',
            name='adverseID',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='blogID',
        ),
        migrations.RemoveField(
            model_name='bodypart',
            name='bodypartID',
        ),
        migrations.RemoveField(
            model_name='drug',
            name='drugID',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='tagID',
        ),
        migrations.AddField(
            model_name='drug',
            name='activeingredients',
            field=models.ManyToManyField(blank=True, default=None, to='adverse_effects.ActiveIngredient'),
        ),
    ]
