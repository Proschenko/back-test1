from fastapi import APIRouter
from app.services import get_wells_by_organization
from pydantic import BaseModel

router = APIRouter()

class OrganizationRequest(BaseModel):
    organization_name: str

@router.post("/wells")
async def get_wells(request: OrganizationRequest):
    wells = await get_wells_by_organization(request.organization_name)
    return {"wells": wells}
