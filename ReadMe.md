# Princípios SOLID em Python

Este repositório foi feito para a disciplina de Engenharia de Software (BCC3004) da Universidade Tecnologica Federal do Paraná (UTFPR) e tem como objetivo
apresentar alguns principios SOLID em uma linguagem de programação escolhida (python neste caso), sendo assim foram escolhidos os principios:

Single Responsability Principle:

O Princípio da Responsabilidade Única (SRP) é um dos pilares do SOLID na engenharia de software. Ele enfatiza que cada classe ou módulo deve ter apenas uma
responsabilidade ou motivo para mudar. Isso significa que uma classe deve ser especializada em realizar apenas uma tarefa específica e não deve ser sobrecarregada com
funcionalidades não relacionadas. Ao seguir o SRP, promove-se um design mais modular e coeso, onde cada componente do sistema é claro e focado. Isso resulta em código
mais legível, escalável e menos propenso a erros, facilitando a manutenção e a evolução do software ao longo do tempo.

Open Closed Principle:

O Princípio Aberto/Fechado (OCP) diz que as entidades de software (como classes, módulos ou funções) devem estar abertas para extensão, mas fechadas para
modificação. Em outras palavras, o comportamento de uma entidade deve ser estendido sem alterar seu código-fonte original. Isso é alcançado através da utilização de
abstrações e interfaces, permitindo que novos comportamentos sejam adicionados através de subclasses, implementações alternativas ou componentes adicionais, sem
necessidade de alterações nos componentes existentes. O OCP promove um design flexível e adaptável, que pode evoluir com os requisitos do sistema sem introduzir
riscos desnecessários de quebra de funcionalidades já existentes. Isso resulta em um código mais estável, modular e de fácil manutenção, que pode ser estendido e
adaptado de forma eficiente ao longo do tempo. 

Liskov Substituition Principle:

O Princípio da Substituição de Liskov (LSP) formulado por Barbara Liskov enfatiza que os objetos de uma classe base devem ser substituíveis por instâncias de suas
subclasses sem afetar a corretude do programa. Ou seja, uma subclasse deve ser capaz de substituir sua classe base sem alterar o comportamento esperado do programa.
Para cumprir o LSP, as subclasses devem respeitar o contrato estabelecido pela classe base, mantendo as precondições, pós-condições e invariáveis do sistema. Isso
implica que as subclasses devem estender o comportamento da classe base sem alterar suas características fundamentais. Quando o LSP é seguido, o código se torna mais
flexível e escalável, permitindo que novas funcionalidades sejam adicionadas através de subclasses sem introduzir erros ou comportamentos inesperados.

Principio de Demeter:

O Princípio de Demeter, também conhecido como "Lei de Demeter", é um princípio de design de software que enfatiza a minimização do conhecimento entre os componentes
de um sistema. Sendo assim uma classe deve ter conhecimento limitado sobre outras classes, mantendo interações diretas apenas com seus amigos imediatos. Seguir o
Princípio de Demeter ajuda a reduzir o acoplamento entre os componentes do sistema, o que resulta em um design mais flexível e fácil de manter. Isso é alcançado
através da restrição das interações de uma classe para apenas seus membros imediatos, evitando cadeias de chamadas profundas e o acesso direto a componentes internos
de objetos relacionados.

## Exemplos

Para todos os exemplos temos uma versão que viola o principio em questão "wrong.py" e a versão corrigida "correct.py" 

SRP: No exemplo incorreto temos uma classe "IceCream" que possui múltiplas funções e funcionalidades, isto fere diretamente a SRP em primeiro motivo porque a class
IceCream possui funcionalidades como gerenciar pedidos e calcular preços além de enviar notificações, em segundo lugar temos a função "request_and_calculate" price
que também fere diretamente o principio de responsabilidade unica ao executar duas funções: calcular o preço e gerenciar pedidos. 
Para transformar este código em um que respeite a SRP devemos efetuar as seguintes mudanças como vistas no codigo corrigido : separar a class IceCream para lidar
apenas com o que lhe convém (neste caso ela apenas gerencia o sorvete e pode devolver os valores de um sorvete), criando assim outra class para gerenciar apenas os
preços e separando também funções como enviar notificação e gerenciar os pedidos "get_user_selection", agora cada class cuida apenas de uma funcionalidade, assim como
as funções, logo agora este código respeita o principio de responsabilidade única.

OCP: Considerando o codigo incorreto, temos uma classe que gerencia deliverys de vários tipos de comida, porem perceba que para adicionar um tipo de comida nova
teríamos que fazer além do que adicionar uma nova classe, também teríamos que modificar o método DeliveryManager adicionando nossa nova comida aos ifs, o que fere o
principio de aberto e fechado, pois esta entidade não está fechada para modificação.
Para corrigir isto, criamos uma abstração agora chamada "comida", sendo assim cada class nova adicionada é um tipo de comida e para o método DeliveryManager agora
recebe um dicionario com as comidas disponíveis, logo para adicionar um tipo novo de comida não precisaremos modificar o método de delivery, apenas podemos atualizar
o dicionario existente e criar a nova classe com a comida que quisermos adicionar. Sendo assim o codigo agora esta aberto para extensão mas fechado para modificação.

LSP: Para exemplificar o principio de substituição de Liskov podemos começar pelo código errado onde, temos uma classe espada (sword) e outras classes que herdam de
sword como Katana e Shieldedblade o problema é que Liskov diz que uma subclasse deve poder substituir a classe pai ou classe mais alta sem problemas, e isto não
acontece neste código por 2 motivos principais, sendo 1 deles o fato de que a classe katana possui uma condição de ataque que difere da classe alta onde se não houver
energia o suficiente ela não ataca, isto fere o principio de liskov pois a função de ataque da katana não substitui bem a função de ataque original, outro problema é
que na classe Shieldedblade esta possui uma função de defesa o que não é o problema em si, porem esta função de defesa esta substituindo o ataque da original o que
fere completamente o LSP pois não poderíamos também utilizar a class shieldedblade e suas funções para substituir uma sword.
Um meio de transformar este código em um que respeita o LSP pode ser visto no correção, onde por mais que a class katana e nodachi possuam tipos de ataques
diferentes, sua funcionalidade base ainda é preservada, as duas atacam assim como a classe original, logo uma classe sword pode ser substituída pela classe katana ou
nodachi sem erros, atendendo assim a LSP.

Demeter: Como exemplo da lei de demeter temos a versão errada onde há uma classe de um rio e outra de um pescador, um pescador só pode pescar em um rio se sua água
for limpa e para isto devemos verificar tal condição para isto considere esta parte do código : 
```
def fishing(self):
if self.river.water == "clean": # Directly accessing the water attribute of the River instance
while self.baits > 0:
self.get_fish()
self.baits -= 1
```
perceba que ao verificar se a água esta limpa estamos basicamente fazendo fisher.river.water o que fere a lei de demeter pois um pescador (fisher) não deve ter acesso
a classe rio diretamente, pois ele acaba obtendo as informações da classe rio, para isto no código corrigido utilizamos uma nova função implementada na classe rio que
verifica se a água está limpa e ao invés de acessarmos o rio diretamente para verificar a água, utilizamos este novo método como podemos ver:
```
def fishing(self, river):
if river.is_clean(): # Using a method of River class instead of directly accessing attributes
while self.baits > 0:
self.get_fish()
self.baits -= 1
```
agora o acesso não é mais direto e a classe pescador não acessa mais os dados da classe rio, respeitando assim a lei de demeter.
