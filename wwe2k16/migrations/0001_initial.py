# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-03-08 20:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=40, unique=True)),
                ('name', models.CharField(max_length=250, unique=True)),
                ('color', models.CharField(default=b'black', max_length=20)),
                ('status', models.BooleanField(choices=[(True, b'Active'), (False, b'Inactive')], default=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Championship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=40, unique=True)),
                ('name', models.CharField(max_length=250, unique=True)),
                ('belt_type', models.CharField(choices=[(b'PR', b'Primary'), (b'SE', b'Secondary'), (b'TE', b'Tertiary'), (b'TT', b'Tag Team')], default=b'PR', max_length=2)),
                ('status', models.BooleanField(choices=[(True, b'Active'), (False, b'Inactive')], default=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChampionshipHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'history',
            },
        ),
        migrations.CreateModel(
            name='DraftHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(blank=True, max_length=1000, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wwe2k16.Brand')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=40, unique=True)),
                ('name', models.CharField(max_length=250)),
                ('year', models.CharField(max_length=4)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('brand', models.ForeignKey(blank=True, default=b'', null=True, on_delete=django.db.models.deletion.CASCADE, to='wwe2k16.Brand')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('championship', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wwe2k16.Championship')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wwe2k16.Event')),
            ],
            options={
                'verbose_name_plural': 'matches',
            },
        ),
        migrations.CreateModel(
            name='MatchType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=40, unique=True)),
                ('name', models.CharField(max_length=250, unique=True)),
                ('no_of_participants', models.PositiveIntegerField(default=2)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TagTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=40, unique=True)),
                ('name', models.CharField(max_length=250, unique=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'tagteams',
            },
        ),
        migrations.CreateModel(
            name='TagTeamMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winner', models.PositiveSmallIntegerField(choices=[(1, b'Team 1'), (2, b'Team 2')], default=1)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('championship', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wwe2k16.Championship')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wwe2k16.Event')),
            ],
            options={
                'verbose_name_plural': 'matches',
            },
        ),
        migrations.CreateModel(
            name='Wrestler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=40, unique=True)),
                ('name', models.CharField(max_length=250, unique=True)),
                ('ovr', models.PositiveIntegerField(default=0)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('height', models.PositiveIntegerField(blank=True, null=True)),
                ('weight', models.PositiveIntegerField(blank=True, null=True)),
                ('original_primary', models.PositiveIntegerField(default=0)),
                ('original_secondary', models.PositiveIntegerField(default=0)),
                ('primary', models.PositiveIntegerField(default=0)),
                ('secondary', models.PositiveIntegerField(default=0)),
                ('tertiary', models.PositiveIntegerField(default=0)),
                ('tag_team', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('brand', models.ForeignKey(blank=True, default=b'', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='wwe2k16.Brand')),
            ],
        ),
        migrations.AddField(
            model_name='tagteammatch',
            name='team1',
            field=models.ManyToManyField(related_name='team1', to='wwe2k16.Wrestler'),
        ),
        migrations.AddField(
            model_name='tagteammatch',
            name='team2',
            field=models.ManyToManyField(related_name='team2', to='wwe2k16.Wrestler'),
        ),
        migrations.AddField(
            model_name='tagteam',
            name='members',
            field=models.ManyToManyField(to='wwe2k16.Wrestler'),
        ),
        migrations.AddField(
            model_name='match',
            name='match_type',
            field=models.ForeignKey(blank=True, default=b'', on_delete=django.db.models.deletion.CASCADE, to='wwe2k16.MatchType'),
        ),
        migrations.AddField(
            model_name='match',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='participants', to='wwe2k16.Wrestler'),
        ),
        migrations.AddField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='wwe2k16.Wrestler'),
        ),
        migrations.AddField(
            model_name='championshiphistory',
            name='match',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wwe2k16.Match'),
        ),
        migrations.AddField(
            model_name='championshiphistory',
            name='new_champion',
            field=models.ManyToManyField(blank=True, related_name='new_champion', to='wwe2k16.Wrestler'),
        ),
        migrations.AddField(
            model_name='championshiphistory',
            name='old_champion',
            field=models.ManyToManyField(blank=True, related_name='old_champion', to='wwe2k16.Wrestler'),
        ),
        migrations.AddField(
            model_name='championship',
            name='champion',
            field=models.ManyToManyField(blank=True, default=b'', to='wwe2k16.Wrestler'),
        ),
        migrations.AlterUniqueTogether(
            name='event',
            unique_together=set([('name', 'year')]),
        ),
    ]
