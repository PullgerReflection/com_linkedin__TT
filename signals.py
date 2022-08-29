from django.db.models import signals
from django.dispatch import receiver
from pullgerReflection.com_linkedin import models as com_linkedin_models
from pullgerReflection.com_linkedin__TT import models as com_linkedin__TT_MODELS
from pullgerReflection.exceptions import *

LOGGER_NAME = "pullger.Reflection.com_linkedin.TaskFlow.integrationSignals"

@receiver(signals.post_save, sender=com_linkedin_models.people)
def add_taskflow_on_crating(sender, instance, **kwargs):
    if instance.uuid != None:
        try:
            com_linkedin__TT_MODELS.LinkPeople.checkAndCreateLink(instance)
        except BaseException as e:
            raise excReflections_TT_LinkCreate('Unexpected error on creating LINK', loggerName=LOGGER_NAME, level=50, exeptation=e)