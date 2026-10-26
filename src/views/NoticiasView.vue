<script setup>
import { useNoticiasStore } from '@/stores/useNoticiasStore';
const noticiasStore = useNoticiasStore()
</script>
<template>
    <h2>Notícias</h2>
    <div v-for="noticia in noticiasStore.noticias" :key="noticia.id">
        <h3> {{  noticia.titulo }}</h3>
        <p> {{ noticia.descricao }} - {{ noticia.autor }} </p>
    </div>
</template>
