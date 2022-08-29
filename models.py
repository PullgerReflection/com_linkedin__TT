from django.dispatch import receiver
from django.db import models
from django.db.models import signals
from pullgerReflection.com_linkedin import models as com_linkedin_models
from pullgerReflection.com_linkedin import TaskThread as com_linkedin_TaskThread
import uuid

'''
Proceduce of update structure (add new dataType)
1. Update api function: [sentTaskForProcessing] (add processing of data)  
 
'''



class LinkPeopleManager(models.Manager):
    def isLinkExist(self, inUUID):
        objLink = self.filter(people=inUUID).first()
        if objLink == None:
            return False
        else:
            return True

    def getAllUnprocessedTask(self):
        return self.filter(sended=False)

class LinkPeople(models.Model):
    uuid = models.CharField(max_length=36, primary_key = True)
    people = models.ForeignKey(com_linkedin_models.people, verbose_name = 'uuid_people', db_column='uuid_people', to_field = 'uuid', on_delete=models.CASCADE)
    handler = models.CharField(max_length=100, null=False)
    sended = models.BooleanField(default=False)
    sended_moment = models.DateTimeField(default=None, null=True)
    executor = models.CharField(max_length=120, default=None, null=True)
    executed = models.BooleanField(default=False)
    error = models.BooleanField(default=False)
    error_code = models.IntegerField(default=None, null=True)
    discription = models.CharField(max_length=500, default='', null=True)

    objects = LinkPeopleManager()

    def setSended(self):
        self.sended = True;
        self.save()

    def setExecuted(self, **kwargs):
        self.executed = True
        if 'error' in kwargs:
            self.error = kwargs['error']
        else:
            self.error = False
        if 'discription' in kwargs:
            self.discription = kwargs['discription']
        if 'code' in kwargs:
            self.code = kwargs['code']
        self.save()

    @classmethod
    def checkAndCreateLink(cls, inModelElement):
        if cls.objects.isLinkExist(inModelElement.uuid) == False:
            newLink = cls()
            newLink.people = inModelElement
            newLink.handler = com_linkedin_TaskThread.Operations.PEOPLE.INITIAL_LOAD.name
            newLink.save()



@receiver(signals.pre_save, sender=LinkPeople)
def add_LinkPeople_uuid(sender, instance, **kwargs):

    if not instance.uuid:
        instance.uuid = str(uuid.uuid4())
