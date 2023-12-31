import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware


from app.api.api import api_router


app = FastAPI(title="Transfermarkt API")
app.include_router(api_router)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to specific origins in a production environment
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
