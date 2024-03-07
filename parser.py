from bs4 import BeautifulSoup

html_string = open("C:\\xampp\\htdocs\\bcc3\\dadosAluno\\index.html", "r")
site = BeautifulSoup(html_string, "html.parser")

notas = site.findAll(class_="nota")

disciplinas = site.findAll(class_="nome")

faltas = site.findAll(class_="faltas")

profs = site.findAll(class_="prof")

soma = 0

cont_profs = {}

cont_faltas = {}

for i in range(10):
    soma += float(notas[i].text)

    cont_profs[i] = 0

    for j in range(10):
        if profs[i].text == profs[j].text:
            cont_profs[i] += 1

    if i == 0:
        maisFaltas = i
    elif int(faltas[maisFaltas].text) < int(faltas[i].text):
        maisFaltas = i

    if profs[i].text in cont_faltas:
        cont_faltas[profs[i].text] += int(faltas[i].text)
    else:
        cont_faltas[profs[i].text] = int(faltas[i].text)

media = soma / 10

for i in range(10):
    if i == 0:
        maisDisc = i
    elif cont_profs[maisDisc] < cont_profs[i]:
        maisDisc = i

ordem = sorted(cont_faltas.items(), key = lambda x:x[1], reverse = False)

print("Media do aluno:", media)
print("\nDisciplina com mais faltas:", disciplinas[maisFaltas].text, "(", faltas[maisFaltas].text, "faltas )")
print("\nProfessor com mais disciplinas:", profs[maisDisc].text, "(", cont_profs[maisDisc], "disciplinas )")
print("\nProfessores organizados em ordem crescente pela quantidade de faltas do aluno:")
for elemento in ordem:
    print(elemento[0], "-", elemento[1], "faltas")