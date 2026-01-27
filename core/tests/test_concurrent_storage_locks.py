import asyncio
from framework.storage.concurrent import ConcurrentStorage

async def _touch(storage, key):
    async with storage._get_lock(key):
        pass

def test_file_lock_cache_is_bounded(tmp_path):
    storage = ConcurrentStorage(tmp_path, max_locks=5)

    async def run():
        for i in range(20):
            await _touch(storage, f"file_{i}")

    asyncio.run(run())

    assert len(storage._file_locks) <= 5
