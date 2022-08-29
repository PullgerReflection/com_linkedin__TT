from django.test import TestCase
from pullgerReflection.com_linkedin import models as com_linkedin_MODEL
from pullgerReflection.com_linkedin__TT import models as com_linkedin__TT_MODEL
from pullgerReflection.com_linkedin__TT import api as com_linkedin__TT_API


class standardDataStructures():
    @staticmethod
    def personDATA():
        return  {
            'id': None,
            'nick': 'kkonstantin',
            'first_name': 'Konstantin',
            'second_name': 'Kovalenko',
            'full_name': 'Konstantin Kovalenko',
            'discription': 'Full Stack Engineer at Bukovel',
            'url': 'linkedin.com/in/kkonstantin'
        }

class TestDB(TestCase):
    def test_DB1(self):
        modelObject = com_linkedin_MODEL.people

        newObjectInstance = modelObject()
        objectSetDATA = standardDataStructures.personDATA()

        for curField in modelObject._meta.get_fields():
            if hasattr(curField, 'attname'):
                fieldName = getattr(curField, 'attname')
                if fieldName in objectSetDATA:
                    setattr(newObjectInstance, fieldName, objectSetDATA[fieldName])

        newObjectInstance.save()

        #Check set uuid
        self.assertIsNotNone(newObjectInstance.uuid,'UUID not seted')

        #Check link
        self.assertTrue(com_linkedin__TT_MODEL.LinkPeople.objects.isLinkExist(newObjectInstance.uuid), 'Link not created')


        #Check result with reread
        checkNewObjectInstance = modelObject.objects.filter(uuid = newObjectInstance.uuid).first()

        # newObjectInstance.uuid
        for (keyData, valueData) in objectSetDATA.items():
            self.assertEqual(getattr(checkNewObjectInstance,keyData), valueData, f'Incorrect compare DATA on new object in [{keyData}] field: [{getattr(checkNewObjectInstance,keyData)}]<>[{valueData}]')

        from django.apps import apps
        from pullgerMultisessionManager_1 import api as pullgerMM_API

        reglament_app = apps.get_app_config('pullgerMultisessionManager')
        reglament_app.multisessionManager = generator.ConnectionManager()

        com_linkedin__TT_API.sendTaskForProcessing()

        #ADD TEST ACCOUNT
        from pullgerAccountManager.tests import dataFactory
        dataFactory.addLinkedinAccount()
        # ===================================================
        pullgerMM_API.addNewSession()
        pullgerMM_API.executeTask()
        pullgerMM_API.executeTask()
        pullgerMM_API.executeFinalizer()

    def test_SendTaskToTreatment(self):
        pass