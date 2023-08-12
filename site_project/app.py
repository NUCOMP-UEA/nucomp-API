from fastapi import FastAPI
from site_project.ui.routes.students import student_router

app = FastAPI(title="Site do núcleo de computação")

app.include_router(student_router)
