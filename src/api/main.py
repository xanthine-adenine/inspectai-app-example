from fastapi import FastAPI

app = FastAPI(
    title="Inspect AI App Example",
    description="A simple example of building an app that uses the Inspect framework",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {"message": "Welcome to Inspect AI App Example"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
