# Projeto Figurinhas da Copa 2026

O sistema permite controlar dois álbuns: o seu álbum e o álbum de um amigo. Com isso, é possível testar a inserção de figurinhas, o armazenamento de repetidas e o sistema de trocas automáticas.

Principais funções do projeto:

- Adicionar figurinha ao álbum
- Remover figurinha do álbum
- Consultar figurinha pelo número
- Buscar figurinha por jogador
- Buscar figurinha por seleção
- Ver o álbum completo
- Ver figurinhas repetidas
- Mostrar a porcentagem concluída do álbum
- Registrar proposta de troca
- Efetuar troca automática
- Salvar e carregar álbum em JSON

## Como usar?

Para executar o projeto, deixe todos os arquivos na mesma pasta e rode:

```bash
python main.py
```

Depois disso, basta escolher uma opção no menu principal.

## Persistência

O projeto salva os dados em JSON. Se o usuário não informar um nome de arquivo, o sistema usa o nome padrão:

```bash
album.json
```

O arquivo salvo guarda as figurinhas do álbum, as repetidas e o total de figurinhas esperado para completar o álbum.
