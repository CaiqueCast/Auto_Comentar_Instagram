# Auto Comentador no Instagram

## Instalação do Anaconda e Jupyter Notebook

Se você deseja executar este código Python e outros projetos, é recomendável configurar um ambiente Python com o Anaconda e o Jupyter Notebook. Siga os passos abaixo para fazer a instalação:

1. **Baixe o Anaconda:**

   - Acesse o [site oficial do Anaconda](https://www.anaconda.com/products/distribution).
   - Escolha a versão apropriada para o seu sistema operacional (Windows, macOS ou Linux).
   - Baixe o instalador e siga as instruções para instalar o Anaconda no seu computador.

2. **Instale o Anaconda:**

   - Execute o instalador que você baixou.
   - Siga o assistente de instalação e aceite as configurações padrão, a menos que tenha uma razão específica para alterá-las.

3. **Abra o Anaconda Navigator:**

   - Após a instalação, você pode abrir o Anaconda Navigator, que é uma interface gráfica para gerenciar ambientes e pacotes Python. Você pode encontrá-lo no menu de programas (Windows) ou usar o terminal (Linux/macOS) com o comando `anaconda navigator`.

4. **Inicie o Jupyter Notebook:**

   - No Anaconda Navigator, vá para a seção "Home".
   - Certifique-se de que você está no ambiente correto.
   - Clique em "Launch" em "Notebook" para iniciar o Jupyter Notebook no seu navegador.
    ![anacond](https://github.com/CaiqueCast/Auto_Comentar_Instagram/assets/124590909/916e0ad0-84f8-4eb7-8e11-1ba85e0ffe37)



5. **Execute Código Python no Jupyter Notebook:**

   - Agora, você pode criar um novo notebook ou abrir um existente e começar a executar o código Python interativamente no Jupyter Notebook.
    ![jupiter](https://github.com/CaiqueCast/Auto_Comentar_Instagram/assets/124590909/686a0b8a-d1ff-463d-909b-0158a8b24091)



## Descrição do Código

- Aqui você encontra como funciona o [Código do Comentador](https://github.com/CaiqueCast/Auto_Comentar_Instagram/blob/main/codigo.py).

Este código em Python utiliza a biblioteca Selenium para automatizar interações no Instagram. Ele realiza as seguintes etapas:

1. Importação de Bibliotecas:
   - O código começa importando as bibliotecas necessárias, incluindo:
     - `selenium`: para automação do navegador.
     - `pyperclip`: para copiar e colar texto na área de transferência.
     - `pyautogui`: para realizar ações do teclado e mouse.
     - `time`: para adicionar pausas entre as ações.
     - `ActionChains` do Selenium: para realizar ações complexas no navegador.

2. Inicialização do Navegador:
   - Um navegador Chrome é iniciado usando `webdriver.Chrome()`.
   - Uma instância `ActionChains` é criada para facilitar a automação de ações no navegador.

3. Acesso à Página Inicial do Instagram:
   - A página inicial do Instagram é aberta utilizando `navegador.get("https://www.instagram.com/")`.
   - O código espera por 2 segundo (usando `time.sleep(2)`) para garantir que a página seja totalmente carregada.

4. Preenchimento do Formulário de Login:
   - Os campos de e-mail e senha no formulário de login são preenchidos utilizando `send_keys`.

5. Pressionar a Tecla Enter:
   - A tecla Enter é pressionada para efetuar o login no Instagram.

6. Aguardo de 60 Segundos (1 Minuto):
   - O código aguarda por 1 minuto para permitir que o usuário vá para a publicação desejada manualmente.
   - Voce tera 1 minuto para entar na publicação que deseja comentar e clicar no campo de digitação.
   
       ![image](https://github.com/CaiqueCast/Auto_Comentar_Instagram/assets/124590909/16eefae8-d353-4bfe-8815-ee0299dd24ac)
     
7. Loop de Interações (3000 vezes):
   - Inicia um loop que se repetirá 3000 vezes.
   - Em cada iteração do loop, o código aguarda por mais 45 segundos.
   - Espera 45 segundos ate o proximo comentario para o Instagram não te bloquear por Spam.

8. Simulação de Ações de Teclado:
   - Dentro de cada iteração do loop, ele realiza uma ação de teclado simulando a entrada de "O", "k" e a tecla Enter.
   - A lógica exata dessa interação depende do contexto do caso de uso específico e pode estar relacionada a alguma automação de ações específicas no Instagram.

9. Etapa final:  
   - Agora você pode minimizar o navegador que foi aberto e continuar utilizando seu computador normalmente.

### ***Lembre-se de que este código foi feito no Jupiter Notebook, ambiente do Anaconda.***
