from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/admin/config")
def get_config():
    return {
        "message": "Admin configuration settings retrieved successfully."
    }

@router.post("/admin/config")
def update_config(config: dict):
    # Here you would typically update the configuration in your database or settings
    return {
        "message": "Admin configuration updated successfully.",
        "config": config
    }

@router.delete("/admin/config")
def delete_config():
    # Here you would typically delete the configuration from your database or settings
    return {
        "message": "Admin configuration deleted successfully."
    }