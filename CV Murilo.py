import datetime
import calendar


def mk_str(var):
    return ' '.join(var)


date = datetime.date.today()
year = date.strftime("%Y")

var_name = ('Murilo', 'Betoni', 'de', 'Freitas')

age, local = 20, "São Bernardo do Campo - SP, Brazil"

contact = ["(11) 97157-6609", "murilo.betoni@gmail.com", "www.linkedin.com/in/murilobfreitas"]
phone, email, linkedin = contact

objective = "Estágio - Desenvolvedor"

academic_education = {'semestre':6, 'curso':'Sistemas de Informação', 'faculdade':'Universidade Metodista de São Paulo', 'conclusao':'12/2022'}

professional_xp = {'cargo':'Assistente Administrativo', 'empresa':'4 Show Comércio de Eletrônicos', 'admissao':f'{calendar.month_abbr[12]}/{int(year) - 1}', 'demissao':f'{calendar.month_abbr[7]}/{year}', 'atv':'Testes de funcionalidades para celulares, limpeza de eletrônicos e trabalhos manuais de carga e descarga'}

knowledges = ['Python', 'Java', 'HTML', 'CSS', 'Javascript', 'Git', 'Oracle SQL', 'Office', 'Medologias Ágeis']

negrito = '\033[;1m'
limpa = '\033[m'


print(f"{negrito}{mk_str(var_name)}{limpa} \n{age} anos, {local} \n")

print(f"{phone} \n{email} \n{linkedin} \n")

print(f"{negrito}Objetivo{limpa} \n{objective} \n")

print(f"{negrito}Formação{limpa} \nCursando {academic_education['semestre']}º semestre de {academic_education['curso']} \n{academic_education['faculdade']} \nConclusão em {academic_education['conclusao']} \n")

print(f"{negrito}Experiência Profissional{limpa} \n{professional_xp['cargo']} \n{professional_xp['empresa']} \n{professional_xp['admissao']} - {professional_xp['demissao']} \n\nAtividades realizadas: \n{professional_xp['atv']} \n")

print(f"{negrito}Conhecimentos{limpa}")
for x in knowledges:
    print(f"- {x}")
