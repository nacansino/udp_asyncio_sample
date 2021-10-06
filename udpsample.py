"""aioudp from https://gist.github.com/vxgmichel/e47bff34b68adb3cf6bd4845c4bed448"""

import asyncio
from aioudp import open_local_endpoint, open_remote_endpoint

async def sender_loop():
    # Create a remote UDP enpoint, pointing to the first one
    remote = await open_remote_endpoint(host="127.0.0.1", port=56224)

    while True:
        # The remote endpoint sends a datagram
        print("trysend...")
        remote.send(b'Hey Hey, My My')
        await asyncio.sleep(0.75)

async def tulogmuna():
    while True:
        print("Epal lng...")
        await asyncio.sleep(1)

async def receiver_loop(port=8514):
    endpoint = await open_local_endpoint(port=port)
    print(f"The UDP server is running on port {endpoint.address[1]}...")
    while True:
        data, (host, port) = await endpoint.receive()
        print(f"Received {len(data)} bytes from {host}:{port}")
        print(">", data)


if __name__ == "__main__":
    asyncio.get_event_loop().create_task(sender_loop())
    asyncio.get_event_loop().run_until_complete(receiver_loop())