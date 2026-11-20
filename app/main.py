from fastapi import FastAPI
from app.api import routes_prices, routes_subs, routes_admin

app = FastAPI(title="Crop Price AI Agent")

# Register routes
app.include_router(routes_prices.router, prefix="/api")
app.include_router(routes_subs.router, prefix="/api")
app.include_router(routes_admin.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Crop Price Agent running!"}