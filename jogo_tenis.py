from unittest import TestCase, main

def verifica_ganhador(jogos):
    pontos_a = 0
    pontos_b = 0

    equivalencia_pontos = {
        1 : 15,
        2 : 30,
        3 : 40,
        4 : 40
    }

    resultado_placar = {
        "pontos_jogador_a" : 0,
        "pontos_jogador_b" : 0,
        "resultado_jogo" : ""
    }

    for i in range(len(jogos["jogador_a"])):
        if(jogos["jogador_a"][i] == 1):
            pontos_a += 1
            resultado_placar["pontos_jogador_a"] = equivalencia_pontos[pontos_a]

        if jogos["jogador_b"][i] == 1:
            pontos_b += 1
            resultado_placar["pontos_jogador_b"] = equivalencia_pontos[pontos_b]

    if pontos_a == pontos_b:
        resultado_placar["resultado_jogo"] = "deuce"
        jogos_pos_empate = verifica_desempate(jogos["jogos_pos_empate"])
        resultado_placar["jogos_pos_empate"] = jogos_pos_empate

    if pontos_a > pontos_b:
        resultado_placar["resultado_jogo"] = "Jogador A"

    if pontos_a < pontos_b:
        resultado_placar["resultado_jogo"] = "Jogador B"

    return resultado_placar


def verifica_desempate(jogos):
    placar = {
        "A" : 0,
        "B" : 0
    }

    jogos_pos_empate = {}

    for i in jogos:
        if(jogos[i]["A"] > jogos[i]["B"]):
            placar["A"] += 1
            jogos_pos_empate[i] = "advantage Jogador A"

        if(jogos[i]["B"] > jogos[i]["A"]):
            placar["B"] += 1
            jogos_pos_empate[i] = "advantage Jogador B"

        if(placar["A"] == placar["B"]):
            placar["A"] = 0
            placar["B"] = 0
            jogos_pos_empate[i] = "deuce"

        if(placar["A"] == 2):
            jogos_pos_empate[i] = "vitoria Jogador A"
        if(placar["B"] == 2):
            jogos_pos_empate[i] = "vitoria Jogador B"

    return jogos_pos_empate



class teste_tenis(TestCase):
    def test_framework(self):
        self.assertTrue(True)


    def teste_vitoria_4jogos(self):
        jogos = {
            "jogador_a" : [0,0,0,0],
            "jogador_b" : [1,1,1,1]
        }

        esperado = {
            "pontos_jogador_a" : 0,
            "pontos_jogador_b" : 40,
            "resultado_jogo" : "Jogador B"
        }


        self.assertEqual(verifica_ganhador(jogos), esperado)

    def teste_empate(self):
        jogos ={
            "jogador_a" : [1,0,1,0,1,0],
            "jogador_b" : [0,1,0,1,0,1],
            "jogos_pos_empate" : {
                1 : {"A": 0, "B": 1},
                2 : {"A": 1, "B": 0},
                3 : {"A": 1, "B": 0},
                4 : {"A": 1, "B": 0},
            }
        }

        esperado = {
            "pontos_jogador_a" : 40,
            "pontos_jogador_b" : 40,
            "resultado_jogo" : "deuce",
            "jogos_pos_empate" : {
                1 :  "advantage Jogador B",
                2 :  "deuce",
                3 :  "advantage Jogador A",
                4 :  "vitoria Jogador A"
            }
        }

        self.assertEqual(verifica_ganhador(jogos), esperado)

    def teste_desempate(self):
        jogos = {
            1 : {"A": 0, "B": 1},
            2 : {"A": 1, "B": 0},
            3 : {"A": 1, "B": 0},
            4 : {"A": 1, "B": 0},
        }



        #self.assertEqual(verifica_desempate(jogos), esperado)
