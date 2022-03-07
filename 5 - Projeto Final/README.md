# Projeto Final

O projeto final irá reunir os conceitos de backend, aplicativos móveis e sistemas embarcados, vistos ao longo da disciplina.

# Descrição
O projeto final deve ser composto de:

- Sistema embarcado: deve possuir pelo menos um sensor, que medirá alguma grandeza física, e um atuador, que executará alguma ação tendo com base a leitura do sensor; os parâmetros de configuração do sistema (ex.: a temperatura a partir da qual é acionado um relé, a luminosidade mínima necessária para acionar um LED, a distância a partir da qual é acionado um alarme, etc.) devem ser lidos a partir do backend. 
- Backend: composto por microservices que serão acessados por meio de um API Gateway; usado pelo sistema embarcado para registrar os dados lidos pelo sensor e para registrar os comandos enviados ao atuador; acessado também pelo aplicativo para configurar os parâmetros de funcionamento do sistema embarcado e para obter o histórico de leituras dos sensores.
- Aplicativo móvel: deve permitir a configuração dos parâmetros de funcionamento do sistema embarcado enviando-os para o backend, ler os dados dos sensores publicados pelo sistema no backend e exibi-los na tela do celular.

Poderão ser usadas as tecnologias vistas em aula ou apresentadas nos seminários da disciplina. Não será permitido usar serviços de backend prontos, como o Firebase e similares - ou seja, você deve construir seu próprio backend. Os dados recebidos pelo backend podem ser mantidos em um banco de dados de sua preferência.

### Observações:

O sistema embarcado pode ser o mesmo da Atividade 2, com o código adaptado de forma a interagir com o backend pela rede. 
Caso seja usado o TinkerCad para simular o funcionamento do sistema embarcado, ou caso sua placa não possua suporte a rede, não será possível realizar a comunicação pela rede com o backend. Nesse caso, as chamadas para o backend devem ser testadas usando o Postman ou similares. 
O emulador do Expo (assim como outros emuladores) também não conseguirá fazer a comunicação pela rede com o backend. Para que a comunicação pela rede seja possível você deve rodar o aplicativo no seu celular. 
Para evitar problemas na comunicação, conecte o celular, o sistema embarcado e o computador que rodará o backend à mesma rede local.
Ao interagir com o backend, substitua 'localhost' na URL pelo endereço IP do computador onde o backend está sendo executado. Para descobrir o endereço IP do computador, execute o comando ifconfig (LInux e MacOS) ou ipconfig (Windows). 

# Apresentação

O projeto deve ser desenvolvido individualmente.

A apresentação deve ser realizada até o dia 21/03 durante o horário de aula, ou no horário reservado pelo professor para atendimento aos alunos. Como esta é a última avaliação do semestre, não serão tolerados atrasos. Os alunos que não apresentarem o projeto dentro do prazo ficarão com nota zero nessa avaliação.

Será verificado o funcionamento do programa e, em seguida, o aluno deve responder oralmente a questões sobre o código-fonte do programa. Caso o  aluno demonstre não conhecer o código do programa, este ficará com nota zero no trabalho.
