# Projeto Chatter - Publisher/Subscriber em ROS 2

Este projeto é uma implementação básica do sistema de comunicação Publisher/Subscriber usando ROS 2. Ele foi desenvolvido como parte de um treinamento para demonstrar os conceitos fundamentais de criação de pacotes, nós, tópicos e mensagens em ROS 2.

---

## Sobre a Atividade:

O sistema consiste em dois nós principais:

* **`talker` (Publicador):** Um nó que publica continuamente uma mensagem de texto no tópico `/chatter`. A mensagem contém um contador que incrementa a cada envio.
* **`listener` (Assinante):** Um nó que se inscreve no tópico `/chatter`, recebe as mensagens enviadas pelo `talker` e as imprime no console.

---

## Instalação e Compilação

Siga os passos abaixo para compilar o projeto.

1.  Clone este repositório em um workspace do ROS 2:
    ```bash
    mkdir -p ~/ros2_ws/src
    cd ~/ros2_ws/src
    git clone [https://github.com/gihgveloso/ros2_chatter.git](https://github.com/gihgveloso/ros2_chatter.git)
    ```
    
2.  Volte para a raiz do workspace e compile o pacote:
    ```bash
    cd ~/ros2_ws
    colcon build --packages-select chatter
    ```

---

## Execução

Para executar os nós, você precisará de dois terminais.

1.  Em cada terminal, navegue até a raiz do seu workspace e execute o comando `source` para carregar o ambiente:
    ```bash
    cd ~/ros2_ws
    source install/setup.bash
    ```
2.  No primeiro terminal, inicie o nó `talker`:
    ```bash
    ros2 run chatter talker
    ```
    *Você verá mensagens de "Publicando..." aparecerem.*
    <img width="843" height="525" alt="Screenshot from 2025-09-20 17-32-18" src="https://github.com/user-attachments/assets/d17c17d3-b87b-4e30-a06d-886a1aa11ae3" />

4.  No segundo terminal, inicie o nó `listener`:
    ```bash
    ros2 run chatter listener
    ```
    *Você verá as mensagens de "Eu ouvi..." correspondentes às que o talker está enviando.*
    <img width="850" height="655" alt="Screenshot from 2025-09-20 17-32-56" src="https://github.com/user-attachments/assets/5fd38403-23e5-4985-8760-ade355469454" />

---
