from fastapi import APIRouter, Depends, status, HTTPException, FastAPI
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from app.models.user import User
from app.schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify
router = APIRouter(prefix='/task', tags=['task'])
@router.get('/')
async def all_tasks():
  pass
@router.get('/task_id')
async def task_by_id():
  pass
@router.post('/create')
async def create_task():
  pass
@router.put('/update')
async def update_task():
  pass
@router.put('/delete')
async def delete_task():
  pass
