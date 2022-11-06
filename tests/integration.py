# from pullgerReflection.com_linkedin.tests import dataTemplate as dataTemplate_com_linkedin
from pullgerReflection.com_linkedin.tests import unit as unit_com_linkedin
from pullgerMultiSessionManager import apiMSM as pullgerMM__API
from django.test import TestCase

class Test_1_000_FullCircle(TestCase):
    def test_000_PeopleLoad(self):
        # pDATA = dataTemplate_com_linkedin.person_DATA()
        uuid_people = unit_com_linkedin.UnitOperations.add_people(self)

        from pullgerAccountManager.tests.unit import UnitOperations as UnitOperations__AM
        UnitOperations__AM.add_account(self, configuration=None)

        from pullgerMultiSessionManager.tests.tools import UnitOperations as UnitOperations__MM
        UnitOperations__MM.AddNewLinkeinSession(self)

        from pullgerMultiSessionManager import apiMSM
        api.make_all_session_authorization()

        from pullgerReflection.com_linkedin__TT import api as com_linkedin__TT_API
        com_linkedin__TT_API.send_task_for_processing()

        pullgerMM__API.executeTask()
        pullgerMM__API.executeTask()

        pullgerMM__API.execute_finalizer()
        pass
