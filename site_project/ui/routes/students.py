from fastapi import FastAPI, APIRouter,status

# Create an instance of APIRouter
client_router = APIRouter()

@client_router.get("/")
async def read_root():
    return {"message": "Hello, this is the root endpoint!"}

@client_router.post("/Signup",status_code=status.HTTP_201_CREATED)
async def create_client_user(student):
    return {"message": "user successfully created"}