# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.ForeignKey('Text', db_column='name')
    username = models.CharField(max_length=192)
    password = models.TextField()
    register_date = models.DateTimeField()
    preferred_language = models.ForeignKey('Language', db_column='preferred_language')
    role = models.CharField(max_length=39)
    created = models.DateTimeField()
    creator = models.ForeignKey('self', null=True, db_column='creator', related_name='creator_set', blank=True)
    modified = models.DateTimeField(null=True, blank=True)
    modifier = models.ForeignKey('self', null=True, db_column='modifier', blank=True)
    revision = models.IntegerField()

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = u'user'

class Text(models.Model):
    id = models.IntegerField(primary_key=True)
    language = models.ForeignKey('Language', db_column='language')
    data = models.TextField()
    source = models.ForeignKey('self', null=True, db_column='source', blank=True)
    created = models.DateTimeField()
    creator = models.ForeignKey(User, null=True, db_column='creator', related_name='text_creator_set', blank=True)
    modified = models.DateTimeField(null=True, blank=True)
    modifier = models.ForeignKey(User, null=True, db_column='modifier', blank=True)
    revision = models.IntegerField()

    def __unicode__(self):
        return self.data

    class Meta:
        db_table = u'text'

class Language(models.Model):
    code = models.CharField(max_length=30, primary_key=True)
    name = models.ForeignKey(Text, db_column='name', related_name='language_text_set')
    direction = models.CharField(max_length=9)

    def __unicode__(self):
        return self.code

    class Meta:
        db_table = u'language'

class License(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.ForeignKey(Text, db_column='name', related_name='liscense_text_set')
    abbreviation = models.ForeignKey(Text, null=True, db_column='abbreviation', blank=True)
    url = models.CharField(max_length=765, blank=True)

    def __unicode__(self):
        return self.abbreviation
        
    class Meta:
        db_table = u'license'

class Ref(models.Model):
    id = models.IntegerField(primary_key=True)
    work = models.ForeignKey('Work', null=True, db_column='work', blank=True)
    type = models.CharField(max_length=36, blank=True)
    osis_id = models.CharField(max_length=48, blank=True)
    position = models.IntegerField()
    name = models.ForeignKey(Text, null=True, db_column='name', blank=True)
    parent = models.ForeignKey('self', null=True, db_column='parent', blank=True)
    start_token = models.ForeignKey('Token', db_column='start_token', related_name='start_token_ref_set')
    end_token = models.ForeignKey('Token', null=True, db_column='end_token', related_name='end_token_ref_set', blank=True)
    numerical_start = models.IntegerField(null=True, blank=True)
    numerical_end = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField()
    creator = models.ForeignKey(User, null=True, db_column='creator', related_name='ref_creator_set', blank=True)
    modified = models.DateTimeField(null=True, blank=True)
    modifier = models.ForeignKey(User, null=True, db_column='modifier', blank=True)
    revision = models.IntegerField()

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = u'ref'


class Token(models.Model):
    id = models.IntegerField(primary_key=True)
    data = models.CharField(max_length=765)
    type = models.CharField(max_length=33)
    position = models.IntegerField()
    ums_token = models.ForeignKey('self', null=True, db_column='ums_token', blank=True)
    work = models.ForeignKey('Work', db_column='work')

    def __unicode__(self):
        return self.data

    class Meta:
        db_table = u'token'

class TokenGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=33)
    created = models.DateTimeField()
    creator = models.ForeignKey(User, null=True, db_column='creator', related_name='token_group_creator_set', blank=True)
    modified = models.DateTimeField(null=True, blank=True)
    modifier = models.ForeignKey(User, null=True, db_column='modifier', blank=True)
    revision = models.IntegerField()

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = u'token_group'

class TokenGroupCluster(models.Model):
    id = models.IntegerField(primary_key=True)
    token_group = models.ForeignKey(TokenGroup, db_column='token_group')
    rel = models.IntegerField()
    created = models.DateTimeField()
    creator = models.ForeignKey(User, null=True, db_column='creator', related_name='token_group_cluster_creator_set', blank=True)
    modified = models.DateTimeField(null=True, blank=True)
    modifier = models.ForeignKey(User, null=True, db_column='modifier', blank=True)
    revision = models.IntegerField()
    
    def __unicode__(self):
        return self.rel

    class Meta:
        db_table = u'token_group_cluster'

class TokenGroupClusterToken(models.Model):
    id = models.IntegerField(primary_key=True)
    token_group_cluster = models.ForeignKey(TokenGroupCluster, db_column='token_group_cluster')
    token = models.ForeignKey(Token, db_column='token')
    inclusion_rating = models.FloatField()
    comment = models.ForeignKey(Text, null=True, db_column='comment', blank=True)
    created = models.DateTimeField()
    creator = models.ForeignKey(User, null=True, db_column='creator', related_name='token_gropu_cluster_token_creator_set', blank=True)
    modified = models.DateTimeField(null=True, blank=True)
    modifier = models.ForeignKey(User, null=True, db_column='modifier', blank=True)
    revision = models.IntegerField()

    def __unicode__(self):
        return self.id

    class Meta:
        db_table = u'token_group_cluster_token'

class TokenParsing(models.Model):
    id = models.IntegerField(primary_key=True)
    token = models.ForeignKey(Token, db_column='token')
    parse = models.CharField(max_length=765, blank=True)
    strongs = models.CharField(max_length=765, blank=True)
    lemma = models.CharField(max_length=765, blank=True)
    language = models.ForeignKey(Language, null=True, db_column='language', blank=True)
    work = models.ForeignKey('Work', null=True, db_column='work', blank=True)
    created = models.DateTimeField()
    creator = models.ForeignKey(User, null=True, db_column='creator', related_name='token_parsing_set',blank=True)
    modified = models.DateTimeField(null=True, blank=True)
    modifier = models.ForeignKey(User, null=True, db_column='modifier', blank=True)
    revision = models.IntegerField()

    def __unicode__(self):
        return self.parse

    class Meta:
        db_table = u'token_parsing'


class UserLanguage(models.Model):
    user = models.ForeignKey(User, db_column='user', related_name='user_language_user_set')
    language = models.ForeignKey(Language, db_column='language')
    preference = models.FloatField()
    created = models.DateTimeField()
    creator = models.ForeignKey(User, null=True, db_column='creator', related_name='user_language_set', blank=True)
    modified = models.DateTimeField(null=True, blank=True)
    modifier = models.ForeignKey(User, null=True, db_column='modifier', blank=True)
    revision = models.IntegerField()

    def __unicode__(self):
        return self.user

    class Meta:
        db_table = u'user_language'

class Work(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.ForeignKey(Text, db_column='name', related_name='name_text_set')
    abbreviation = models.ForeignKey(Text, null=True, db_column='abbreviation', related_name='abbreviation_text_set',blank=True)
    language = models.ForeignKey(Language, null=True, db_column='language', blank=True)
    osis_id = models.CharField(unique=True, max_length=48)
    type = models.CharField(max_length=54)
    unified_work = models.ForeignKey('self', null=True, db_column='unified_work', blank=True)
    copyright = models.ForeignKey(Text, null=True, db_column='copyright', blank=True)
    url = models.CharField(max_length=765, blank=True)
    created = models.DateTimeField()
    creator = models.ForeignKey(User, null=True, db_column='creator', related_name='work_creator_set', blank=True)
    modified = models.DateTimeField(null=True, blank=True)
    modifier = models.ForeignKey(User, null=True, db_column='modifier', blank=True)
    revision = models.IntegerField()

    def __unicode__(self):
        return self.user

    class Meta:
        db_table = u'work'

class WorkLicense(models.Model):
    work = models.ForeignKey(Work, db_column='work')
    license = models.ForeignKey(License, db_column='license')
    
    def __unicode__(self):
        return self.work

    class Meta:
        db_table = u'work_license'

