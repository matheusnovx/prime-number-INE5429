# Gerador de Números Primos

Este projeto é um gerador de números primos baseado em Python, utilizando o Gerador Congruente Linear (LCG) e o gerador de números aleatórios de Park-Miller. Inclui implementações dos testes de primalidade de Fermat e Miller-Rabin para verificar os números gerados.

### Estrutura do Projeto

- `pseudo_aleatorio/LinearCongruentialGenerator.py`: Contém a implementação do Gerador Congruente Linear.
- `pseudo_aleatorio/ParkMiller.py`: Contém a implementação do gerador de números aleatórios de Park-Miller.
- `pseudo_aleatorio/main.py`: Script para medir o tempo de execução da geração de números aleatórios usando diferentes comprimentos de bits.
- `primalidade/Fermat.py`: Contém a implementação do teste de primalidade de Fermat.
- `primalidade/MillerRabin.py`: Contém a implementação do teste de primalidade de Miller-Rabin.
- `primalidade/main.py`: Script principal para gerar números primos e medir o tempo de execução usando diferentes comprimentos de bits e testes de primalidade.

### Requisitos

- Python 3.x


## Gerando Números Primos

Para gerar números primos usando os testes de primalidade de Fermat ou Miller-Rabin, execute o script primalidade/main.py. Você pode descomentar o método de teste desejado no script.

```bash
python primalidade/main.py
```


## Geração de Números Primos

Para a geração de números aleatórios usando LCG ou Park-Miller, execute o script pseudo_aleatorio/main.py. Você pode descomentar o gerador desejado no script.

```bash
python pseudo_aleatorio/main.py
```
