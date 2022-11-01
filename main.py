#!/usr/bin/env python3
from fastapi import FastAPI
from data import *
from config.db import con
# SCHEMAS
from schemas.release import Release
from schemas.project import Project
from schemas.product import Product
# MODELS
from models.index import releases
from models.index import projects
from models.index import products

# API
app = FastAPI()

# ROOT
@app.get("/")
async def root():
    return root_msg

# INFO
@app.get("/api/info")
async def getInfo():
    return info

# ABOUT
@app.get("/api/about")
async def getAbout():
    return about


#------------------------------------------------------------------------------------------------
# RELEASES
#------------------------------------------------------------------------------------------------

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

#------------------------------------------------------------------------------------------------
# PROJECTS
#------------------------------------------------------------------------------------------------

#-----------------------
# GET PROJECTS
#-----------------------
@app.get("/api/projects")
async def getProjects():
    data=con.execute(projects.select()).fetchall()
    if data:
        return {
            "success": True,
            "data": data,
        }
    else:
        return {
            "success": False,
            "msg": "No projects found."
        }

#-----------------------
# CREATE PROJECT
#-----------------------
@app.post("/api/projects")
async def store(project:Project):
    data=con.execute(projects.insert().values(
        date=project.date,
        title=project.title,
        description=project.description,
        link=project.link,
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
# EDIT PROJECT
#-----------------------
@app.put('/api/projects/{id}')
async def edit(id:int):
    data=con.execute(projects.select().where(projects.c.id==id)).fetchall()
    return {
        "success": True,
        "data": data,
    }

#-----------------------
# UPDATE PROJECT
#-----------------------
@app.patch('/api/projects/{id}')
async def update(id:int, project:Project):
    data=con.execute(projects.update().values(
        date=project.date,
        title=project.title,
        description=project.description,
        link=project.link,
    ).where(projects.c.id==id))
    if data:
        return {
            "success": True,
            "msg": "Project update succuessful."
        }
    else:
        return {
            "success": False,
            "msg": "Project update failed."
        }

#-----------------------
# DELETE PROJECT
#-----------------------
@app.delete('/api/projects/{id}')
async def delete(id:int):
    data=con.execute(projects.delete().where(projects.c.id==id))
    if data:
        return {
            "success": True,
            "msg": "Project delete succuessful."
        }
    else:
        return {
            "success": False,
            "msg": "Project delete failed."
        }

#-----------------------
# SEARCH PROJECT
#-----------------------
@app.get('/api/projects/{search}')
async def search(search):
    data=con.execute(projects.select().where(projects.c.title.like
    ('%'+search+'%'))).fetchall()
    return {
        "success": True,
        "data": data,
    }

#------------------------------------------------------------------------------------------------
# PRODUCTS
#------------------------------------------------------------------------------------------------

#-----------------------
# GET PRODUCTS
#-----------------------
@app.get("/api/products")
async def getProducts():
    data=con.execute(products.select()).fetchall()
    if data:
        return {
            "success": True,
            "data": data,
        }
    else:
        return {
            "success": False,
            "msg": "No products found."
        }

#-----------------------
# CREATE PRODUCT
#-----------------------
@app.post("/api/products")
async def store(product:Product):
    data=con.execute(products.insert().values(
        date=product.date,
        title=product.title,
        description=product.description,
        link=product.link,
    ))
    if data.is_insert:
        return {
            "success": True,
            "msg": "Product store successful."
        }
    else:
        return {
            "success": False,
            "msg": "Product failed to store.",
        }

#-----------------------
# EDIT PRODUCT
#-----------------------
@app.put('/api/products/{id}')
async def edit(id:int):
    data=con.execute(products.select().where(products.c.id==id)).fetchall()
    return {
        "success": True,
        "data": data,
    }

#-----------------------
# UPDATE PRODUCT
#-----------------------
@app.patch('/api/products/{id}')
async def update(id:int, product:Product):
    data=con.execute(products.update().values(
        date=product.date,
        title=product.title,
        description=product.description,
        link=product.link,
    ).where(products.c.id==id))
    if data:
        return {
            "success": True,
            "msg": "Product update succuessful."
        }
    else:
        return {
            "success": False,
            "msg": "Product update failed."
        }

#-----------------------
# DELETE PRODUCT
#-----------------------
@app.delete('/api/products/{id}')
async def delete(id:int):
    data=con.execute(products.delete().where(products.c.id==id))
    if data:
        return {
            "success": True,
            "msg": "Product delete succuessful."
        }
    else:
        return {
            "success": False,
            "msg": "Product delete failed."
        }

#-----------------------
# SEARCH PRODUCT
#-----------------------
@app.get('/api/products/{search}')
async def search(search):
    data=con.execute(products.select().where(products.c.title.like
    ('%'+search+'%'))).fetchall()
    return {
        "success": True,
        "data": data,
    }






