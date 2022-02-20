Atividade 3 - Backend

Você deve criar o backend para um sistema de monitoramento de alarmes residenciais.

Considere que cada alarme residencial possui uma central com acesso à Internet, e que vários sensores de presença posicionados em diferentes cômodos da residência estão conectados a essa central. Cada alarme residencial possui um identificador único que deve ser informado em todas as comunicações realizadas com o backend do sistema de monitoramento.

O backend do sistema de monitoramento deve atender várias residências. O backend será composto por cinco microservices, responsáveis pelas funcionalidades descritas a seguir:

    cadastro dos imóveis monitorados: mantém os dados de cada imóvel, como o endereço, nome do proprietário e seus dados de contato;
    acionamento do alarme: registra o horário em que um alarme é ativado ou desativado pelo proprietário;
    status do alarme: recebe uma requisição a cada 30 segundos da central de alarme para informar que ela está conectada à rede; todas as mensagens de status recebidas devem ser registradas no banco de dados; 
    monitoramento do imóvel: recebe da central a indicação de que um sensor detectou a presença de uma pessoa no imóvel; registra o horário e o sensor que foi acionado, e ativa o serviço de notificação de alarme;
    notificação de alarme: emite uma mensagem (basta imprimir na tela) informando que há um acesso suspeito ao imóvel; a mensagem deve apresentar os dados do imóvel e do proprietário, obtidos a partir do cadastro de imóveis, para que seja feito contato com o proprietário e, se necessário, um vigilante se dirija ao local.

Os microservices devem ser acessados por meio de um API gateway, que deve fornecer uma interface REST para acesso aos serviços. A interação do gateway com os microservices pode empregar qualquer tecnologia que você considere apropriada, como REST, AMQP, MQTT, Thrift, etc.

O API gateway e os microservices podem ser implementados utilizando o Node.js ou qualquer outra tecnologia que você conheça.  
Avaliação

A atividade deve ser desenvolvida individualmente.

A apresentação deve ser realizada na aula síncrona do dia 21/02, ou anteriormente a esta data nos horários de aula, mediante agendamento, ou no horário reservado pelo professor para atendimentos aos alunos.

Será verificado o funcionamento do backend por meio do envio de requisições partindo de um código de teste da API criado pelo aluno ou de uma ferramenta de teste de API como o Postman ou similares. Em seguida, o aluno deve responder oralmente a questões sobre o código-fonte do programa.

Obs.: Em caso de cópia de código / plágio, todos os envolvidos terão nota igual a zero.
