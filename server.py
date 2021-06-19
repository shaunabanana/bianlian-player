#!/usr/bin/env python

import asyncio
import websockets

filenames = [
    '1鸡哥不屑.json',
    '2鸡哥左右看.json',
    '3鸡哥邪魅一笑.json',
    '4鸡哥不赞同的目光.json',
    '5鸡哥无语.json',
    '6鸡哥大为震撼.json',
    '7鸡哥眨眼.json',
    '8鸡哥睁大眼睛.json'
];

async def echo(websocket, path):
    while True:
        for filename in filenames:
            await websocket.send(filename)
            await asyncio.sleep(2);

start_server = websockets.serve(echo, "localhost", 8765)
print('Starting server at ws://localhost:8765')
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()