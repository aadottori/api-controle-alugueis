from fastapi import FastAPI, Request
import models, database
from database import engine, get_db
from routers import room, people, payment, user, authentication, mainpage
import uvicorn


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API do Dottori Alugueis")

get_db = database.get_db

app.include_router(authentication.router)
app.include_router(room.router)
app.include_router(people.router)
app.include_router(payment.router)
app.include_router(user.router)
app.include_router(mainpage.router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
