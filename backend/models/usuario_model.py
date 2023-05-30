from backend.models.postgres_connection_pool2 import PostgreSQLPool

class UsuarioModel:
    def __init__(self):        
        self.mysql_pool = PostgreSQLPool()

    def get_usuario(self, id_usuario):    
        params = {'id_usuario' : id_usuario}      
        rv = self.mysql_pool.execute("SELECT * from usuario where id_usuario=%(id_usuario)s", params)
        data = []
        content = {}
        for result in rv:
            content = {'id_usuario': result[0], 'dni': result[1], 'passw': result[2],'foto': result[3],'vector': result[4],'nombre': result[5], 'apellido': result[6], 'email': result[7]}
            data.append(content)
            content = {}
        return data

    def get_usuarios(self):  
        rv = self.mysql_pool.execute("SELECT * from usuario")  
        data = []
        content = {}
        for result in rv:
            content = {'id_usuario': result[0], 'dni': result[1], 'passw': result[2],'foto': result[3],'vector': result[4],'nombre': result[5], 'apellido': result[6], 'email': result[7]}
            data.append(content)
            content = {}
        return data

    def create_usuario(self, dni, passw,foto,vector,nombre,apellido,email):    
        data = {
            'dni' : dni,
            'passw' : passw,
            'foto' : foto,
            'vector' : vector,
            'nombre' : nombre,
            'apellido' : apellido,
            'email' : email
        }  
        query = """insert into usuario (dni, passw,foto,vector,nombre,apellido,email) 
            values (%(dni)s, %(passw)s,%(foto)s,%(vector)s, %(nombre)s, %(apellido)s, %(email)s)"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        data['id_usuario'] = cursor.lastrowid
        return data

    def update_usuario(self, dni, passw,foto,vector,nombre,apellido,email):    
        data = {
            'dni' : dni,
            'passw' : passw,
            'foto' : foto,
            'vector' : vector,
            'nombre' : nombre,
            'apellido' : apellido,
            'email' : email
        }  
        query = """update usuario set passw = %(passw)s,foto = %(foto)s,vector = %(vector)s, nombre = %(nombre)s, apellido = %(apellido)s, email = %(email)s
                where dni = CAST(%(dni)s AS VARCHAR)"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_usuario(self, dni):    
        params = {'dni' : dni}      
        query = """delete from usuario where dni = CAST(%(dni)s AS VARCHAR)"""   
        self.mysql_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 