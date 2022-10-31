from fastapi import FastAPI
from data import *
from schemas.release import Release
from config.db import con
from models.index import releases

#--------------------------
# API
#--------------------------
app = FastAPI()

#-----------------------
# ROOT
#-----------------------
@app.get("/")
async def root():
    return root_msg

#-----------------------
# INFO
#-----------------------
@app.get("/api/info")
async def getInfo():
    return info

#-----------------------
# ABOUT
#-----------------------
@app.get("/api/about")
async def getAbout():
    return about


#------------------------------------------------
# RELEASES
#------------------------------------------------

#-----------------------
# GET RELEASES
#-----------------------
@app.get("/api/releases")
async def getAbout():
    data=con.execute(releases.select()).fetchall()
    return {
        "success": True,
        "data": data,
    }


#-----------------------
# CREATE RELEASE
#-----------------------
@app.post("/api/releases")
async def store(release:Release):
    data=con.execute(releases.insert().values(
        date=release.date,
        title=release.title,
        description=release.description,
        link=release.link,
    ))
    if data.is_insert:
        return {
            "success": True,
            "msg": "Release note store successful."
        }
    else:
        return {
            "success": False,
            "msg": "Release note failed to store.",
        }


#-----------------------
# EDIT RELEASE
#-----------------------
@app.put('/api/releases/{id}')
async def edit(id:int):
    data=con.execute(releases.select().where(releases.c.id==id)).fetchall()
    return {
        "success": True,
        "data": data,
    }

#-----------------------
# UPDATE RELEASE
#-----------------------
@app.patch('/api/releases/{id}')
async def update(id:int, release:Release):
    data=con.execute(releases.update().values(
        date=release.date,
        title=release.title,
        description=release.description,
        link=release.link,
    ).where(releases.c.id==id))
    if data:
        return {
            "success": True,
            "msg": "Release update succuessful."
        }
    else:
        return {
            "success": False,
            "msg": "Release update failed."
        }



#-----------------------
# DELETE RELEASE
#-----------------------
@app.delete('/api/releases/{id}')
async def delete(id:int):
    data=con.execute(releases.delete().where(releases.c.id==id))
    if data:
        return {
            "success": True,
            "msg": "Release delete succuessful."
        }
    else:
        return {
            "success": False,
            "msg": "Release delete failed."
        }


#-----------------------
# SEARCH RELEASE
#-----------------------
@app.get('/api/releases/{search}')
async def search(search):
    data=con.execute(releases.select().where(releases.c.title.like
    ('%'+search+'%'))).fetchall()
    return {
        "success": True,
        "data": data,
    }

#!----------------------------------
#! TODO: Add CRUD logic.
#!----------------------------------

#------------------------------------------------
# PROJECTS
#------------------------------------------------

#-----------------------
# GET PROJECTS
#-----------------------
@app.get("/api/projects")
async def getProjects():
    return projects

#------------------------------------------------
# PRODUCTS
#------------------------------------------------

#-----------------------
# GET PRODUCT
#-----------------------
@app.get("/api/products")
async def getProducts():
    return products

