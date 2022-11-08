from django.db.models import signals
from django.dispatch import receiver
from pullgerReflection.com_linkedin import models as models_core
from pullgerReflection.com_linkedin__TT import models
from pullgerInternalControl import pIC_pR


@receiver(signals.post_save, sender=models_core.People)
# @receiver(signals.post_save, sender=models_core.Companies)
@receiver(signals.post_save, sender=models_core.SearchRequests)
def add_taskflow_on_crating(sender, instance, created, **kwargs):
    if created is True:
        try:
            models.ExecutionStackLinks.check_and_create_link(
                element=instance,
                model=sender.__module__ + '.' + sender.__qualname__,
                handler='sync'
            )
        except BaseException as e:
            raise pIC_pR.TT.LinkCreate(
                'Unexpected error on creating LINK',
                level=50,
                exeptation=e
            )