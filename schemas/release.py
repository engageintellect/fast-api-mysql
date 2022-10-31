from pydantic import BaseModel

class Release(BaseModel):
	date:str
	title:str
	description:str
	link:str
