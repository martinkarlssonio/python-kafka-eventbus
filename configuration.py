"""
This file holds configuration used in the service. Both which topics that's onboarder but also what kind of actions that is allowed.
"""
def kafkaTopics():
    """
    Returns the configured topics.
    """
    topics = [
    "notConfiguredTopic",
    "integration"
    ]
    return topics

def getActionCommand(actionType,target):
    """
    Returns a UNIX command to be executed for the specific actionType
    """
    if actionType == "startContainer":
        returnCommand = "docker run {}".format(target)
    if actionType == "log":
        returnCommand = "echo 'This is a Test-Log to the terminal!'"
    return returnCommand