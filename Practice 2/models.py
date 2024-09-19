from enum import Enum
from sqlmodel import SQLModel, Relationship, Field
from typing import Optional, List


class RaceType(str, Enum):
    director = "director"
    worker = "worker"
    junior = "junior"


class Profession(SQLModel, table= True):
    id : Optional[int] = Field(primary_key= True, default=None)
    name: str
    description:  Optional[str]
    warriors: List["Warrior"] = Relationship(back_populates='proffession')

class WarriorSkillLink(SQLModel, table= True):
    warrior_id : Optional[int] = Field(primary_key= True, foreign_key= 'warrior.id', default=None)
    skill_id : Optional[int] = Field(primary_key=True, foreign_key="skill.id", default=None)

class Skill(SQLModel, table= True):
    id : Optional[int] = Field(primary_key= True, default=None)
    name: str
    description:  Optional[str]
    warriors: Optional[List["Warrior"]] = Relationship(back_populates="skills", link_model=WarriorSkillLink)


class Warrior(SQLModel, table= True):
    id : Optional[int] = Field(primary_key= True, default=None)
    race: RaceType
    name: str
    level: int
    Proffesion_id: Optional[int]= Field(foreign_key='profession.id')
    profession: Optional[Profession] =  Relationship( back_populates='warriors')
    skills: Optional[List[Skill]] = Relationship(back_populates="warriors", link_model=WarriorSkillLink)
