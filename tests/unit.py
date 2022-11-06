from pullgerReflection.com_linkedin.tests import unit as unit_com_linkedin
from pullgerReflection.com_linkedin__TT import models as com_linkedin__TT_MODEL
from django.test import TestCase


class Test_1_001_CreateLinks(TestCase):
    def test_001_PeopleCreate(self):
        uuid_people = unit_com_linkedin.UnitOperations.add_people(self)
        self.assertTrue(com_linkedin__TT_MODEL.LinkPeople.objects.is_link_exist(uuid_people), 'Task threat not created')
        pass

