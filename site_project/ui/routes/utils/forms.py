from fastapi import Depends, FastAPI, Form, HTTPException, status
from site_project.application.dtos.creation_dto import CoordinatorCreationDTO, TeacherCreationDTO
from fastapi import FastAPI, File, UploadFile

async def get_coordinator_form(
    name: str = Form(...),
    academic_title: str = Form(...),
    curriculum_lattes_url: str = Form(...),
    linkedin_url: str = Form(...),
    photo: UploadFile = File()
    
):
    image = await photo.read()
    coordinator = CoordinatorCreationDTO(
        name=name,
        academic_title=academic_title,
        curriculum_lattes_url=curriculum_lattes_url,
        linkedin_url=linkedin_url,
        photo=image
    )

    return coordinator

async def get_teacher_form(
    name: str = Form(...),
    academic_title: str = Form(...),
    curriculum_lattes_url: str = Form(...),
    related_subjects: list = Form(...),
    areas_of_interest: list = Form(...),
    linkedin_url: str = Form(...),
    photo: UploadFile = File()
    
):
    image = await photo.read()
    teacher = TeacherCreationDTO(
        name=name,
        academic_title=academic_title,
        curriculum_lattes_url=curriculum_lattes_url,
        linkedin_url=linkedin_url,
        related_subjects=related_subjects,
        areas_of_interest=areas_of_interest,
        photo=image
    )

    return teacher