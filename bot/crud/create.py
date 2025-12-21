from bot.api import ApiClient, urls_dict
from bot.crud.utils import check_token


async def create_task(access, refresh, state, task):
    headers = {"Authorization": f"Bearer {access}"}
    async with ApiClient(urls_dict.get("base_url")) as client:
        data = await client.post(urls_dict.get("create"), headers=headers, data=task)
        code = data[1]
        if code == 401:
            headers = await check_token(refresh, state)
        data = await client.post(urls_dict.get("create"), headers=headers, data=task)
        return data
