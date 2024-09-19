from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from enum import Enum

class Book(SQLModel, table= True):
  id: Optional[int] =  Field(primary_key= True, default= None )
  title: str
  author: Optional[str]
  description: Optional[str]
  owner_id = ""