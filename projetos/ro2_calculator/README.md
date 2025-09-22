# Projeto 2: Calculadora com Service/Client em ROS 2

[cite_start]Este projeto foi desenvolvido como parte do programa de treinamento de trainees da equipe de robótica EDROM[cite: 2]. [cite_start]O objetivo é demonstrar a implementação de um sistema de comunicação síncrona (requisição-resposta) utilizando Serviços (Services) em ROS 2[cite: 35].

[cite_start]O sistema consiste em um nó **Servidor** que aguarda por um pedido, e um nó **Cliente** que faz esse pedido e espera por uma resposta[cite: 36]. [cite_start]Este padrão é ideal para tarefas que necessitam de uma confirmação ou de um resultado direto, funcionando de forma similar a uma chamada de função remota[cite: 37].

---

### Como Compilar e Executar

Este projeto é um pacote ROS 2 e deve ser compilado dentro de um workspace.

**1. Preparar o Workspace**

Se você ainda não tem, crie um workspace e crie um link simbólico do pacote para a pasta `src`, permitindo que o `colcon` o encontre.

```bash
# Crie um workspace
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws

# Crie um link simbólico do pacote para a pasta src
# (Assumindo que o repositório 'treinamento_edrom' está na sua Home)
ln -s ~/treinamento_edrom/projetos/ros2_calculator ./src
```

**2. Compilar o Pacote**

Na raiz do seu workspace, execute o `colcon` para compilar o pacote da calculadora.

```bash
cd ~/ros2_ws
colcon build --packages-select calculadora
```

**3. Executar os Nós**

Para o sistema funcionar, o servidor precisa estar ativo antes que o cliente faça uma requisição. Você precisará de dois terminais.

* **No Terminal 1 (Inicie o Servidor):**

    ```bash
    # Faça o source do ambiente do seu workspace
    source ~/ros2_ws/install/setup.bash

    # Execute o nó servidor
    ros2 run calculadora calculator_server
    ```
    
    <img width="924" height="286" alt="Screenshot from 2025-09-20 23-08-27" src="https://github.com/user-attachments/assets/1f09ae51-e4fb-4a0f-8809-b573fbf4ff6d" />

* **No Terminal 2 (Execute o Cliente):**

    ```bash
    # Faça o source do ambiente no novo terminal também
    source ~/ros2_ws/install/setup.bash

    # Execute o nó cliente, passando dois números como argumento
    ros2 run calculadora calculator_client 5 10
    ```
    
    <img width="924" height="286" alt="Screenshot from 2025-09-20 23-09-15" src="https://github.com/user-attachments/assets/9209e3ff-7268-4e54-ac06-3467db5801e0" />

---

### 👨‍💻 Autor

* **Giovanna Guedes Veloso** - [gihgveloso](https://github.com/gihgveloso)
