import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const Flight = () => import('@/views/flight/index.vue')
const Stand = () => import('@/views/stand/index.vue')
const Baggage = () => import('@/views/baggage/index.vue')
const Bridge = () => import('@/views/bridge/index.vue')
const Stairs = () => import('@/views/stairs/index.vue')
const RefuelAviation = () => import('@/views/refuel_aviation/index.vue')
const Water = () => import('@/views/water/index.vue')
const Lavatory = () => import('@/views/lavatory/index.vue')
const Catering = () => import('@/views/catering/index.vue')
const Deicing = () => import('@/views/deicing/index.vue')
const Pushback = () => import('@/views/pushback/index.vue')
const Gpu = () => import('@/views/gpu/index.vue')
const Acu = () => import('@/views/acu/index.vue')
const Ramp = () => import('@/views/ramp/index.vue')
const Fodb = () => import('@/views/fodb/index.vue')
const BoardGate = () => import('@/views/board_gate/index.vue')
const CrewGround = () => import('@/views/crew_ground/index.vue')
const EquipmentGround = () => import('@/views/equipment_ground/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/flight', name: 'flight', component: Flight },
    { path: '/stand', name: 'stand', component: Stand },
    { path: '/baggage', name: 'baggage', component: Baggage },
    { path: '/bridge', name: 'bridge', component: Bridge },
    { path: '/stairs', name: 'stairs', component: Stairs },
    { path: '/refuel_aviation', name: 'refuel_aviation', component: RefuelAviation },
    { path: '/water', name: 'water', component: Water },
    { path: '/lavatory', name: 'lavatory', component: Lavatory },
    { path: '/catering', name: 'catering', component: Catering },
    { path: '/deicing', name: 'deicing', component: Deicing },
    { path: '/pushback', name: 'pushback', component: Pushback },
    { path: '/gpu', name: 'gpu', component: Gpu },
    { path: '/acu', name: 'acu', component: Acu },
    { path: '/ramp', name: 'ramp', component: Ramp },
    { path: '/fodb', name: 'fodb', component: Fodb },
    { path: '/board_gate', name: 'board_gate', component: BoardGate },
    { path: '/crew_ground', name: 'crew_ground', component: CrewGround },
    { path: '/equipment_ground', name: 'equipment_ground', component: EquipmentGround },
  ],
})

export default router
