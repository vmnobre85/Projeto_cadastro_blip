#language: pt
Funcionalidade: ''Eu como usuário quero acessar o site de cadastro gratuito da plataforma Blip''


Cenario: Cadastrar o usuario gratuitamente caso nao possua cadastro
Dado que acesso a pagina de cadastro
Quando preencho os dados solicitados 
E e os dados digitados nao coincidem com usuario cadastrado,clico na caixa de aceite dos termos e em cadastre-se gratis
Então apresentado cadastro realizado com sucesso
E se os dados coincidirem com usuario ja cadastrado o botao cadastre-se gratis nao e habilitado
