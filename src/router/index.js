import { createRouter, createWebHistory } from 'vue-router'
import NoticiasView from '../views/NoticiasView.vue'
import ArtigosView from '../views/ArtigosView.vue'
import PalestrasView from '../views/PalestrasView.vue'
const routes = [
    {
        path: '/',
        name: 'Notícias',
        component: NoticiasView
    },
    {
        path: '/artigos',
        name: 'Artigos',
        component: ArtigosView
    },
    {
        path: '/palestras',
        name: 'Palestras',
        component: PalestrasView
    }
]

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes
})

export default router