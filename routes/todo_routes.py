from fastapi import APIRouter
from config.database import collec
from models.todo_models import Todo
from schemas.todos_schema import todo_serializer
from bson import ObjectId
todo_api_router = APIRouter()


@todo_api_router.get("/")
async def get_todos():
    todo_data = collec.find_one()  # Assuming collec is properly initialized
    if todo_data:
        todod = todo_serializer(todo_data)
        return {"status": "success", "data": todod}
    else:
        return {"status": "error", "message": "No todos found"}
@todo_api_router.get("/{id}")
async def get_todo(id: str):
    todo_data = collec.find_one({"id": ObjectId(id)})  
    if todo_data:
        todo = todo_serializer(todo_data)
        return {"status": "ok", "data": todo}
    else:
        return {"status": "error", "message": "Todo not found"}
    

@todo_api_router.post("/")
async def create_todo(todo_data: dict):
    
      
        result = collec.insert_one(todo_data)
        
       
        created_todo = collec.find_one({"_id": result.inserted_id})

        return {"status": "ok", "data": todo_serializer(created_todo)}
@todo_api_router.put("/{todo_id}")
async def update_todo(todo_id: str, todo_data: dict):
    result = await collec.update_one({"_id": ObjectId(todo_id)}, {"$set": todo_data})
    
    if result.modified_count == 1:
       
        updated_todo = await collec.find_one({"_id": ObjectId(todo_id)})
        return {"status": "ok", "data": todo_serializer(updated_todo)}
    else:
        # If the todo item with the specified ID was not found
        return {"status": "error", "message": "Todo item not found"}
@todo_api_router.delete("/{todo_id}")
async def delete_todo(todo_id: str):
   
    result = await collec.delete_one({"_id": ObjectId(todo_id)})
    
    if result.deleted_count == 1:
      
        return {"status": "ok", "message": "Todo item deleted"}
    else:
       
        return {"status": "error", "message": "Todo item not found"}
