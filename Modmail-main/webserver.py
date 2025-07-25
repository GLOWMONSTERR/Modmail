import os
from sanic import Sanic, response

app = Sanic("modmail_ping")

@app.get("/ping")
async def ping(request):
    return response.text("Pong", status=200)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8080)),
        single_process=True
    )
