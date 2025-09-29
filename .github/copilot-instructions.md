# Copilot Instructions for AI Coding Agents

## Visão Geral do Projeto
- Este repositório é um conjunto de exercícios e projetos de Programação Orientada a Objetos (POO), organizado em blocos temáticos (ex: BLOCO_A, BLOCO_B).
- Cada exercício está em uma subpasta dentro de `poo/database/`, com um diretório para cada tema (ex: `carro`, `toalha`).
- Cada tema possui um `Readme.md` detalhando requisitos, regras de negócio e exemplos.

## Estrutura e Convenções
- Os códigos-fonte ficam em subpastas `py/` dentro de cada tema (ex: `poo/database/toalha/py/draft.py`).
- Siga as instruções e exemplos dos arquivos `Readme.md` de cada tema para implementar as classes e métodos.
- Use nomes de classes e métodos exatamente como especificado nos enunciados para garantir compatibilidade com testes automáticos.
- Testes devem ser criados no mesmo diretório do código, preferencialmente em arquivos separados ou no próprio `draft.py`.

## Fluxos de Trabalho Importantes
- **Inicialização do ambiente:**
  - Utilize o script e comandos do `Readme.md` raiz para instalar dependências e configurar o ambiente (ex: `pipx install tko`).
  - O comando `tko run <arquivo_codigo>` executa o código com a interface padrão; `tko gui <arquivo_codigo>` usa interface curses.
- **Estrutura de pastas:**
  - `poo/Readme.md` traz visão geral das atividades e links para materiais de apoio.
  - Cada subdiretório em `poo/database/` representa um exercício independente.
- **Comandos úteis:**
  - `tko init --remote poo --folder poo --lang py --filter BLOCO_A BLOCO_B` para inicializar o repositório local.
  - `tko open poo` para abrir o repositório.
  - `pipx upgrade tko` para atualizar a ferramenta.

## Padrões Específicos
- Métodos de entrada e saída devem seguir o formato dos exemplos dos enunciados.
- Mensagens de erro e retorno devem ser idênticas às especificadas (ex: `fail: limite de pessoas atingido`).
- Para exercícios como "Toalha" e "Carro", siga o diagrama e exemplos de código dos respectivos `Readme.md`.

## Integrações e Dependências
- O projeto depende da ferramenta `tko` para execução e testes.
- Não há integração com serviços externos além do ambiente local e do Codespaces.

## Exemplos de Arquivos-Chave
- `poo/database/toalha/Readme.md` — enunciado e exemplos para o exercício da Toalha.
- `poo/database/carro/Readme.md` — enunciado e exemplos para o exercício do Carro.
- `poo/Readme.md` — visão geral e links para materiais de apoio.
- `Readme.md` (raiz) — instruções de configuração do ambiente e comandos principais.

## Recomendações para Agentes
- Sempre leia o `Readme.md` do exercício antes de implementar.
- Priorize clareza, aderência ao enunciado e compatibilidade com os comandos e ferramentas descritos.
- Não altere a estrutura de pastas ou nomes de arquivos sem necessidade explícita.
- Documente decisões não triviais diretamente no código ou em comentários.
