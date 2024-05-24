# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BodyLookup(models.Model):
    lkid = models.AutoField(db_column='LKID', primary_key=True)  # Field name made lowercase.
    body = models.TextField(db_column='BODY')  # Field name made lowercase.
    checksum = models.CharField(db_column='CHECKSUM', max_length=40)  # Field name made lowercase.
    date_time = models.DateTimeField(db_column='DATE_TIME')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BODY_LOOKUP'


class ConversationId(models.Model):
    conversationid = models.AutoField(db_column='conversationId', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONVERSATION_ID'


class Messages0(models.Model):
    mailid = models.BigAutoField(primary_key=True)
    conversation_id = models.BigIntegerField()
    userid = models.IntegerField()
    usertype = models.CharField(max_length=1)
    from_email = models.CharField(max_length=255)
    from_name = models.CharField(max_length=255)
    to_userid = models.IntegerField()
    to_usertype = models.CharField(max_length=1)
    to_email = models.CharField(max_length=255)
    to_name = models.CharField(max_length=255)
    bodyid = models.BigIntegerField()
    lookupid = models.BigIntegerField()
    subject = models.CharField(max_length=250)
    date = models.DateTimeField()
    folderid = models.IntegerField()
    labels = models.CharField(max_length=10)
    is_read = models.IntegerField()
    appid = models.IntegerField()
    ipaddr = models.CharField(max_length=20)
    mid = models.CharField(db_column='MID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    metadata = models.TextField(blank=True, null=True)
    message_id = models.IntegerField(blank=True, null=True)
    isnew = models.IntegerField(db_column='isNew')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MESSAGES_0'


class Messages1(models.Model):
    mailid = models.BigAutoField(primary_key=True)
    conversation_id = models.BigIntegerField()
    userid = models.IntegerField()
    usertype = models.CharField(max_length=1)
    from_email = models.CharField(max_length=255)
    from_name = models.CharField(max_length=255)
    to_userid = models.IntegerField()
    to_usertype = models.CharField(max_length=1)
    to_email = models.CharField(max_length=255)
    to_name = models.CharField(max_length=255)
    bodyid = models.BigIntegerField()
    lookupid = models.BigIntegerField()
    subject = models.CharField(max_length=250)
    date = models.DateTimeField()
    folderid = models.IntegerField()
    labels = models.CharField(max_length=10)
    is_read = models.IntegerField()
    appid = models.IntegerField()
    ipaddr = models.CharField(max_length=20)
    mid = models.CharField(db_column='MID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    metadata = models.TextField(blank=True, null=True)
    message_id = models.IntegerField(blank=True, null=True)
    isnew = models.IntegerField(db_column='isNew')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MESSAGES_1'


class Messages10(models.Model):
    mailid = models.BigAutoField(primary_key=True)
    conversation_id = models.BigIntegerField()
    userid = models.IntegerField()
    usertype = models.CharField(max_length=1)
    from_email = models.CharField(max_length=255)
    from_name = models.CharField(max_length=255)
    to_userid = models.IntegerField()
    to_usertype = models.CharField(max_length=1)
    to_email = models.CharField(max_length=255)
    to_name = models.CharField(max_length=255)
    bodyid = models.BigIntegerField()
    lookupid = models.BigIntegerField()
    subject = models.CharField(max_length=250)
    date = models.DateTimeField()
    folderid = models.IntegerField()
    labels = models.CharField(max_length=10)
    is_read = models.IntegerField()
    appid = models.IntegerField()
    ipaddr = models.CharField(max_length=20)
    mid = models.CharField(db_column='MID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    metadata = models.TextField(blank=True, null=True)
    message_id = models.IntegerField(blank=True, null=True)
    isnew = models.IntegerField(db_column='isNew')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MESSAGES_10'


class Messages11(models.Model):
    mailid = models.BigAutoField(primary_key=True)
    conversation_id = models.BigIntegerField()
    userid = models.IntegerField()
    usertype = models.CharField(max_length=1)
    from_email = models.CharField(max_length=255)
    from_name = models.CharField(max_length=255)
    to_userid = models.IntegerField()
    to_usertype = models.CharField(max_length=1)
    to_email = models.CharField(max_length=255)
    to_name = models.CharField(max_length=255)
    bodyid = models.BigIntegerField()
    lookupid = models.BigIntegerField()
    subject = models.CharField(max_length=250)
    date = models.DateTimeField()
    folderid = models.IntegerField()
    labels = models.CharField(max_length=10)
    is_read = models.IntegerField()
    appid = models.IntegerField()
    ipaddr = models.CharField(max_length=20)
    mid = models.CharField(db_column='MID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    metadata = models.TextField(blank=True, null=True)
    message_id = models.IntegerField(blank=True, null=True)
    isnew = models.IntegerField(db_column='isNew')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MESSAGES_11'


class Messages12(models.Model):
    mailid = models.BigAutoField(primary_key=True)
    conversation_id = models.BigIntegerField()
    userid = models.IntegerField()
    usertype = models.CharField(max_length=1)
    from_email = models.CharField(max_length=255)
    from_name = models.CharField(max_length=255)
    to_userid = models.IntegerField()
    to_usertype = models.CharField(max_length=1)
    to_email = models.CharField(max_length=255)
    to_name = models.CharField(max_length=255)
    bodyid = models.BigIntegerField()
    lookupid = models.BigIntegerField()
    subject = models.CharField(max_length=250)
    date = models.DateTimeField()
    folderid = models.IntegerField()
    labels = models.CharField(max_length=10)
    is_read = models.IntegerField()
    appid = models.IntegerField()
    ipaddr = models.CharField(max_length=20)
    mid = models.CharField(db_column='MID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    metadata = models.TextField(blank=True, null=True)
    message_id = models.IntegerField(blank=True, null=True)
    isnew = models.IntegerField(db_column='isNew')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MESSAGES_12'


class Messages13(models.Model):
    mailid = models.BigAutoField(primary_key=True)
    conversation_id = models.BigIntegerField()
    userid = models.IntegerField()
    usertype = models.CharField(max_length=1)
    from_email = models.CharField(max_length=255)
    from_name = models.CharField(max_length=255)
    to_userid = models.IntegerField()
    to_usertype = models.CharField(max_length=1)
    to_email = models.CharField(max_length=255)
    to_name = models.CharField(max_length=255)
    bodyid = models.BigIntegerField()
    lookupid = models.BigIntegerField()
    subject = models.CharField(max_length=250)
    date = models.DateTimeField()
    folderid = models.IntegerField()
    labels = models.CharField(max_length=10)
    is_read = models.IntegerField()
    appid = models.IntegerField()
    ipaddr = models.CharField(max_length=20)
    mid = models.CharField(db_column='MID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    metadata = models.TextField(blank=True, null=True)
    message_id = models.IntegerField(blank=True, null=True)
    isnew = models.IntegerField(db_column='isNew')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MESSAGES_13'


class Messages14(models.Model):
    mailid = models.BigAutoField(primary_key=True)
    conversation_id = models.BigIntegerField()
    userid = models.IntegerField()
    usertype = models.CharField(max_length=1)
    from_email = models.CharField(max_length=255)
    from_name = models.CharField(max_length=255)
    to_userid = models.IntegerField()
    to_usertype = models.CharField(max_length=1)
    to_email = models.CharField(max_length=255)
    to_name = models.CharField(max_length=255)
    bodyid = models.BigIntegerField()
    lookupid = models.BigIntegerField()
    subject = models.CharField(max_length=250)
    date = models.DateTimeField()
    folderid = models.IntegerField()
    labels = models.CharField(max_length=10)
    is_read = models.IntegerField()
    appid = models.IntegerField()
    ipaddr = models.CharField(max_length=20)
    mid = models.CharField(db_column='MID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    metadata = models.TextField(blank=True, null=True)
    message_id = models.IntegerField(blank=True, null=True)
    isnew = models.IntegerField(db_column='isNew')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MESSAGES_14'


class Messages15(models.Model):
    mailid = models.BigAutoField(primary_key=True)
    conversation_id = models.BigIntegerField()
    userid = models.IntegerField()
    usertype = models.CharField(max_length=1)
    from_email = models.CharField(max_length=255)
    from_name = models.CharField(max_length=255)
    to_userid = models.IntegerField()
    to_usertype = models.CharField(max_length=1)
    to_email = models.CharField(max_length=255)
    to_name = models.CharField(max_length=255)
    bodyid = models.BigIntegerField()
    lookupid = models.BigIntegerField()
    subject = models.CharField(max_length=250)
    date = models.DateTimeField()
    folderid = models.IntegerField()
    labels = models.CharField(max_length=10)
    is_read = models.IntegerField()
    appid = models.IntegerField()
    ipaddr = models.CharField(max_length=20)
    mid = models.CharField(db_column='MID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    metadata = models.TextField(blank=True, null=True)
    message_id = models.IntegerField(blank=True, null=True)
    isnew = models.IntegerField(db_column='isNew')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MESSAGES_15'


class Messages16(models.Model):
    mailid = models.BigAutoField(primary_key=True)
    conversation_id = models.BigIntegerField()
    userid = models.IntegerField()
    usertype = models.CharField(max_length=1)
    from_email = models.CharField(max_length=255)
    from_name = models.CharField(max_length=255)
    to_userid = models.IntegerField()
    to_usertype = models.CharField(max_length=1)
    to_email = models.CharField(max_length=255)
    to_name = models.CharField(max_length=255)
    bodyid = models.BigIntegerField()
    lookupid = models.BigIntegerField()
    subject = models.CharField(max_length=250)
    date = models.DateTimeField()
    folderid = models.IntegerField()
    labels = models.CharField(max_length=10)
    is_read = models.IntegerField()
    appid = models.IntegerField()
    ipaddr = models.CharField(max_length=20)
    mid = models.CharField(db_column='MID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    metadata = models.TextField(blank=True, null=True)
    message_id = models.IntegerField(blank=True, null=True)
    isnew = models.IntegerField(db_column='isNew')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MESSAGES_16'


class Messages17(models.Model):
    mailid = models.BigAutoField(primary_key=True)
    conversation_id = models.BigIntegerField()
    userid = models.IntegerField()
    usertype = models.CharField(max_length=1)
    from_email = models.CharField(max_length=255)
    from_name = models.CharField(max_length=255)
    to_userid = models.IntegerField()
    to_usertype = models.CharField(max_length=1)
    to_email = models.CharField(max_length=255)
    to_name = models.CharField(max_length=255)
    bodyid = models.BigIntegerField()
    lookupid = models.BigIntegerField()
    subject = models.CharField(max_length=250)
    date = models.DateTimeField()
    folderid = models.IntegerField()
    labels = models.CharField(max_length=10)
    is_read = models.IntegerField()
    appid = models.IntegerField()
    ipaddr = models.CharField(max_length=20)
    mid = models.CharField(db_column='MID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    metadata = models.TextField(blank=True, null=True)
    message_id = models.IntegerField(blank=True, null=True)
    isnew = models.IntegerField(db_column='isNew')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MESSAGES_17'


class Messages18(models.Model):
    mailid = models.BigAutoField(primary_key=True)
    conversation_id = models.BigIntegerField()
    userid = models.IntegerField()
    usertype = models.CharField(max_length=1)
    from_email = models.CharField(max_length=255)
    from_name = models.CharField(max_length=255)
    to_userid = models.IntegerField()
    to_usertype = models.CharField(max_length=1)
    to_email = models.CharField(max_length=255)
    to_name = models.CharField(max_length=255)
    bodyid = models.BigIntegerField()
    lookupid = models.BigIntegerField()
    subject = models.CharField(max_length=250)
    date = models.DateTimeField()
    folderid = models.IntegerField()
    labels = models.CharField(max_length=10)
    is_read = models.IntegerField()
    appid = models.IntegerField()
    ipaddr = models.CharField(max_length=20)
    mid = models.CharField(db_column='MID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    metadata = models.TextField(blank=True, null=True)
    message_id = models.IntegerField(blank=True, null=True)
    isnew = models.IntegerField(db_column='isNew')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MESSAGES_18'


class Messages19(models.Model):
    mailid = models.BigAutoField(primary_key=True)
    conversation_id = models.BigIntegerField()
    userid = models.IntegerField()
    usertype = models.CharField(max_length=1)
    from_email = models.CharField(max_length=255)
    from_name = models.CharField(max_length=255)
    to_userid = models.IntegerField()
    to_usertype = models.CharField(max_length=1)
    to_email = models.CharField(max_length=255)
    to_name = models.CharField(max_length=255)
    bodyid = models.BigIntegerField()
    lookupid = models.BigIntegerField()
    subject = models.CharField(max_length=250)
    date = models.DateTimeField()
    folderid = models.IntegerField()
    labels = models.CharField(max_length=10)
    is_read = models.IntegerField()
    appid = models.IntegerField()
    ipaddr = models.CharField(max_length=20)
    mid = models.CharField(db_column='MID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    metadata = models.TextField(blank=True, null=True)
    message_id = models.IntegerField(blank=True, null=True)
    isnew = models.IntegerField(db_column='isNew')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MESSAGES_19'


class Messages2(models.Model):
    mailid = models.BigAutoField(primary_key=True)
    conversation_id = models.BigIntegerField()
    userid = models.IntegerField()
    usertype = models.CharField(max_length=1)
    from_email = models.CharField(max_length=255)
    from_name = models.CharField(max_length=255)
    to_userid = models.IntegerField()
    to_usertype = models.CharField(max_length=1)
    to_email = models.CharField(max_length=255)
    to_name = models.CharField(max_length=255)
    bodyid = models.BigIntegerField()
    lookupid = models.BigIntegerField()
    subject = models.CharField(max_length=250)
    date = models.DateTimeField()
    folderid = models.IntegerField()
    labels = models.CharField(max_length=10)
    is_read = models.IntegerField()
    appid = models.IntegerField()
    ipaddr = models.CharField(max_length=20)
    mid = models.CharField(db_column='MID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    metadata = models.TextField(blank=True, null=True)
    message_id = models.IntegerField(blank=True, null=True)
    isnew = models.IntegerField(db_column='isNew')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MESSAGES_2'


class Messages20(models.Model):
    mailid = models.BigAutoField(primary_key=True)
    conversation_id = models.BigIntegerField()
    userid = models.IntegerField()
    usertype = models.CharField(max_length=1)
    from_email = models.CharField(max_length=255)
    from_name = models.CharField(max_length=255)
    to_userid = models.IntegerField()
    to_usertype = models.CharField(max_length=1)
    to_email = models.CharField(max_length=255)
    to_name = models.CharField(max_length=255)
    bodyid = models.BigIntegerField()
    lookupid = models.BigIntegerField()
    subject = models.CharField(max_length=250)
    date = models.DateTimeField()
    folderid = models.IntegerField()
    labels = models.CharField(max_length=10)
    is_read = models.IntegerField()
    appid = models.IntegerField()
    ipaddr = models.CharField(max_length=20)
    mid = models.CharField(db_column='MID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    metadata = models.TextField(blank=True, null=True)
    message_id = models.IntegerField(blank=True, null=True)
    isnew = models.IntegerField(db_column='isNew')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MESSAGES_20'


class Messages21(models.Model):
    mailid = models.BigAutoField(primary_key=True)
    conversation_id = models.BigIntegerField()
    userid = models.IntegerField()
    usertype = models.CharField(max_length=1)
    from_email = models.CharField(max_length=255)
    from_name = models.CharField(max_length=255)
    to_userid = models.IntegerField()
    to_usertype = models.CharField(max_length=1)
    to_email = models.CharField(max_length=255)
    to_name = models.CharField(max_length=255)
    bodyid = models.BigIntegerField()
    lookupid = models.BigIntegerField()
    subject = models.CharField(max_length=250)
    date = models.DateTimeField()
    folderid = models.IntegerField()
    labels = models.CharField(max_length=10)
    is_read = models.IntegerField()
    appid = models.IntegerField()
    ipaddr = models.CharField(max_length=20)
    mid = models.CharField(db_column='MID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    metadata = models.TextField(blank=True, null=True)
    message_id = models.IntegerField(blank=True, null=True)
    isnew = models.IntegerField(db_column='isNew')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MESSAGES_21'


class Messages22(models.Model):
    mailid = models.BigAutoField(primary_key=True)
    conversation_id = models.BigIntegerField()
    userid = models.IntegerField()
    usertype = models.CharField(max_length=1)
    from_email = models.CharField(max_length=255)
    from_name = models.CharField(max_length=255)
    to_userid = models.IntegerField()
    to_usertype = models.CharField(max_length=1)
    to_email = models.CharField(max_length=255)
    to_name = models.CharField(max_length=255)
    bodyid = models.BigIntegerField()
    lookupid = models.BigIntegerField()
    subject = models.CharField(max_length=250)
    date = models.DateTimeField()
    folderid = models.IntegerField()
    labels = models.CharField(max_length=10)
    is_read = models.IntegerField()
    appid = models.IntegerField()
    ipaddr = models.CharField(max_length=20)
    mid = models.CharField(db_column='MID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    metadata = models.TextField(blank=True, null=True)
    message_id = models.IntegerField(blank=True, null=True)
    isnew = models.IntegerField(db_column='isNew')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MESSAGES_22'


class Messages23(models.Model):
    mailid = models.BigAutoField(primary_key=True)
    conversation_id = models.BigIntegerField()
    userid = models.IntegerField()
    usertype = models.CharField(max_length=1)
    from_email = models.CharField(max_length=255)
    from_name = models.CharField(max_length=255)
    to_userid = models.IntegerField()
    to_usertype = models.CharField(max_length=1)
    to_email = models.CharField(max_length=255)
    to_name = models.CharField(max_length=255)
    bodyid = models.BigIntegerField()
    lookupid = models.BigIntegerField()
    subject = models.CharField(max_length=250)
    date = models.DateTimeField()
    folderid = models.IntegerField()
    labels = models.CharField(max_length=10)
    is_read = models.IntegerField()
    appid = models.IntegerField()
    ipaddr = models.CharField(max_length=20)
    mid = models.CharField(db_column='MID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    metadata = models.TextField(blank=True, null=True)
    message_id = models.IntegerField(blank=True, null=True)
    isnew = models.IntegerField(db_column='isNew')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MESSAGES_23'


class Messages24(models.Model):
    mailid = models.BigAutoField(primary_key=True)
    conversation_id = models.BigIntegerField()
    userid = models.IntegerField()
    usertype = models.CharField(max_length=1)
    from_email = models.CharField(max_length=255)
    from_name = models.CharField(max_length=255)
    to_userid = models.IntegerField()
    to_usertype = models.CharField(max_length=1)
    to_email = models.CharField(max_length=255)
    to_name = models.CharField(max_length=255)
    bodyid = models.BigIntegerField()
    lookupid = models.BigIntegerField()
    subject = models.CharField(max_length=250)
    date = models.DateTimeField()
    folderid = models.IntegerField()
    labels = models.CharField(max_length=10)
    is_read = models.IntegerField()
    appid = models.IntegerField()
    ipaddr = models.CharField(max_length=20)
    mid = models.CharField(db_column='MID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    metadata = models.TextField(blank=True, null=True)
    message_id = models.IntegerField(blank=True, null=True)
    isnew = models.IntegerField(db_column='isNew')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MESSAGES_24'


class Messages3(models.Model):
    mailid = models.BigAutoField(primary_key=True)
    conversation_id = models.BigIntegerField()
    userid = models.IntegerField()
    usertype = models.CharField(max_length=1)
    from_email = models.CharField(max_length=255)
    from_name = models.CharField(max_length=255)
    to_userid = models.IntegerField()
    to_usertype = models.CharField(max_length=1)
    to_email = models.CharField(max_length=255)
    to_name = models.CharField(max_length=255)
    bodyid = models.BigIntegerField()
    lookupid = models.BigIntegerField()
    subject = models.CharField(max_length=250)
    date = models.DateTimeField()
    folderid = models.IntegerField()
    labels = models.CharField(max_length=10)
    is_read = models.IntegerField()
    appid = models.IntegerField()
    ipaddr = models.CharField(max_length=20)
    mid = models.CharField(db_column='MID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    metadata = models.TextField(blank=True, null=True)
    message_id = models.IntegerField(blank=True, null=True)
    isnew = models.IntegerField(db_column='isNew')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MESSAGES_3'


class Messages4(models.Model):
    mailid = models.BigAutoField(primary_key=True)
    conversation_id = models.BigIntegerField()
    userid = models.IntegerField()
    usertype = models.CharField(max_length=1)
    from_email = models.CharField(max_length=255)
    from_name = models.CharField(max_length=255)
    to_userid = models.IntegerField()
    to_usertype = models.CharField(max_length=1)
    to_email = models.CharField(max_length=255)
    to_name = models.CharField(max_length=255)
    bodyid = models.BigIntegerField()
    lookupid = models.BigIntegerField()
    subject = models.CharField(max_length=250)
    date = models.DateTimeField()
    folderid = models.IntegerField()
    labels = models.CharField(max_length=10)
    is_read = models.IntegerField()
    appid = models.IntegerField()
    ipaddr = models.CharField(max_length=20)
    mid = models.CharField(db_column='MID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    metadata = models.TextField(blank=True, null=True)
    message_id = models.IntegerField(blank=True, null=True)
    isnew = models.IntegerField(db_column='isNew')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MESSAGES_4'


class Messages5(models.Model):
    mailid = models.BigAutoField(primary_key=True)
    conversation_id = models.BigIntegerField()
    userid = models.IntegerField()
    usertype = models.CharField(max_length=1)
    from_email = models.CharField(max_length=255)
    from_name = models.CharField(max_length=255)
    to_userid = models.IntegerField()
    to_usertype = models.CharField(max_length=1)
    to_email = models.CharField(max_length=255)
    to_name = models.CharField(max_length=255)
    bodyid = models.BigIntegerField()
    lookupid = models.BigIntegerField()
    subject = models.CharField(max_length=250)
    date = models.DateTimeField()
    folderid = models.IntegerField()
    labels = models.CharField(max_length=10)
    is_read = models.IntegerField()
    appid = models.IntegerField()
    ipaddr = models.CharField(max_length=20)
    mid = models.CharField(db_column='MID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    metadata = models.TextField(blank=True, null=True)
    message_id = models.IntegerField(blank=True, null=True)
    isnew = models.IntegerField(db_column='isNew')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MESSAGES_5'


class Messages6(models.Model):
    mailid = models.BigAutoField(primary_key=True)
    conversation_id = models.BigIntegerField()
    userid = models.IntegerField()
    usertype = models.CharField(max_length=1)
    from_email = models.CharField(max_length=255)
    from_name = models.CharField(max_length=255)
    to_userid = models.IntegerField()
    to_usertype = models.CharField(max_length=1)
    to_email = models.CharField(max_length=255)
    to_name = models.CharField(max_length=255)
    bodyid = models.BigIntegerField()
    lookupid = models.BigIntegerField()
    subject = models.CharField(max_length=250)
    date = models.DateTimeField()
    folderid = models.IntegerField()
    labels = models.CharField(max_length=10)
    is_read = models.IntegerField()
    appid = models.IntegerField()
    ipaddr = models.CharField(max_length=20)
    mid = models.CharField(db_column='MID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    metadata = models.TextField(blank=True, null=True)
    message_id = models.IntegerField(blank=True, null=True)
    isnew = models.IntegerField(db_column='isNew')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MESSAGES_6'


class Messages7(models.Model):
    mailid = models.BigAutoField(primary_key=True)
    conversation_id = models.BigIntegerField()
    userid = models.IntegerField()
    usertype = models.CharField(max_length=1)
    from_email = models.CharField(max_length=255)
    from_name = models.CharField(max_length=255)
    to_userid = models.IntegerField()
    to_usertype = models.CharField(max_length=1)
    to_email = models.CharField(max_length=255)
    to_name = models.CharField(max_length=255)
    bodyid = models.BigIntegerField()
    lookupid = models.BigIntegerField()
    subject = models.CharField(max_length=250)
    date = models.DateTimeField()
    folderid = models.IntegerField()
    labels = models.CharField(max_length=10)
    is_read = models.IntegerField()
    appid = models.IntegerField()
    ipaddr = models.CharField(max_length=20)
    mid = models.CharField(db_column='MID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    metadata = models.TextField(blank=True, null=True)
    message_id = models.IntegerField(blank=True, null=True)
    isnew = models.IntegerField(db_column='isNew')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MESSAGES_7'


class Messages8(models.Model):
    mailid = models.BigAutoField(primary_key=True)
    conversation_id = models.BigIntegerField()
    userid = models.IntegerField()
    usertype = models.CharField(max_length=1)
    from_email = models.CharField(max_length=255)
    from_name = models.CharField(max_length=255)
    to_userid = models.IntegerField()
    to_usertype = models.CharField(max_length=1)
    to_email = models.CharField(max_length=255)
    to_name = models.CharField(max_length=255)
    bodyid = models.BigIntegerField()
    lookupid = models.BigIntegerField()
    subject = models.CharField(max_length=250)
    date = models.DateTimeField()
    folderid = models.IntegerField()
    labels = models.CharField(max_length=10)
    is_read = models.IntegerField()
    appid = models.IntegerField()
    ipaddr = models.CharField(max_length=20)
    mid = models.CharField(db_column='MID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    metadata = models.TextField(blank=True, null=True)
    message_id = models.IntegerField(blank=True, null=True)
    isnew = models.IntegerField(db_column='isNew')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MESSAGES_8'


class Messages9(models.Model):
    mailid = models.BigAutoField(primary_key=True)
    conversation_id = models.BigIntegerField()
    userid = models.IntegerField()
    usertype = models.CharField(max_length=1)
    from_email = models.CharField(max_length=255)
    from_name = models.CharField(max_length=255)
    to_userid = models.IntegerField()
    to_usertype = models.CharField(max_length=1)
    to_email = models.CharField(max_length=255)
    to_name = models.CharField(max_length=255)
    bodyid = models.BigIntegerField()
    lookupid = models.BigIntegerField()
    subject = models.CharField(max_length=250)
    date = models.DateTimeField()
    folderid = models.IntegerField()
    labels = models.CharField(max_length=10)
    is_read = models.IntegerField()
    appid = models.IntegerField()
    ipaddr = models.CharField(max_length=20)
    mid = models.CharField(db_column='MID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    metadata = models.TextField(blank=True, null=True)
    message_id = models.IntegerField(blank=True, null=True)
    isnew = models.IntegerField(db_column='isNew')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MESSAGES_9'
