import { createRouter, createWebHistory } from "vue-router"
import Home from "./views/Home.vue"
import ProneAppDemo from "./views/ProneAppDemo.vue"

const routes = [
    {
        name: 'Home',
        path: '/',
        component: Home
    },
    {
        name: 'ProneAppDemo',
        path: '/ProneAppDemo',
        component: ProneAppDemo
    },

]


const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router