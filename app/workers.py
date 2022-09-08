import asyncio
from collections import defaultdict

from concurrent.futures import ThreadPoolExecutor


TOTAL_THREADS = 1


class BackgroundThreads:
    def start(self):
        self.lock = defaultdict(asyncio.Lock)
        self.loop = asyncio.get_running_loop()
        self.executor = ThreadPoolExecutor(TOTAL_THREADS)

    async def run(self, func, *args):
        return await self.loop.run_in_executor(self.executor, func, *args)

    def close(self):
        self.executor.shutdown()


background_threads = BackgroundThreads()
