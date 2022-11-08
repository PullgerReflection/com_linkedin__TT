import uuid as uuid_class

from django.dispatch import receiver
from django.db import models
from django.db.models import signals, Q
from pullgerReflection.com_linkedin import models as com_linkedin_models
from pullgerReflection.com_linkedin import TaskThread as com_linkedin_TaskThread

from datetime import datetime


class LinkPeopleManager(models.Manager):
    def is_link_exist(self, inUUID):
        objLink = self.filter(people=inUUID).first()
        if objLink is None:
            return False
        else:
            return True

    def get_all_unprocessed_task(self):
        return self.filter(sended=False)


class LinkPeople(models.Model):
    uuid = models.UUIDField(default=uuid_class.uuid4, editable=False, primary_key=True)
    people = models.ForeignKey(com_linkedin_models.people, verbose_name='uuid_people', db_column='uuid_people', to_field='uuid', on_delete=models.CASCADE)
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
    def check_and_create_link(cls, in_model_element):
        if cls.objects.is_link_exist(in_model_element.uuid) is False:
            new_link = cls()
            new_link.people = in_model_element
            new_link.handler = com_linkedin_TaskThread.Operations.PEOPLE.INITIAL_LOAD.name
            new_link.save()


class ExecutionStackLinksManager(models.Manager):
    def is_link_exist(self, uuid_link):
        obj_link = self.filter(uuid_link=uuid_link).first()
        if obj_link is None:
            return False
        else:
            return True

    def get_all_unprocessed_task(self):
        return self.filter(~Q(sent=True) & ~Q(executed=True))

    def get_by_uuid(self=None, uuid: (str, uuid_class) = None):
        if self is None:
            self = ExecutionStackLinks.objects

        return self.filter(uuid=str(uuid)).first()

    def initialization_clear(self):
        self.filter(Q(sent=True) & Q(executed=False)).update(sent=False)


class ExecutionStackLinks(models.Model):
    uuid = models.UUIDField(default=uuid_class.uuid4, editable=False, primary_key=True)
    uuid_link = models.CharField(max_length=36, null=False)
    table = models.CharField(max_length=250, null=False)
    model = models.CharField(max_length=1000, null=False)

    sent = models.BooleanField(default=False)
    sent_moment = models.DateTimeField(default=None, null=True)
    executed = models.BooleanField(default=False)
    executed_moment = models.DateTimeField(default=None, null=True)

    status_code = models.IntegerField(null=True)
    status_description = models.CharField(max_length=1000, null=True)

    error = models.BooleanField(default=False)
    error_code = models.IntegerField(default=None, null=True)

    handler = models.CharField(max_length=100, null=False)
    executor = models.CharField(max_length=120, default=None, null=True)

    description = models.CharField(max_length=500, default='', null=True)
    pull_data = models.TextField()

    objects = ExecutionStackLinksManager()

    def set_sent(self):
        self.sent = True
        self.sent_moment = datetime.now()
        self.save()

    def set_executed(self, error=None, description=None, code=None):
        self.executed = True

        if error is not None:
            self.error = error
        else:
            self.error = False

        if description is not None:
            self.description = description

        if code is not None:
            self.code = code

        self.save()

    def finalize(self=None, uuid=None, status_code=None, status_description=None):
        if self is None:
            self = ExecutionStackLinks.objects.get_by_uuid(uuid)

        self.executed = True
        self.executed_moment = datetime.now()
        self.status_code = status_code
        self.status_description = status_description
        self.save()

    @classmethod
    def check_and_create_link(cls, element, model: str, handler: str):
        if cls.objects.is_link_exist(element.uuid) is False:
            newLink = cls()
            newLink.model = model
            newLink.handler = handler.lower()
            newLink.uuid_link = str(element.uuid)
            newLink.save()
