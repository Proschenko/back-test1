from app.database import get_db_pool

async def get_wells_by_organization(organization_name: str):
    pool = await get_db_pool()
    async with pool.acquire() as conn:
        query = """
            SELECT w.id, w.uwi, w."number", o.short_name_ru, f.short_name_en, w.fin_drill
            FROM eav.well w
            JOIN eav.organization o ON w.novatek_owner = o.id
            JOIN eav.field f ON w.deposit = f.id
            WHERE o.short_name_ru = $1
        """
        result = await conn.fetch(query, organization_name)
    return result
