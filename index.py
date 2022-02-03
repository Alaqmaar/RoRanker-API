import fastapi
import roblox

cookie = ''
authKey = ''

app = fastapi.FastAPI()
client = roblox.Client(cookie)

@app.get('/')
def main():
    return

@app.get('/{playerUsername}/{groupId}/{toRank}/{key}')
async def setRank(playerUsername: str, groupId: int, toRank: int, key: str):

    if key == authKey:
        group = await client.get_group(groupId)
        member = await group.get_member_by_username(playerUsername)

        await member.set_rank(toRank)
