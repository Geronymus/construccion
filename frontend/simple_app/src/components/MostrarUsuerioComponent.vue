<template>
    <div>
      <h1>Mostrar Usuarios</h1>
      <table class="table">
        <thead>
          <tr>
            <th>DNI</th>
            <th>Password</th>
            <th>Nombre</th>
            <th>Apellido</th>
            <th>Email</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="usuario in usuarios" :key="usuario.dni">
            <td>{{ usuario.dni }}</td>
            <td>{{ usuario.passw }}</td>
            <td>{{ usuario.nombre }}</td>
            <td>{{ usuario.apellido }}</td>
            <td>{{ usuario.email }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        usuarios: []
      };
    },
    created() {
      this.fetchUsuarios();
    },
    methods: {
      fetchUsuarios() {
        const config = {
          headers: {
            'Content-Type': 'application/json'
          }
        };
  
        this.$http.post('http://127.0.0.1:5000/usuarios', {}, config)
          .then(response => {
            this.usuarios = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      }
    }
  };
  </script>
  
  <style>
  /* Estilos adicionales según tus preferencias */
  </style>
  