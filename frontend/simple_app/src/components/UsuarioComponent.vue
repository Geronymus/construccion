<template>
  <div>
    <h1>Create/Update User</h1>
    <form @submit.prevent="submit">
      <!-- Formulario para crear o actualizar usuarios -->
      <div>
        <label for="dni">DNI:</label>
        <input type="text" id="dni" v-model="dni" required>
      </div>
      <div>
        <label for="passw">Password:</label>
        <input type="password" id="passw" v-model="passw" required>
      </div>
      <div>
        <label for="nombre">Nombre:</label>
        <input type="text" id="nombre" v-model="nombre" required>
      </div>
      <div>
        <label for="apellido">Apellido:</label>
        <input type="text" id="apellido" v-model="apellido" required>
      </div>
      <div>
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required>
      </div>
      <div>
        <label for="foto">Foto:</label>
        <input type="file" id="foto" ref="fileInput" accept="image/*" required>
      </div>
      <button type="submit">Create</button>
      <button type="button" @click="update">Update</button>
    </form>

    <h1>Delete User</h1>
    <form @submit.prevent="deleteUser">
      <!-- Formulario para eliminar un usuario -->
      <div>
        <label for="dniToDelete">DNI:</label>
        <input type="text" id="dniToDelete" v-model="dniToDelete" required>
      </div>

      <!-- Botón para eliminar usuario -->
      <button type="submit">Delete</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      dni: '',
      passw: '',
      nombre: '',
      apellido: '',
      email: '',
      dniToDelete: ''
    };
  },
  methods: {
    submit() {
      const formData = new FormData();
      formData.append('dni', JSON.stringify(this.dni));
      formData.append('passw', JSON.stringify(this.passw));
      formData.append('nombre', JSON.stringify(this.nombre));
      formData.append('apellido', JSON.stringify(this.apellido));
      formData.append('email', JSON.stringify(this.email));
      formData.append('file', this.$refs.fileInput.files[0]);

      const config = {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      };

      this.$http.put('http://127.0.0.1:5000/usuario', formData, config)
        .then(response => {
          console.log(response.data);
          // Aquí puedes realizar alguna acción después de crear el usuario
          this.resetForm();
        })
        .catch(error => {
          console.log(error);
          // Aquí puedes manejar el error en caso de que ocurra
        });
    },
    update() {
      const formData = new FormData();
      formData.append('dni', JSON.stringify(this.dni));
      formData.append('passw', JSON.stringify(this.passw));
      formData.append('nombre', JSON.stringify(this.nombre));
      formData.append('apellido', JSON.stringify(this.apellido));
      formData.append('email', JSON.stringify(this.email));
      formData.append('file', this.$refs.fileInput.files[0]);

      const config = {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      };

      this.$http.patch('http://127.0.0.1:5000/usuario', formData, config)
        .then(response => {
          console.log(response.data);
          // Aquí puedes realizar alguna acción después de actualizar el usuario
          this.resetForm();
        })
        .catch(error => {
          console.log(error);
          // Aquí puedes manejar el error en caso de que ocurra
        });
    },
    deleteUser() {
      const xhr = new XMLHttpRequest();
      xhr.open('DELETE', 'http://127.0.0.1:5000/usuario');
      xhr.setRequestHeader('Content-Type', 'application/json');

      xhr.onload = () => {
        if (xhr.status === 200) {
          console.log('Usuario eliminado');
          // Aquí puedes realizar alguna acción después de eliminar el usuario
          this.resetDeleteForm();
        } else {
          console.log('Error al eliminar el usuario');
          // Aquí puedes manejar el error en caso de que ocurra
        }
      };

      xhr.send(JSON.stringify({ dni: this.dniToDelete }));
    },
    resetForm() {
      this.dni = '';
      this.passw = '';
      this.nombre = '';
      this.apellido = '';
      this.email = '';
      this.$refs.fileInput.value = '';
    },
    resetDeleteForm() {
      this.dniToDelete = '';
    }
  }
};
</script>
