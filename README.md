⚙️ Pré-requisitos
Python 3.8+: Instalado na sua máquina (Download).

R 4.0+: Instalado (Download).

Pacotes R:

r
Copy
install.packages(c("httr", "dplyr"))  # Execute no RStudio ou terminal R  
🛠 Como Usar
Passo 1: Execute o Código Python
Navegue até a pasta python/:

bash
Copy
cd caminho/para/projeto/python  
Execute:

bash
Copy
python agricultura.py  
Use o menu para adicionar culturas e insumos. Ao sair (opção 6), o arquivo plantio.csv será gerado.

Passo 2: Execute o Código R
Navegue até a pasta R/:

bash
Copy
cd caminho/para/projeto/R  
Abra o RStudio ou terminal R e execute:

r
Copy
source("analise.R")  
Saída esperada:

Copy
[1] "Média das áreas: 89.25 m²"  
[1] "Temperatura atual em São Paulo: 22 °C"  
❗ Importante: Caminho do CSV
O R precisa encontrar o plantio.csv gerado pelo Python. Para isso:

Certifique-se de que o arquivo plantio.csv está na pasta python/ após executar o Python.

No código R (analise.R), ajuste o caminho do CSV:

r
Copy
# Substitua pelo caminho absoluto do seu arquivo  
plantio <- read.csv("../python/plantio.csv")  # ".." sobe um nível na pasta  
🐛 Solução de Problemas
Erro: "não é possível abrir o arquivo 'plantio.csv'
Causa: O R não está encontrando o CSV.

Solução:

Verifique se o CSV foi gerado pelo Python na pasta python/.

No R, use o caminho absoluto:

r
Copy
plantio <- read.csv("C:/projeto/python/plantio.csv")  
📝 Exemplo de Uso
No Python:
python
Copy
# Adicionar café (área retangular)  
Digite a opção desejada: 1  
Cultura: café  
Largura (m): 10  
Comprimento (m): 20  
Insumo: fosfato  
No R:
r
Copy
# Saída após executar analise.R  
[1] "Média das áreas: 200.00 m²"  
[1] "Temperatura atual em São Paulo: 24 °C"  
📚 Melhorias Futuras
Adicionar interface gráfica (Python: Tkinter / R: Shiny).

Incluir previsão de produtividade baseada no clima.

Suporte a mais culturas (ex: soja, trigo).

🤝 Contribuição
Contribuições são bem-vindas! Siga os passos:

Faça um fork do projeto.

Crie uma branch: git checkout -b feature/nova-funcionalidade.

Commit: git commit -m 'Adicionei X'.

Push: git push origin feature/nova-funcionalidade.

Abra um Pull Request.

📄 Licença
Distribuído sob a licença MIT. Veja LICENSE para mais detalhes.

Copy

---

## 📌 Como Salvar o README  
1. Crie um arquivo chamado **`README.md`** na **pasta raiz do projeto**.  
2. Copie o conteúdo acima e cole no arquivo.  
3. **Dica:** Use o [Visual Studio Code](https://code.visualstudio.com/) para visualizar a formatação Markdown.  

![Estrutura Final](https://static.vecteezy.com/system/resources/previews/016/017/621/non_2x/file-folder-icon-free-vector.jpg)  
*Organize assim e seu projeto estará pronto para compartilhamento!* 🌟
