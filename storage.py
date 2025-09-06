import asyncio
from pathlib import Path


class IDStorage:
    def __init__(self, filename="subscribed_IDS.txt"):
        self.filename = filename
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        Path(self.filename).touch(exist_ok=True)

    async def get_all_ids(self) -> list:

        def read_file():
            with open(self.filename, "r") as f:
                return [line.strip() for line in f if line.strip()]

        return await asyncio.to_thread(read_file)

    async def add_id(self, chat_id: str) -> bool:

        async def write_operation():
            ids = await self.get_all_ids()
            if chat_id not in ids:
                with open(self.filename, "a") as f:
                    f.write(chat_id + "\n")
                return True
            return False

        return await write_operation()

    async def remove_id(self, chat_id: str) -> bool:

        async def write_operation():
            ids = await self.get_all_ids()
            if chat_id in ids:
                ids.remove(chat_id)
                with open(self.filename, "w") as f:
                    for value in ids:
                        f.write(value + "\n")
                return True
            return False

        return await write_operation()

    async def contains_id(self, chat_id: str) -> bool:
        ids = await self.get_all_ids()
        return chat_id in ids