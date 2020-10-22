import asyncio
import datetime
import websockets

# 接收客户端消息并处理，这里只是简单把客户端发来的返回回去
async def recv_msg(websocket):
    while True:
        now = datetime.datetime.utcnow().isoformat() + "Z"
        recv_text = await websocket.recv()
        print(f'获取到的消息：{recv_text}')
        response_text = f"你发送的消息为: {recv_text} {now}"
        await websocket.send(response_text)

# 服务器端主逻辑
# websocket和path是该函数被回调时自动传过来的，不需要自己传
async def main_logic(websocket, path):
    await recv_msg(websocket)

start_server = websockets.serve(main_logic, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()