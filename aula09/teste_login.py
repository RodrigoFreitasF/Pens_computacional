from util.db import SQL
#invadir isso aqui

cpf = input('Digite o CPF: ')
senha = input('Digite o Senha: ')


cmd = f'''
SELECT nme_colaborador, sts_colaborador FROM tb_colaborador WHERE cpf_colaborador = "{cpf}" 
AND pwd_colaborador = SHA("{senha}")
'''


sql = SQL(esquema='bd_planejamento')


colaborador = sql.get_object(cmd)


if colaborador is None:
   print('Falha no Login')
else:
   print('Bem vindo ao sistema')
   print(colaborador['nme_colaborador'])
   print('Função:', ('Administrador' if colaborador['sts_colaborador'] == 'A' else 'Usuário Comum'))