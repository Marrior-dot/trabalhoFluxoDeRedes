class Vertice:
    def __init__(self, content):
        self.content = content
    
    def get_content(self):
        return self.content
    
class Aresta:
    def __init__(self,ce,fe,u,v):
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
    
    def get_verticeu(self):
        return self.u
    
    def get_vertice_v(self):
        return self.v

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
    
    def fe0(self):
        for aresta in self.arestas:
            aresta.set_fluxo(0)
    
class RedeResidual(Rede):
    def __init__(self):
        self.definir_arestas_diretas
    
    def definir_arestas_diretas(self):
        for aresta in self.arestas:
            if aresta.get_capacidade - aresta.get_fluxo > 0:
                aresta.set_capacidade( aresta.get_capacidade + (aresta.get_capacidade - aresta.set_fluxo))
    
    def definir_arestas_contrarias(self):
        for aresta in self.arestas:
            if aresta.get_fluxo > 0 and aresta.get_capacidade == aresta.get_fluxo:
                aresta.
                
            