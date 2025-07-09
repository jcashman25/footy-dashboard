# routes
from fastapi import APIRouter

router = APIRouter(prefix="/api")

@router.get("/matches/today")
def get_today_matches():
    # Placeholder - replace with API call to API-Football
    return {"matches": ["Team A vs Team B"]}