# Dungeon Matemática

Dungeon Matemática é um Sistema Tutor Inteligente de Matemática Básica para estudantes do 6º e 7º anos. A campanha usa fases de RPG para ensinar operações fundamentais, frações e porcentagens. O progresso na campanha e o domínio matemático são medidos separadamente.

## Executar localmente

Requer Python 3.11 ou superior. Os comandos funcionam no PowerShell e em shells Unix com Python disponível como `python`.

```powershell
python -m venv .venv
```

Ative o ambiente com `.\.venv\Scripts\Activate.ps1` no PowerShell ou `source .venv/bin/activate` em Linux e macOS. Em seguida, instale e execute:

```sh
python -m pip install -e .
python -m dungeon_matematica
python -m unittest discover -s tests -v
```

## Base inicial

- Catálogo com 15 conceitos, seus pré-requisitos propostos e os três módulos da campanha. O grafo aguarda validação curricular.
- Modelo do aluno com pontuação inicial zero, quatro dificuldades e domínio por conceito a partir de 70 pontos com acertos nos níveis médio e difícil.
- Regras de aprovação de fase comum e de chefão. O chefão exige cobertura de todos os conceitos do módulo, pelo menos 70% de acertos no total e 60% em cada conceito.
- Execução no terminal para visualizar o catálogo e testes automatizados para as regras iniciais.

A interface do jogo, o reconhecimento de manuscritos, o tutor, o combate e a persistência fazem parte das próximas entregas.
