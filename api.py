from . import models as MODELS
from pullgerMultiSessionManager import apiMSM as pullgerMultiSessionManager_API
from pullgerReflection.com_linkedin import TaskThread as com_linkedin_TASKTHREAD


def send_task_for_processing():
    """
    Send task for processing in pullgerMultiSessionManager
    """
    unprocessedTasks = MODELS.LinkPeople.objects.get_all_unprocessed_task()
    for taskForProcessing in unprocessedTasks:
        oparation_class = com_linkedin_TASKTHREAD.Operations.getOperationClassByName(taskForProcessing.handler)

        parameters = oparation_class.get_multi_session_parameters()
        parameters['uuid_link'] = taskForProcessing.uuid
        parameters['loader'].setObject(taskForProcessing.people)
        parameters['taskFinalizer'] = taskForProcessing.setExecuted

        pullgerMultiSessionManager_API.add_task(**parameters)
        taskForProcessing.setSended()


def send_all_task_for_processing():
    unprocessed_tasks = MODELS.ExecutionStackLinks.objects.get_all_unprocessed_task()
    for task_for_processing in unprocessed_tasks:
        pullgerMultiSessionManager_API.add_sync_task(task_for_processing)
    return len(unprocessed_tasks)
