# Generated by Django 3.0.7 on 2020-07-03 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proprietaire', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_de_bien', models.CharField(choices=[('appartement', 'appartement'), ('maison', 'maison'), ('terrain', 'terrain')], max_length=50)),
                ('operation', models.CharField(choices=[('vente', 'vente'), ('location', 'location'), ('estimation', 'estimation')], max_length=50)),
                ('chambre', models.IntegerField()),
                ('sdb', models.IntegerField()),
                ('toilette', models.IntegerField()),
                ('superficie_salon', models.IntegerField()),
                ('cuisine', models.IntegerField()),
                ('meuble', models.CharField(choices=[('oui', 'oui'), ('non', 'non')], max_length=3)),
                ('garage', models.CharField(choices=[('oui', 'oui'), ('non', 'non')], max_length=3)),
                ('parking', models.IntegerField()),
                ('superficie_habitat', models.IntegerField()),
                ('superficie_terrain', models.IntegerField()),
                ('proprietaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proprietaire.Proprietaire')),
            ],
        ),
        migrations.CreateModel(
            name='Photo_biens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='static/img/biens_img')),
                ('bien', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='produits.Biens')),
            ],
        ),
    ]
