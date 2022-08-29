from . import models as MODELS
from pullgerMultisessionManager_1 import api as pullgerMultisessionManager_API
from pullgerReflection.com_linkedin import TaskThread as com_linkedin_TASKTHREAD

def sendTaskForProcessing():
    '''
    Send task for processing in pullgerMultisessionManager
    '''
    unprocessedTasks = MODELS.LinkPeople.objects.getAllUnprocessedTask()
    for taskForProcessing in unprocessedTasks:
        OparationClass = com_linkedin_TASKTHREAD.Operations.getOperationClassByName(taskForProcessing.handler)

        parameters = OparationClass.getMultisessionParameters()
        parameters['uuid_link'] = taskForProcessing.uuid
        parameters['loader'].setObject(taskForProcessing.people)
        parameters['taskFinalizer'] = taskForProcessing.setExecuted

        pullgerMultisessionManager_API.addTask(**parameters)
        taskForProcessing.setSended()