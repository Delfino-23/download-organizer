# Organizador de Downloads

Pequeno utilitário Python para organizar arquivos de download (script principal: `app.py`).

## Descrição

Este projeto contém um script que organiza arquivos em uma pasta (por exemplo, a pasta de Downloads). Há também arquivos gerados por empacotamento com PyInstaller no repositório (`DownloadOrganizer.spec` e a pasta `build/`).

## Requisitos

- Python 3.8 ou superior

> Observação: este repositório não possui atualmente um `requirements.txt`. Se o seu `app.py` depender de pacotes externos, adicione-os em um `requirements.txt` e instale com `pip`.

## Instalação

1. Clone este repositório ou copie os arquivos para sua máquina.
2. (Opcional) Crie um ambiente virtual e ative-o:

```
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

3. Instale dependências (se houver):

```
pip install -r requirements.txt
```

## Uso

Execute o script diretamente com Python:

```
python app.py
```

O comportamento exato depende de como `app.py` está implementado (por exemplo, quais pastas ele organiza ou quais opções de linha de comando aceita).

## Empacotamento (PyInstaller)

Este repositório já contém um arquivo de especificação `DownloadOrganizer.spec` e uma pasta `build/` gerada por PyInstaller. Para recriar o executável, execute:

```
pyinstaller DownloadOrganizer.spec
```

Após o build, verifique as pastas `dist/` ou `build/` para encontrar o executável gerado.

## Estrutura relevante

- `app.py` — script principal
- `DownloadOrganizer.spec` — especificação do PyInstaller (se aplicável)
- `build/` — pasta gerada pelo PyInstaller (artefatos de build)

## Contribuição

Pull requests são bem-vindos. Para contribuir, abra uma issue com o que pretende alterar e envie um PR pequeno e focado.

## Licença

Nenhuma licença foi especificada. Adicione um arquivo `LICENSE` se desejar publicar com termos claros.
