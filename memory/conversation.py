def append_history(history, user, assistant=None):
    history.append({
        f"User": {user},
    })
    if assistant:
        history.append({f"Agent": {assistant}})
    return history