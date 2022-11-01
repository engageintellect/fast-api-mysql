from pydantic import BaseModel

class Product(BaseModel):
	date:str
	title:str
	description:str
	link:str


