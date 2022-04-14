nome = input('Informe seu nome: ')--
idade =int(input('Olá {}, agora informe sua idade: '.format(nome)))
tempo= int(input('Informe o seu tempo de serviço: '))

if (tempo >= 30):
    print("Você pode se aposentar")
elif (tempo < 30):
    print("Você não pode se aposentar")
 
if (idade >= 65):
    print("Você poderá se aposentar devido a idade!")
elif (idade < 65):
    print("Você não pode se aposentar somente por idade")

if (tempo >= 30):
    print("Tempo de carteira assinada OK, portanto pode se aposentar")
elif (tempo < 30):
    print("Sem tempo de carteira assinada sulficiente, portanto não pode se aposentar")

if (idade >= 65):
    print("Parabéns, você poderá se aposentar devido a idade!")
elif (idade < 65):
    print("Você não pode se aposentar somente por idade")
  