from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

'''
The User class already has the following
username
firstname
lastname
email
password
groups
user_permissions
is_staff
is_active
is_superuser
last_login
date_joined
'''

# meta data about the user profile
class userMetadata(models.Model):
    user = models.ForeignKey(User)
    currRole = models.ForeignKey(role)
    profilePicUrl = models.CharField(max_length=100)
    longestStreak = models.IntegerField(default=0)   #number of days
    longestStreakSprint = models.ForeignKey(workSprint)

    class Meta:
        db_table = 'userMetadata'

# the character of different masons
class role(models.Model):
    roleId = models.AutoField(primary_key=True)
    masonName = models.CharField(max_length=50)
    masonBonus = models.IntegerField()
    superPowers = models.CharField(max_length=200)
    imgPath = models.CharField(max_length=100)

    class Meta:
        db_table = 'role'

# brick - a unit of action
class brick(models.Model):
    brickId = models.AutoField(primary_key=True)
    action = models.CharField(max_length=400)
    desc = models.CharField(max_length=1000)
    proofUrl = models.URLField()
    imgPath = models.CharField(max_length=100)

    class Meta:
        db_table = 'brick'

class brickType(models.Model):
    brickTypeId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    desc = models.CharField(max_length=1000)
    imgPAth = models.CharField(max_length=100)

    class Meta:
        db_table = 'brickType'

# a topic you want to work at for eg Data structures
class pillar(models.Model):
    pillarId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=1000)
    imgPath = models.CharField(max_length=100)

    class Meta:
        db_table = 'pillar'

# commitment made -> construction project
class constructionProject(models.Model):
    upvId = models.CharField(primary_key=True)  #CK = userId + pillarId + Version number of commitment
    brickQty = models.IntegerField()
    constnFreq = models.IntegerField()  # n = brickQty / n days
    status = models.BooleanField(default=True)  #true = ongoing project , false = closed project

    class Meta:
        db_table = 'constructionProject'

# a day's/sprint's work done i.e number of bricks added
class workSprint(models.Model):
    startDate = models.DateField()
    endDate = models.DateField()
    brickQty = models.IntegerField()
    brickType = models.ForeignKey(brick)
    cpId = models.ForeignKey(constructionProject)
    actionMetadata = models.CommaSeparatedIntegerField()    #comma separated brick ids

    class Meta:
        db_table = 'workSprint'

# skill level benchmarks
class skillLevel(models.Model):
    skillId = models.AutoField(primary_key=True)
    numOfBricks = models.IntegerField() #total number of bricks added by user to define the pro-ness level
    steakCount = models.IntegerField() #longest streak of user should cross this count for level up

    class Meta:
        db_table = 'skillLevel'

# all data linking a user to a Pillar and a brick
class userProject(models.Model):
    upId = models.AutoField(primary_key=True)
    user = models.ForeignKey(userMetadata)
    pillar = models.ForeignKey(pillar)
    brickType = models.ForeignKey(brickType)
    constnStartDate = models.DateTimeField(default=timezone.now())
    constnEndDate = models.DateTimeField()
    skillLevelStartDate = models.DateField()
    currentVersion = models.IntegerField()

    class Meta:
        db_table = 'userProject'

# a group of users
class group(models.Model):
    groupId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=1000)
    code = models.CharField(max_length=5)   #sorrt of OTP

    class Meta:
        db_table = 'group'

# because a user can be a part of multiple groups
class userGroupDetails(models.Model):
    group = models.ForeignKey(group)
    user = models.ForeignKey(userMetadata)
    pillar = models.ForeignKey(pillar)

    class Meta:
        db_table = 'userGroupDetails'