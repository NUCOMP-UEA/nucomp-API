from fastapi import FastAPI

from site_project.ui.routes.base_user import nucomp_router
from site_project.ui.routes.coordinator import coordinator_router
from site_project.ui.routes.students import student_router
from site_project.ui.routes.teacher import teacher_router

app = FastAPI(
    title="Site do núcleo de computação",
    description="Site destinado aos cursos do núcleo de computação",
)

app.include_router(nucomp_router)
app.include_router(student_router)
app.include_router(teacher_router)
app.include_router(coordinator_router)
