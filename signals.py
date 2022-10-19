from django.db.models import signals
from django.dispatch import receiver
from pullgerReflection.com_linkedin import models as com_linkedin_models
from pullgerReflection.com_linkedin__TT import models as com_linkedin__TT_MODELS
from pullgerInternalControl import pIC_pR


@receiver(signals.post_save, sender=com_linkedin_models.people)
def add_taskflow_on_crating(sender, instance, **kwargs):
    if instance.uuid is not None:
        try:
            com_linkedin__TT_MODELS.LinkPeople.checkAndCreateLink(instance)
        except BaseException as e:
            raise pIC_pR.TT.LinkCreate(
                'Unexpected error on creating LINK',
                level=50,
                exeptation=e
            )