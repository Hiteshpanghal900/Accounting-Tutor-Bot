def build_tutor_prompt(system_prompt, context, student_message, memory):
    memory_summary = f"""
    Student Memory:
    - Last topic : {memory.get('last_topic')}
    - Topic Mastery: {memory.get('topic_mastery')}
    - Common Errors: {memory.get('common_errors')}
    """

    return f"""
    {system_prompt}

    {memory_summary}

    CONTEXT: {context}

    Student says: {student_message}

    """