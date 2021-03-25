import { createRouter, createWebHistory } from "vue-router"
import Home from "./views/Home.vue"
import Strokeinput from "./views/StrokeInput.vue"

const routes = [
    {
        name: 'Home',
        path: '/',
        component: Home
    },
    {
        name: 'Strokeinput',
        path: '/strokeinput',
        component: Strokeinput
    },

]


const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router