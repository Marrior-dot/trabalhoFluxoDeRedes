class Vertice:
    def __init__(self, content):
        self.content = content
    
    def get_content(self):
        return self.content
    
class Aresta:
    def __init__(self,ce,fe,u: Vertice,v: Vertice):
        self.fe = fe
        self.ce = ce 
        self.u = u
        self.v = v
    
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
    
    def set_fluxo(self, novo_fluxo):
        self.F = novo_fluxo
    
    def fe0(self):
        for aresta in self.arestas:
            aresta.set_fluxo(0)
    
    def adj(self, vertice: Vertice):
        adjs = []
        for aresta in self.arestas:
            
            if vertice == aresta.get_vertice_u:
                adjs.append(aresta)
            elif vertice == aresta.get_vertice_v:
                adjs.append(aresta)
            '''
            for vertices in self.vertices:
                if(vertice == aresta.get_vertice_v and vertices == aresta.get_vertice_u):
                    adjs.append(aresta)
                elif(vertices == aresta.get_vertice_v and vertice == aresta.get_vertice_u):
                    adjs.append(aresta)
                    '''
        return adjs

    def caminho_dfs(self, visitados: list[Vertice]):
        for vertice in self.vertices:
            visitados.append(vertice)
            for adjacencia in self.adj(vertice):
                if adjacencia not in visitados:
                    
                    self.caminho_dfs(self, adjacencia, visitados)

        
class RedeResidual(Rede):
    
    def set_fluxo_rede(self, v: Vertice):
        fluxo_residual = self.adj(v)
        return fluxo_residual
        #for adjs in self.adj(v):
            

'''
    def definir_arestas_diretas(self):
        for aresta in self.arestas:
            if aresta.get_capacidade - aresta.get_fluxo > 0:
                aresta.set_capacidade( aresta.get_capacidade + (aresta.get_capacidade - aresta.set_fluxo))
    
    def definir_arestas_contrarias(self):
        for aresta in self.arestas:
            if aresta.get_fluxo > 0 and aresta.get_capacidade == aresta.get_fluxo:
                verticev = aresta.get_vertice_v
                verticeu = aresta.get_vertice_u
                aresta.set_vertice_u = verticev
                aresta.set_vertice_v = verticeu
                aresta.set_capacidade(aresta.get_fluxo)
                    
                
    def caminho_dfs(self, visitados: list[Vertice]):
        for vertice in self.vertices:
            visitados.append(vertice)
            for adjacencia in self.adj(vertice):
                if adjacencia not in visitados:
                    self.set_fluxo()
                    self.caminho_dfs(self, adjacencia, visitados)
'''                
vertice1 = Vertice("Vertice1")
vertice2 = Vertice("Vertice2")
vertice3 = Vertice("Vertice3")
vertice4 = Vertice("Vertice4") 

aresta1 = Aresta(2,3,vertice1,vertice2)
aresta2 = Aresta(3,5,vertice2,vertice3)
aresta3 = Aresta(1,2,vertice2,vertice3)

rede = Rede([vertice1,vertice2,vertice3,vertice4],[aresta1,aresta2,aresta3])
rede_residual = RedeResidual([vertice1,vertice2,vertice3,vertice4],[aresta1,aresta2,aresta3])    

print(rede.get_arestas())
print(rede.adj(vertice1))