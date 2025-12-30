def student_memory(student_id: str):
    return {
        "student_id": student_id,
        "topic_mastery": {
            "ledgers": 0.0,
            "journal_entries": 0.0,
            "trial_balance": 0.0,
        },
        "common_errors": [],
        "last_topic": None,
        "total_interactions": 0
    }