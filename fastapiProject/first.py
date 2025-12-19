from fastapi import FastAPI
api = FastAPI()
all_todo = [
    {'todo_id':1 ,"todo_name":"sports","todo_description":"go to the club"},
    {'todo_id':2 ,"todo_name":"movies","todo_description":"watching spider-man no way home"},
    {'todo_id':3 ,"todo_name":"learning","todo_description":"study calculus"},
    {'todo_id':4 ,"todo_name":"playing","todo_description":"play one hour fifa "},
    {'todo_id':5 ,"todo_name":"cooking","todo_description":"make a seafood soup"}
]

#Get , Post , Put , Delete
@api.get('/')
def index():
    return {"message ": "hello mohamed "}

# localhost:9999/todos
@api.get("/todos/{todo_id}")
def get_todo(todo_id:int):
    for todo in all_todo:
        if todo_id == todo['todo_id']:
            return {'result':todo}
@api.get("/todos")
def get_todos(first_n:int=None):
    if first_n:
        return all_todo[:first_n] if first_n <= len(all_todo) else all_todo
    else:
        return all_todo 
    
@api.post("/todos")
def create_todo(todo:dict):
    new_todo_id  = max(todo['todo_id'] for todo in all_todo) +1 
    new_todo = {
        "todo_id":new_todo_id,
        "todo_name":todo["todo_name"],
        'todo_description':todo['todo_description']
    }
    all_todo.append(new_todo)
    return new_todo

@api.put("/todos/{todo_id}")
def udpate_todo(todo_id:int , updated_todo:dict):
    for todo in all_todo:
        if todo['todo_id'] == todo_id:
            todo["todo_name"] = updated_todo['todo_name']
            todo['todo_description'] = updated_todo['todo_description']
            return todo
    return "error , not found "

@api.delete("/todos/{todo_id}")
def delete_todo(todo_id:int ):
    for index,todo in enumerate(all_todo):
        if todo['todo_id'] ==todo_id:
            deleted_todo = all_todo.pop(index)
            return deleted_todo
        
    return "error , not found "