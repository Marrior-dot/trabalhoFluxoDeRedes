class Vertice:
    def __init__(self, content):
        self.content = content
        self.cor = ""
        self.antecessor = None
    
    def get_content(self):
        return self.content
    
    def get_cor(self):
        return self.cor
    
    def set_cor(self, nova_cor: int):
        self.cor = nova_cor
    
    def get_antecessor(self):
        return self.antecessor
    
    def set_antecessor(self, novo_antecessor):
        self.antecessor = novo_antecessor
        
class Aresta:
    def __init__(self,ce,fe,u: Vertice,v: Vertice):
        self.fe = fe
        self.ce = ce 
        self.u = u
        self.v = v
        self.aresta_direta = None
    
    def get_fluxo(self):
        return self.fe
    
    def set_fluxo(self, novo_fe):
        self.fe = novo_fe
    
    def get_capacidade(self):
        return self.ce
    
    def set_capacidade(self, nova_capacidade):
        self.capacidade = nova_capacidade
    
    def get_vertice_u(self):
        return self.u
    
    def set_vertice_u(self, novo_vertice_u: Vertice):
        self.u = novo_vertice_u
    
    def get_vertice_v(self):
        return self.v

    def set_vertice_v(self, novo_vertice_v: Vertice):
        self.v = novo_vertice_v
        
    def get_aresta_direta(self):
        return self.aresta_direta
    
    def set_aresta_direta(self, direta: bool):
        self.aresta_direta = direta

class Rede:
    def __init__(self,vertices: list[Vertice],arestas: list[Aresta]):
        self.vertices = vertices
        self.arestas = arestas
        self.s = self.vertices[0]
        self.t = self.vertices[len(vertices) - 1]
        self.F = 0
        
        self.fe0
    
    def get_vertices(self):
        return self.vertices
    
    def get_arestas(self):
        return self.arestas
    
    def get_fluxo_rede(self):
        return self.F
    
    def set_fluxo(self, novo_fluxo):
        self.F = novo_fluxo
    
    def add_fluxo(self, fluxo):
        self.F += fluxo
    
    def add_aresta(self, ce, fe, u: Vertice, v: Vertice):
        arestas = self.get_arestas()
        nova_aresta = Aresta(ce, fe, u, v)
        arestas.append(nova_aresta)
        
        return nova_aresta
    
    def fe0(self):
        for aresta in self.arestas:
            aresta.set_fluxo(0)
    
    def adj(self, vertice: Vertice):
        adjs = []
        for aresta in self.arestas:
            if vertice == aresta.get_vertice_u():
                adjs.append(aresta)
            elif vertice == aresta.get_vertice_v():
                adjs.append(aresta)
           
        return adjs
    
    def bfs(self, vertice_inicial: Vertice):
        for vertice in self.get_vertices():
            vertice.set_cor(0)
            vertice.set_antecessor(None)
            
        
        fila = [vertice_inicial]
        
        while len(fila) > 0:
            vertice_atual = fila.pop(0)
            for adjacencia in self.adj(vertice_atual):
                if(adjacencia.get_vertice_v().get_cor() == 0):
                    adjacencia.get_vertice_v().set_cor(1)
                    adjacencia.get_vertice_v().set_antecessor(adjacencia.get_vertice_u())
                    fila.append(adjacencia.get_vertice_v())
                
            vertice_inicial.set_cor(2)
        
        if self.get_vertices()[-1].get_antecessor():
            return True
        return False
    
    def diferenciar_arestas(self):
        for aresta in self.arestas:
            if aresta.get_capacidade() - aresta.get_fluxo() > 0:
                aresta.set_aresta_direta(True)
            else:
                aresta.set_aresta_direta(False)
                
    def resetar_arestas_diretas(self):
        for aresta in self.get_arestas():
            aresta.set_aresta_direta(None)
            
    def definir_fluxo_rede(self):
        for aresta in self.adj(self.get_vertices()[0]):
            self.add_fluxo(aresta.get_fluxo())
            
class RedeResidual(Rede):
       
    def __init__(self, rede: Rede):
        self.caminho_aumentante = []
        self.capacidade_minima = 9223372036854775807    # max_int
        super().__init__(rede.get_vertices(), [])
        
        for aresta in rede.get_arestas():
            if aresta.get_aresta_direta():
                self.add_aresta(aresta.get_capacidade() - aresta.get_fluxo(), 0, aresta.get_vertice_u(), aresta.get_vertice_v()).set_aresta_direta(True)
            else:
                self.add_aresta(aresta.get_fluxo(), 0, aresta.get_vertice_v(), aresta.get_vertice_u()).set_aresta_direta(False)
        
    # def diferenciar_arestas(self):
    #     for aresta in self.arestas:
    #         if aresta.get_capacidade() - aresta.get_fluxo() > 0:
    #             aresta.set_capacidade(aresta.get_capacidade() + (aresta.get_capacidade() - aresta.set_fluxo()))
    #             aresta.set_aresta_direta(True)
    #         else:
    #             verticev = aresta.get_vertice_v()
    #             verticeu = aresta.get_vertice_u()
    #             aresta.set_vertice_u(verticev)
    #             aresta.set_vertice_v (verticeu)
    #             aresta.set_capacidade(aresta.get_fluxo)
    #             aresta.set_aresta_direta(False)
    
    def get_caminho_aumentante(self):
        return self.caminho_aumentante
    
    # def set_fluxo_rede(self, a: Aresta):
    #     self.F = a.get_capacidade()
        
    def set_caminho_aumentante(self, caminho_aumentante: list):
        self.caminho_aumentante = caminho_aumentante
     
    def get_arestas_rede_residual(self):
        return self.arestas
    
    def get_capacidade_minima(self):
        return self.capacidade_minima
    
    def set_capacidade_minima(self, capacidade_minima):
        self.capacidade_minima = capacidade_minima
    
    def encontrar_caminho_aumentante(self):
        vertice_final = self.get_vertices()[-1]
        caminho_aumentante = self.get_caminho_aumentante()
        
        v2 = vertice_final
        v1 = vertice_final.get_antecessor()
        
        print(v1.get_content())
        print(v2.get_content())
        print(v2.get_antecessor().get_content())
        
        while v1:
            for aresta in self.get_arestas():
                if aresta.get_vertice_u() == v1 and aresta.get_vertice_v() == v2:
                    if aresta.get_capacidade() < self.get_capacidade_minima():
                        self.set_capacidade_minima(aresta.get_capacidade())
                    caminho_aumentante.insert(0, aresta)
                    # print(caminho_aumentante)
            # print(v1.get_content())
            # print(v2.get_content())
            
            v2 = v1
            v1 = v2.get_antecessor()
            
        if v1 == self.get_vertices()[0]:
            return True
            
        return False
    
    def resetar_vertices_bfs(self):
        for vertice in self.get_vertices():
            vertice.set_cor(0)
            vertice.set_antecessor(None)
    
    
vertice_s = Vertice("s")
vertice_1 = Vertice("V1")
vertice_2 = Vertice("V2")
vertice_3 = Vertice("V3")
vertice_4 = Vertice("V4") 
vertice_t = Vertice("t") 

# aresta1 = Aresta(3,2,vertice1,vertice2)
# aresta2 = Aresta(5,3,vertice2,vertice3)
# aresta3 = Aresta(2,1,vertice3,vertice4)
# aresta4 = Aresta(2,2,vertice4, vertice1)
# aresta4 = Aresta(2, 2, vertice1, vertice4)

aresta1 = Aresta(4,0,vertice_s,vertice_2)
aresta2 = Aresta(2,0,vertice_s,vertice_3)
aresta3 = Aresta(3,0,vertice_s,vertice_1)
aresta4 = Aresta(3,0,vertice_1,vertice_3)
aresta5 = Aresta(2,0,vertice_2,vertice_3)
aresta6 = Aresta(3,0,vertice_2,vertice_t)
aresta7 = Aresta(1,0,vertice_3,vertice_2)
aresta8 = Aresta(4,0,vertice_3,vertice_4)
aresta8 = Aresta(4,0,vertice_3,vertice_4)
aresta9 = Aresta(3,0,vertice_4,vertice_1)
aresta10 = Aresta(5,0,vertice_4,vertice_t)



rede = Rede([vertice_s, vertice_1, vertice_2, vertice_3, vertice_4, vertice_t],[aresta1,aresta2,aresta3,aresta4,aresta5,aresta6,aresta7,aresta8,aresta9,aresta10])
rede.diferenciar_arestas()
rede_residual = RedeResidual(rede)    

for aresta in rede_residual.get_arestas():
    print(aresta.get_vertice_u().get_content(), aresta.get_vertice_v().get_content())
    
conditio_while = rede_residual.bfs(rede_residual.get_vertices()[0])

for vertice in rede_residual.get_vertices():
    if vertice.get_antecessor():
        print(f"{vertice.content}[antecessor] = {vertice.get_antecessor().get_content()}")

while conditio_while == True:
    print("loop")
    rede_residual.encontrar_caminho_aumentante()
    # print(rede_residual.get_caminho_aumentante())
    for aresta_au in rede_residual.get_caminho_aumentante():
        for aresta in rede.get_arestas():
            if aresta_au.get_aresta_direta() == True and aresta_au.get_vertice_u() == aresta.get_vertice_u() and aresta_au.get_vertice_v() == aresta.get_vertice_v():
                aresta.set_fluxo(aresta.get_fluxo() + rede_residual.get_capacidade_minima())     
            elif aresta_au.get_aresta_direta() == False and aresta_au.get_vertice_u() == aresta.get_vertice_v() and aresta_au.get_vertice_v() == aresta.get_vertice_u():
                aresta.set_fluxo(aresta.get_fluxo() - rede_residual.get_capacidade_minima()) 
    rede.definir_fluxo_rede()
    
    print(rede.get_fluxo_rede())
    rede.resetar_arestas_diretas()
    rede.diferenciar_arestas()
    rede_residual = RedeResidual(rede)
    conditio_while = rede_residual.bfs(rede_residual.get_vertices()[0])
   