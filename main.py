from fastapi import FastAPI
from Router.instrument import new_app

app = FastAPI()
app.include_router(new_app)


@app.get("/")
def root():
    return {"message": "Hi welcome to Employee Asset Management"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
