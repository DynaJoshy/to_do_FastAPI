def todo_serializer(todo) -> dict:
    return {
        "id": todo["id"],  # Corrected from todo[id] to todo["id"]
        "name": todo["name"],
        "description": todo["description"],
        "completed": todo["completed"]
    }

def todomul_serializer(todomul) -> list:
    return [todo_serializer(todo) for todo in todomul]
