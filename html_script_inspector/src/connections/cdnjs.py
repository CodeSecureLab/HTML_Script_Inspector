import aiohttp

async def get_latest_version_cdnjs(module_name):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.cdnjs.com/libraries/{module_name}") as response:
            if response.status == 200:
                data = await response.json()
                return data['version']
            else:
                return "Not Found"

