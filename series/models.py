from django.contrib.postgres.fields import JSONField
from django.db import models


class Show(models.Model):
    tmdb_id = models.PositiveSmallIntegerField(db_index=True, unique=True)
    name = models.CharField(max_length=100, db_index=True)
    overview = models.TextField()
    # Other TMDB fields accessed from API response stored in tmdb_data
    tmdb_data = JSONField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<Show: %r>' % self.name


class Season(models.Model):
    tmdb_id = models.PositiveSmallIntegerField(db_index=True, unique=True)
    name = models.CharField(max_length=100, db_index=True)
    overview = models.TextField()
    season_number = models.PositiveSmallIntegerField()

    tmdb_data = JSONField()

    show = models.ForeignKey(Show, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<%r>' % self.name


class Episode(models.Model):
    tmdb_id = models.PositiveSmallIntegerField(db_index=True, unique=True)
    name = models.CharField(max_length=100, db_index=True)
    overview = models.TextField()
    episode_number = models.PositiveSmallIntegerField()

    tmdb_data = JSONField()

    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<Episode: %r>' % self.name
