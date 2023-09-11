import uvicorn

from site_project.app import app

if __name__ == "__main__":
    uvicorn.run(app)
