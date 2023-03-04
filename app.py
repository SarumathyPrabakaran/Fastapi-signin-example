from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
import starlette.status as status
from starlette.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

user = {"email": "test4@admin.com", "password": "test123"}


@app.get("/", response_class=HTMLResponse)
async def signin(request: Request):
    return templates.TemplateResponse("signin.html", context={"request": request})


@app.post("/", response_class=RedirectResponse)
async def Validate(request: Request, email: str = Form(...), password: str = Form(...)):
    if(email==user["email"] and password==user["password"]):
        return templates.TemplateResponse("success.html",context={"request":request})    
    else:
        redirect_url = request.url_for('signin')+ '?x-error=Invalid+credentials'
        return RedirectResponse(redirect_url, status_code=status.HTTP_302_FOUND, headers={"x-error": "Invalid credentials"})


if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0", port=8036, reload=True)
