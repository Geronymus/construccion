<template>
  <div id="app">    
    <UsuarioComponent msg="Mensaje desde App.vue"/>
    <MostrarUsuerioComponent msg="Mensaje desde App.vue"/>
  </div>
</template>

<script>
import UsuarioComponent from './components/UsuarioComponent.vue';
import MostrarUsuerioComponent from './components/MostrarUsuerioComponent.vue';
export default {
  name: 'App',
  components: {
    UsuarioComponent,
    MostrarUsuerioComponent
}
}
</script>