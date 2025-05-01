from fastapi import FastAPI
import pyautogui
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

# Página HTML com um botão para acionar o press-space
html_content = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pressionar Espaço</title>
     <style>
        /* CSS para aumentar o tamanho do botão */
        button {
            font-size: 20px;         /* Tamanho da fonte */
            padding: 15px 30px;      /* Aumenta o tamanho do botão */
            width: 300px;            /* Largura fixa */
            height: 60px;            /* Altura fixa */
            background-color: #4CAF50; /* Cor de fundo */
            color: white;            /* Cor da fonte */
            border: none;            /* Remove a borda */
            border-radius: 10px;     /* Bordas arredondadas */
            cursor: pointer;        /* Muda o cursor para indicar interatividade */
            transition: background-color 0.3s ease; /* Efeito ao passar o mouse */
            margin:20px;
        }

        button:hover {
            background-color: #45a049; /* Cor do botão ao passar o mouse */
        }
    </style>
</head>
<body>
    <h1>Pressione o botão para simular o pressionamento da tecla espaço</h1>
    <button onclick="pressSpace()">Pressionar Espaço</button>

    <script>
        function pressSpace() {
            fetch("http://192.168.0.2:8080/press-space", { method: "POST" })
                .then(response => response.json())
                .catch(error => console.error('Erro:', error));
        }
    </script>

      <button onclick="pressFkey()">Pressionar o F</button>

    <script>
        function pressFkey() {
            fetch("http://192.168.0.2:8080/press-fullscreen", { method: "POST" })
                .then(response => response.json())
                .catch(error => console.error('Erro:', error));
        }
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def get_html():
    return html_content

@app.post("/press-space")
def press_space():
    pyautogui.press('space')
    return   {"message": "Tecla espaço pressionada com sucesso"}

@app.post("/press-fullscreen")
def press_space():
    pyautogui.press('F')
    return   {"message": "Tecla F pressionada com sucesso"}

# Para rodar o servidor com uvicorn
if __name__ == "__main__":
    uvicorn.run("Server:app", host="0.0.  0.0", port=8080, reload=True)
