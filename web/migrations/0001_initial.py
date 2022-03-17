# Generated by Django 4.0.2 on 2022-03-17 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categori',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('categoriname', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'categori',
            },
        ),
        migrations.CreateModel(
            name='Ceo',
            fields=[
                ('ceoid', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'ceo',
            },
        ),
        migrations.CreateModel(
            name='Cust',
            fields=[
                ('custno', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.CharField(blank=True, max_length=30, null=True)),
                ('password', models.CharField(blank=True, max_length=30, null=True)),
                ('name', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('regdate', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'cust',
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('foodid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('regdate', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'food',
            },
        ),
        migrations.CreateModel(
            name='Seocho',
            fields=[
                ('seochono', models.IntegerField(primary_key=True, serialize=False)),
                ('marketname', models.CharField(blank=True, max_length=50, null=True)),
                ('ceoname', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('categori', models.CharField(blank=True, max_length=100, null=True)),
                ('food', models.CharField(blank=True, max_length=100, null=True)),
                ('open', models.CharField(blank=True, max_length=100, null=True)),
                ('close', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'seocho',
            },
        ),
        migrations.CreateModel(
            name='Seochofood',
            fields=[
                ('foodid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('seochono', models.ForeignKey(db_column='seochono', on_delete=django.db.models.deletion.DO_NOTHING, to='web.seocho')),
            ],
            options={
                'db_table': 'seochofood',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('reviewno', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(blank=True, max_length=100, null=True)),
                ('star', models.FloatField(blank=True, null=True)),
                ('regdate', models.DateField(auto_now=True)),
                ('custno', models.ForeignKey(db_column='custno', on_delete=django.db.models.deletion.CASCADE, to='web.cust')),
                ('seochono', models.ForeignKey(db_column='seochono', on_delete=django.db.models.deletion.DO_NOTHING, to='web.seocho')),
            ],
            options={
                'db_table': 'review',
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('replyid', models.AutoField(primary_key=True, serialize=False)),
                ('pcontent', models.CharField(blank=True, max_length=100, null=True)),
                ('regdate', models.DateField(auto_now=True)),
                ('ceoid', models.ForeignKey(db_column='ceoid', on_delete=django.db.models.deletion.DO_NOTHING, to='web.ceo')),
                ('reviewno', models.ForeignKey(db_column='reviewno', on_delete=django.db.models.deletion.DO_NOTHING, to='web.review')),
                ('seochono', models.ForeignKey(db_column='seochono', on_delete=django.db.models.deletion.DO_NOTHING, to='web.seocho')),
            ],
            options={
                'db_table': 'reply',
            },
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('marketno', models.AutoField(primary_key=True, serialize=False)),
                ('marketname', models.CharField(blank=True, max_length=100, null=True)),
                ('marketaddress', models.CharField(blank=True, max_length=100, null=True)),
                ('regdate', models.DateField(auto_now=True)),
                ('open', models.TimeField(blank=True, null=True)),
                ('close', models.TimeField(blank=True, null=True)),
                ('holiday', models.DateField(blank=True, null=True)),
                ('hit', models.IntegerField(blank=True, null=True)),
                ('cid', models.ForeignKey(db_column='cid', on_delete=django.db.models.deletion.DO_NOTHING, to='web.categori')),
                ('foodid', models.ForeignKey(db_column='foodid', on_delete=django.db.models.deletion.DO_NOTHING, to='web.food')),
            ],
            options={
                'db_table': 'market',
            },
        ),
        migrations.AddField(
            model_name='ceo',
            name='seochono',
            field=models.ForeignKey(db_column='seochono', on_delete=django.db.models.deletion.DO_NOTHING, to='web.seocho'),
        ),
    ]
