from pydantic import BaseModel

class Project(BaseModel):
	date:str
	title:str
	description:str
	link:str

