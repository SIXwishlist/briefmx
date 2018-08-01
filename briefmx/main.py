import asyncio
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


async def client_connected(reader, writer):
    addr = writer.get_extra_info('peername')
    logger.info(f"New connection: {addr}")
    writer.write("220 smtp.briefmx.com ESMTP BriefMX\n".encode('utf-8'))
    writer.write("554 No SMTP service here\n".encode('utf-8'))
    await writer.drain()
    logger.info("Closing client connection")
    writer.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    server = asyncio.start_server(client_connected, '127.0.0.1', 2525, loop=loop)
    loop.run_until_complete(server)
    logger.info("Server started")
    loop.run_forever()
