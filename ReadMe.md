# Princípios SOLID em Python

Este repositório foi feito para a disciplina de engenharia de software (BCC3004) da Universidade Tecnologica federal do paraná (UTFPR) e tem como objetivo
apresentar alguns principios SOLID em uma linguagem de programação escolhida (python neste caso), sendo assim foram escolhidos os principios:

Single responsability Principle:

O Princípio da Responsabilidade Única (SRP) é um dos pilares do SOLID na engenharia de software. Ele enfatiza que cada classe ou módulo deve ter apenas uma
responsabilidade ou motivo para mudar. Isso significa que uma classe deve ser especializada em realizar apenas uma tarefa específica e não deve ser sobrecarregada com
funcionalidades não relacionadas. Ao seguir o SRP, promove-se um design mais modular e coeso, onde cada componente do sistema é claro e focado. Isso resulta em código
mais legível, escalável e menos propenso a erros, facilitando a manutenção e a evolução do software ao longo do tempo.

Open closed Principle:

O Princípio Aberto/Fechado (OCP) diz que as entidades de software (como classes, módulos ou funções) devem estar abertas para extensão, mas fechadas para
modificação. Em outras palavras, o comportamento de uma entidade deve ser estendido sem alterar seu código-fonte original. Isso é alcançado através da utilização de
abstrações e interfaces, permitindo que novos comportamentos sejam adicionados através de subclasses, implementações alternativas ou componentes adicionais, sem
necessidade de alterações nos componentes existentes. O OCP promove um design flexível e adaptável, que pode evoluir com os requisitos do sistema sem introduzir
riscos desnecessários de quebra de funcionalidades já existentes. Isso resulta em um código mais estável, modular e de fácil manutenção, que pode ser estendido e
adaptado de forma eficiente ao longo do tempo. 

Liskov substituition Principle:

O Princípio da Substituição de Liskov (LSP) formulado por Barbara Liskov enfatiza que os objetos de uma classe base devem ser substituíveis por instâncias de suas
subclasses sem afetar a corretude do programa. Ou seja, uma subclasse deve ser capaz de substituir sua classe base sem alterar o comportamento esperado do programa.
Para cumprir o LSP, as subclasses devem respeitar o contrato estabelecido pela classe base, mantendo as precondições, pós-condições e invariáveis do sistema. Isso
implica que as subclasses devem estender o comportamento da classe base sem alterar suas características fundamentais. Quando o LSP é seguido, o código se torna mais
flexível e escalável, permitindo que novas funcionalidades sejam adicionadas através de subclasses sem introduzir erros ou comportamentos inesperados.

Principio de Demeter:

O Princípio de Demeter, também conhecido como "Lei do Demeter", é um princípio de design de software que enfatiza a minimização do conhecimento entre os componentes
de um sistema. Sendo assim uma classe deve ter conhecimento limitado sobre outras classes, mantendo interações diretas apenas com seus amigos imediatos. Seguir o
Princípio de Demeter ajuda a reduzir o acoplamento entre os componentes do sistema, o que resulta em um design mais flexível e fácil de manter. Isso é alcançado
através da restrição das interações de uma classe para apenas seus membros imediatos, evitando cadeias de chamadas profundas e o acesso direto a componentes internos
de objetos relacionados.

## Exemplos

SRP:

