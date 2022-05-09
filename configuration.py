def kafkaTopics():
    topics = [
    "notConfiguredTopic",
    "integration"
    ]
    return topics

def getActionCommand(actionType,target):
    if actionType == "startContainer":
        returnCommand = "docker run {}".format(target)
    if actionType == "log":
        returnCommand = "echo 'This is a Test-Log to the terminal!'"
    return returnCommand