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
    
    def get_fluxo(self):
        return self.F
    
    def set_fluxo(self, novo_fluxo):
        self.F = novo_fluxo
    
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
            '''
            for vertices in self.vertices:
                if(vertice == aresta.get_vertice_v and vertices == aresta.get_vertice_u):
                    adjs.append(aresta)
                elif(vertices == aresta.get_vertice_v and vertice == aresta.get_vertice_u):
                    adjs.append(aresta)
                    '''
        return adjs
        
    '''
    def caminho_s_t(self, vertice: Vertice):
        for aresta in self.adj(vertice):
            if self.t == aresta.get_vertice_u():
                return True
            elif self.t == aresta.get_vertice_v():
                return True
            #print(aresta.get_vertice_u())
            '''
'''
    def caminho_dfs(self, visitados: list[Vertice]):
        for vertice in self.vertices:
            visitados.append(vertice)
            for adjacencia in self.adj(vertice):
                if adjacencia not in visitados:
                    self.caminho_dfs(self, visitados)
'''
        
class RedeResidual(Rede):
    
    def __init__(self, vertices: list[Vertice], arestas: list[Aresta]):
       self.caminho_aumentante = []
       super().__init__(vertices ,arestas)
    
    def get_fluxo_rede(self):
        return self.F
    
    def get_caminho_aumentante(self):
        return self.caminho_aumentante
    
    def set_fluxo_rede(self, a: Aresta):
        self.F = a.get_capacidade()
        
    def set_caminho_aumentante(self, caminho_aumentante: list):
        self.caminho_aumentante = caminho_aumentante
     
    def get_arestas_rede_residual(self):
        return self.arestas

  #  def definir_arestas_diretas(self):
   #     for aresta in self.arestas:
    #        if aresta.get_capacidade - aresta.get_fluxo > 0:
     #           aresta.set_capacidade( aresta.get_capacidade + (aresta.get_capacidade - aresta.set_fluxo))
      #          aresta.set_aresta_direta()
    
    #def definir_arestas_contrarias(self):
     #   for aresta in self.arestas:
      #      if aresta.get_fluxo > 0 and aresta.get_capacidade == aresta.get_fluxo:
       #         verticev = aresta.get_vertice_v
        #        verticeu = aresta.get_vertice_u
         #       aresta.set_vertice_u = verticev
          #      aresta.set_vertice_v = verticeu
           #     aresta.set_capacidade(aresta.get_fluxo)

    def diferenciar_arestas(self):
        for aresta in self.arestas:
            if aresta.get_capacidade() - aresta.get_fluxo() > 0:
                aresta.set_capacidade(aresta.get_capacidade() + (aresta.get_capacidade() - aresta.set_fluxo()))
                aresta.set_aresta_direta()
            else:
                verticev = aresta.get_vertice_v()
                verticeu = aresta.get_vertice_u()
                aresta.set_vertice_u(verticev)
                aresta.set_vertice_v (verticeu)
                aresta.set_capacidade(aresta.get_fluxo)
    '''def caminho_dfs(self, visitados: list[Vertice]):
        for vertice in self.vertices:
            visitados.append(vertice)
            for adjacencia in self.adj(vertice):
                if adjacencia not in visitados:
                    self.set_fluxo()
                    self.caminho_dfs(self, adjacencia, visitados)'''
                    
    def bfs(self, vertice_inicial: Vertice):
        for vertice in self.get_vertices():
            vertice.set_cor(0)
            vertice.set_antecessor(None)
            
        # vertice_inicial.set_cor(1)
        
        fila = [vertice_inicial]
        
        while len(fila) > 0:
            vertice_atual = fila.pop(0)
            # print("aq1")
            for adjacencia in self.adj(vertice_atual):
                # print("aq2")
                # # fila.append(adjacencia.u)
                # # print(adjacencia.get_vertice_u().get_content())
                # print(self.adj(vertice_atual)[0].get_vertice_v().get_content())
                if(adjacencia.get_vertice_v().get_cor() == 0):
                    #print("aq3")
                    adjacencia.get_vertice_v().set_cor(1)
                    adjacencia.get_vertice_v().set_antecessor(adjacencia.get_vertice_u())
                    fila.append(adjacencia.get_vertice_v())
                
            vertice_inicial.set_cor(2)
        
        if self.get_vertices()[-1].get_antecessor():
            return True
        return False
    
    def encontrar_caminho_aumentante(self):
        vertice_final = self.get_vertices()[-1]
        caminho_aumentante = self.get_caminho_aumentante()
        
        v2 = vertice_final
        v1 = vertice_final.get_antecessor()
        
        while v1 != self.vertices[0]:
            for aresta in self.arestas:
                if aresta.get_vertice_u() == v1 and aresta.get_vertice_v() == v2:
                    caminho_aumentante.insert(0, aresta)
            v2 = v1
            v1 = v2.get_antecessor()
            
            if v1 == None:  # testa para erro no caminho
                return False
            
        return True
    
    def resetar_vertices_bfs(self):
        for vertice in self.get_vertices():
            vertice.set_cor(0)
            vertice.set_antecessor(None)
    
    
vertice1 = Vertice("Vertice1")
vertice2 = Vertice("Vertice2")
vertice3 = Vertice("Vertice3")
vertice4 = Vertice("Vertice4") 

aresta1 = Aresta(2,3,vertice1,vertice2)
aresta2 = Aresta(3,5,vertice2,vertice3)
aresta3 = Aresta(1,2,vertice3,vertice4)
# aresta4 = Aresta(2, 2, vertice3, vertice4)

rede = Rede([vertice1,vertice2,vertice3,vertice4],[aresta1,aresta2,aresta3])
rede_residual = RedeResidual([vertice1,vertice2,vertice3,vertice4],[aresta1,aresta2,aresta3])    
#rede_residual = RedeResidual()
#print(rede_residual.encontrar_caminho_aumentante())
'''
while rede.bfs(vertice1):
    
    fluxo_antigo = rede_residual.set_fluxo_rede(aresta1)
    for aresta in rede_residual.get_arestas_rede_residual():
        if aresta.get_fluxo() < fluxo_antigo:
            rede_residual.set_fluxo_rede(aresta.get_fluxo())
           
    for aresta in rede.get_arestas():
        if aresta.get_aresta_direta() == True:
            aresta.set_fluxo(aresta.get_fluxo() + rede_residual.get_fluxo_rede())     
        else:
            aresta.set_fluxo(aresta.get_fluxo() - rede_residual.get_fluxo_rede())  

'''
conditio_while = rede_residual.bfs(vertice1)
rede_residual.diferenciar_arestas()
while conditio_while == True:
    print("loop")
    rede_residual.encontrar_caminho_aumentante()
    for aresta in rede_residual.get_arestas():
        if aresta.get_aresta_direta() == True:
            aresta.set_fluxo(aresta.get_fluxo() + rede_residual.get_fluxo_rede())     
        else:
            aresta.set_fluxo(aresta.get_fluxo() - rede_residual.get_fluxo_rede()) 
    rede_residual.set_fluxo(rede_residual.get_fluxo() + rede_residual.get_fluxo_rede())
    rede_residual.resetar_vertices_bfs()
    print(rede_residual.get_fluxo())
    conditio_while = rede_residual.bfs(vertice1)