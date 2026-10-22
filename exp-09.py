
def classify_stage(activity):
    activity = activity.lower()

    keywords = {
        "Direction": [
            "define objectives", "set requirements",
            "identify intelligence needs", "priorities"
        ],
        "Collection": [
            "gather data", "collect logs",
            "gather threat feeds", "collect information"
        ],
        "Processing": [
            "clean data", "normalize logs",
            "remove duplicates", "convert data"
        ],
        "Analysis": [
            "analyze threats", "identify patterns",
            "investigate indicators", "correlate events"
        ],
        "Dissemination": [
            "share report", "distribute intelligence",
            "send findings", "deliver report"
        ],
        "Feedback": [
            "provide feedback", "review usefulness",
            "improve future intelligence", "request changes"
        ]
    }

    scores = {
        stage: sum(1 for word in words if word in activity)
        for stage, words in keywords.items()
    }

    best_stage = max(scores, key=scores.get)

    if scores[best_stage] == 0:
        return "Stage not identified"

    return best_stage


activity = input("Describe the intelligence team activity: ")
stage = classify_stage(activity)

print("Activity:", activity)
print("Lifecycle Stage:", stage)
