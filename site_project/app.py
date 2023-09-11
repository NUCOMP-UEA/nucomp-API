from fastapi import FastAPI

from site_project.ui.routes.base_user import nucomp_router
from site_project.ui.routes.coordinator import coordinator_router
from site_project.ui.routes.students import student_router
from site_project.ui.routes.teacher import teacher_router
from site_project.ui.routes.news_router import news_router
from site_project.ui.routes.articles_router import articles_router
from site_project.ui.routes.events_router import events_router

app = FastAPI(
    title="Site do núcleo de computação",
    description="Site destinado aos cursos do núcleo de computação",
)

app.include_router(nucomp_router, tags=["base"])
app.include_router(student_router, tags=["student"])
app.include_router(teacher_router, tags=["teacher"])
app.include_router(coordinator_router, tags=["coordinator"])
app.include_router(news_router, tags=["news"])
app.include_router(articles_router,tags=["articles"])
app.include_router(events_router, tags=["events"])