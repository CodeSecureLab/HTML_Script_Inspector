import aiohttp

async def get_latest_version_cdnjs(module_name):
    async with aiohttp.ClientSession() as session:
        module_name_stripped = module_name.replace(".js", "")
        async with session.get(f"https://registry.npmjs.org/{module_name_stripped}/latest") as response:
            if response.status == 200:
                data = await response.json()
                return data.get("version")
            else:
                return "Not Found"

