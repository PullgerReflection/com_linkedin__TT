from . import models as MODELS
from pullgerMultiSessionManager import api as pullgerMultiSessionManager_API
from pullgerReflection.com_linkedin import TaskThread as com_linkedin_TASKTHREAD


def send_task_for_processing():
    """
    Send task for processing in pullgerMultiSessionManager
    """
    unprocessedTasks = MODELS.LinkPeople.objects.getAllUnprocessedTask()
    for taskForProcessing in unprocessedTasks:
        oparation_class = com_linkedin_TASKTHREAD.Operations.getOperationClassByName(taskForProcessing.handler)

        parameters = oparation_class.get_multi_session_parameters()
        parameters['uuid_link'] = taskForProcessing.uuid
        parameters['loader'].setObject(taskForProcessing.people)
        parameters['taskFinalizer'] = taskForProcessing.setExecuted

        pullgerMultiSessionManager_API.add_task(**parameters)
        taskForProcessing.setSended()
