import random
from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    """ one variation from each group will be selected. 
        variations are (at minimum) assigned to a group with their control variation
    """
    slug = models.SlugField(max_length=100)
    
    def data(self):
        data = []
        for g in Goal.objects.all():
            scores = []
            for v in self.variations.all():
                scores.append({
                    'variation':v,
                    'score':v.score(g),
                    'total':v.total(),
                    'wins': v.wins(g),
                })
                
            d = {
                'goal':g,
                'scores':scores,
            }
            data.append(d)
        return data
    
    def __unicode__(self):
        return self.slug

class Variation(models.Model):
    group = models.ForeignKey(Group, related_name='variations')
    slug = models.SlugField(max_length=100)
    
    def humans(self):
        p = self.profiles.exclude(user_agent='')
        excludes = ['bot', 'Baiduspider', 'SiteExplorer']
        for e in excludes:
            p = p.exclude(user_agent__icontains=e)
        return p
        
    def total(self):
        return self.humans().count()
        
    def wins(self, goal):
        return self.humans().filter(successes__goal=goal).count()
        
    def score(self, goal):
        """ ratio of profiles with success, vs all profiles (of this variation) """
        if self.total():
            return float(self.wins(goal)) / self.total()
        return 0.0
    
    def __unicode__(self):
        return self.slug
    
class MVProfileManager(models.Manager):
    def new(self):
        """ create a new profile object """
        variations = []
        for g in Group.objects.all():
            #pick a variation from this group
            length = g.variations.all().count()
            if length:
                i = random.randint(0,length-1)
                variations.append(g.variations.all()[i])
            
        p = MVProfile.objects.create()
        p.variations = variations
        return p
    
class MVProfile(models.Model):
    user = models.OneToOneField(User, related_name='mv_profile', null=True, blank=True)
    variations = models.ManyToManyField(Variation, related_name='profiles')
    
    user_agent = models.TextField(default='', blank=True)
    
    objects = MVProfileManager()
    
    def __unicode__(self):
        return str(self.user or 'visitor')
    
    def goal(self):
        """ record a success record for a goal by this name """
        return SuccessRecorder(self)
        
    def v(self):
        return GroupGetter(self)
        
class GroupGetter(object):
    def __init__(self, profile):
        self.profile = profile
        
    def __getattr__(self, name):
        if name[0] == '_':
            raise AttributeError
        
        #get or create a group by this name
        group, created = Group.objects.get_or_create(
            slug = name
            )
        return VariationChecker(self.profile, group)
        
class VariationChecker(object):
    def __init__(self, profile, group):
        self.profile = profile
        self.group = group
        
        #get this profile's variation
        v = self.profile.variations.filter(group=self.group)
        if v:
            v = v[0]
        else:
            #add this user to 'control' variation
            v, created = Variation.objects.get_or_create(
                group = self.group,
                slug = 'control',
                )
            self.profile.variations.add(v)
        self.variation = v
        
    def __getattr__(self, name):
        if name[0] == '_':
            raise AttributeError
            
        #get or create a variation by this name
        variation, created = Variation.objects.get_or_create(
            group = self.group,
            slug = name,
            )
        if variation == self.variation:
            return True
        return False
        
class SuccessRecorder(object):
    def __init__(self, profile):
        self.profile = profile
        
    def __getattr__(self, name):
        if name[0] == '_':
            raise AttributeError
            
        #get or create a goal by this name
        goal, created = Goal.objects.get_or_create(
            slug = name,
            )
        
        success, created = Success.objects.get_or_create(
            profile = self.profile,
            goal = goal,
            )
        
        return True


class Goal(models.Model):
    slug = models.SlugField(max_length=100)
    def __unicode__(self):
        return self.slug
    
class Success(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(MVProfile, related_name='successes')
    goal = models.ForeignKey(Goal, related_name='successes')
    
    def __unicode__(self):
        return str(self.goal)
    
#eof
